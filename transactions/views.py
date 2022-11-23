from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView, Request, Response
from rest_framework.parsers import MultiPartParser
import json
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

from utils.clear_data import clear_data
from utils.write_file import write_file


max_length = [1, 8, 10, 11, 12, 6, 14, 19]
description = [
    "transaction",
    "date",
    "value",
    "cpf",
    "card",
    "hour",
    "owner",
    "store",
]


class ListCreateTransictionView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request: Request, format=None) -> Response:
        file_obj = request.data.get("file")
        temp_file = write_file(file_obj=file_obj)
        if not temp_file:
            return Response("Error")

        df = clear_data(
            data_file="media/tmp/CNAB.txt",
            max_length=max_length,
            description=description,
        )
        json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
        data = []
        for dict_item in json_list:
            instance = Transaction.objects.create(**dict_item)
            data.append(instance)

        serializer = TransactionSerializer(data=data, many=True)
        serializer.is_valid()

        return Response(serializer.data)
