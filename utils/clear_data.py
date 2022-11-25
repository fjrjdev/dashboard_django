import pandas as pd
from utils.read_txt import read_txt
import json


def hour_format(i: str) -> str:
    return f"{i[0:2]}:{i[2:4]}:{i[4:6]}"


def convert_values_by_100(value: str) -> float:
    return float(value) / 100.00


def convert_text(string: str) -> str:
    return string.rstrip()


def clear_data(data_file, max_length, description):
    txt = read_txt(data_file, max_length, description)
    df = pd.DataFrame(txt)

    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    df["date"] = df["date"].astype(str)
    df["transaction"] = df["transaction"].astype(str)
    df["hour"] = df["hour"].apply(hour_format)
    df["value"] = df["value"].apply(convert_values_by_100)
    df["owner"] = df["owner"].apply(convert_text)
    df["store"] = df["store"].apply(convert_text)

    return df
