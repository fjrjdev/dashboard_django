from rest_framework import pagination
from rest_framework.views import Response
from collections import OrderedDict
from .utils import get_balance
from transactions.models import Transaction
from rest_framework.exceptions import NotFound
from django.core.paginator import InvalidPage


class CustomPageNumber(pagination.PageNumberPagination):
    page_size = 25

    def get_paginated_response(self, data):
        print(self.queryset)
        balance_total = get_balance(queryset=self.queryset)
        return Response(
            OrderedDict(
                [
                    ("last_page", self.page.paginator.num_pages),
                    ("count", self.page.paginator.count),
                    ("current", self.page.number),
                    ("balance_total", balance_total),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )

    def paginate_queryset(self, queryset, request, view=None):

        page_size = self.get_page_size(request)
        if not page_size:
            return None
        self.queryset = queryset
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            self.display_page_controls = True

        self.request = request
        return list(self.page)
