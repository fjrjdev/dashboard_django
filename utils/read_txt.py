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
