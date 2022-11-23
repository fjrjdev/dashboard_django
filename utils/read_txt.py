#  max_length = [1, 8, 10, 11, 12, 6, 14, 19]
#         description = [
#             "transaction",
#             "date",
#             "value",
#             "cpf",
#             "card",
#             "hour",
#             "owner",
#             "store",
#         ]
def read_txt(data_file, max_length: list[int], description: list[str]) -> list:
    with open(data_file, "r", encoding="utf-8") as data:
        file = [item for item in data]
        res = []
        for line in file:
            strt = 0
            dict_item = {}
            for index, size in enumerate(max_length):
                dict_item.update({f"{description[index]}": line[strt : strt + size]})
                strt += size
            res.append(dict_item)
        return res
