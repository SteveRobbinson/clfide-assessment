import pandas as pd
import re
from exceptions import InvalidColumnNameError, InvalidColumnTypeError

def validate_column_exists(df: pd.DataFrame, columns: list[str]) -> None:

    non_existing = [x for x in columns if x not in df.columns]

    if non_existing:
        raise InvalidColumnNameError(f"Columns {non_existing} do not exist in the DataFrame")


def validate_column_name(column_names: str | list[str]) -> None:
    
    if isinstance(column_names, str):
        column_names = [column_names]

    pattern = re.compile("^[a-z_]+$")

    broken = [x.strip() for x in column_names if not bool(pattern.fullmatch(x.strip()))]

    if broken:
        raise InvalidColumnNameError(f"These columns are invalid: {broken}")


def validate_numeric_columns(df: pd.DataFrame, columns: list[str]) -> None:

    non_numeric = [col for col in columns if not pd.api.types.is_numeric_dtype(df[col])]
    
    if non_numeric:
        raise InvalidColumnTypeError(f"The following columns are not numeric: {non_numeric}")
