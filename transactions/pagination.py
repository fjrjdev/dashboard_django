from rest_framework import pagination
from rest_framework.views import Response
from collections import OrderedDict
from .utils import get_balance
from transactions.models import Transaction


class CustomPageNumber(pagination.PageNumberPagination):
    page_size = 25

    def get_paginated_response(self, data):
        balance_total = get_balance(Transaction=Transaction)
        print(self.page.paginator.count)
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
