import pandas as pd
import re

def has_required_columns(df: pd.DataFrame, columns: list[str]) -> bool:
    return set(columns).issubset(df.columns)


def has_valid_column_name(column_name: str) -> bool:
    pattern = re.compile("^[a-z_]+$")
    return bool(pattern.fullmatch(column_name.strip()))


def are_columns_numeric_type(df: pd.DataFrame, columns: list[str]) -> bool:
    return pd.api.types.is_numeric_dtype(df[columns].values)
