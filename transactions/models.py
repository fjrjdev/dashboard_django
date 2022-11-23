from django.db import models
import ipdb


class Transaction(models.Model):
    transaction = models.CharField(max_length=1)
    date = models.CharField(max_length=10)
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=8)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_balance(self):
        values = []
        for transaction in Transaction.objects.all():
            values.append(transaction)
        minus_list = ["2", "3", "9"]
        total = 0
        for item in values:
            total += item.value
            if item.transaction in minus_list:
                total -= item.value
        return round(total, 2)
