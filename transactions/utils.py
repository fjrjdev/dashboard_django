def get_balance(Transaction):
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
