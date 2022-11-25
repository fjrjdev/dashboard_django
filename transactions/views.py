from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework.parsers import MultiPartParser
import json
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

from utils.clear_data import clear_data
from utils.write_file import write_file
from .utils import get_balance, get_stores_in_db
from .pagination import CustomPageNumber

MAX_LENGTH = [1, 8, 10, 11, 12, 6, 14, 19]
DESCRIPTION = [
    "transaction",
    "date",
    "value",
    "cpf",
    "card",
    "hour",
    "owner",
    "store",
]


class UploadTransictionView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request: Request, format=None) -> Response:
        file_obj = request.data.get("file", default=None)
        if file_obj is None:
            return Response(
                data={"file": "This field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        write_file(file_obj=file_obj)

        df = clear_data(
            data_file="media/tmp/CNAB.txt",
            max_length=MAX_LENGTH,
            description=DESCRIPTION,
        )
        json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
        data = []
        for dict_item in json_list:
            instance = Transaction.objects.create(**dict_item)
            data.append(instance)

        serializer = TransactionSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(
            data={"status": "Data Added with sucess", "rows": len(serializer.data)},
            status=status.HTTP_200_OK,
        )


class ListAllTransictionView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        self.pagination_class = CustomPageNumber
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListByStoreTransictionView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "store"

    def get(self, request, *args, **kwargs):
        stores = get_stores_in_db(queryset=Transaction.objects.all)
        store_name = self.kwargs["store"]
        if store_name.upper() not in stores:
            return Response(
                data={"detail": "Not found in stores list", "stores": stores},
                status=status.HTTP_404_NOT_FOUND,
            )

        self.queryset = Transaction.objects.filter(store__icontains=store_name.upper())
        queryset = self.filter_queryset(self.get_queryset())
        self.pagination_class = CustomPageNumber
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(data=serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        balance_total = get_balance(Transaction=Transaction)
        return Response({"balance_total": balance_total, "data": serializer.data})
