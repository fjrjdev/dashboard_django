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
