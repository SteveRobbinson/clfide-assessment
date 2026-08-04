import pandas as pd
import re

def has_required_columns(df: pd.DataFrame, columns: list[str]) -> bool:
    return set(columns).issubset(df.columns)


def has_valid_column_name(column_name: str) -> bool:
    pattern = re.compile("^[a-z_]+$")
    return bool(pattern.fullmatch(column_name.strip()))

    broken = [x.strip() for x in column_names if not bool(pattern.fullmatch(x.strip()))]

    if broken:
        raise InvalidColumnNameError(details=f"These columns are invalid: {broken}")


def validate_numeric_columns(df: pd.DataFrame, columns: list[str]) -> None:

    non_numeric = [col for col in columns if not pd.api.types.is_numeric_dtype(df[col])]
    
    if non_numeric:
        raise InvalidColumnTypeError(details=f"The following columns are not numeric: {non_numeric}")
