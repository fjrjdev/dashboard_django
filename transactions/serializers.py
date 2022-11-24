from rest_framework import serializers
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "transaction",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            "owner",
            "store",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
