import ipdb


def get_balance(queryset):
    values = []
    for transaction in queryset:
        values.append(transaction)
    minus_list = ["2", "3", "9"]
    total = 0
    for item in values:
        total += item.value
        if item.transaction in minus_list:
            total -= item.value
    return round(total, 2)


def get_stores_in_db(queryset):
    values = []
    for store in queryset():
        values.append(store)
    store_names_list = []
    for item in values:
        if item.store not in store_names_list:
            store_names_list.append(item.store)
    return store_names_list
