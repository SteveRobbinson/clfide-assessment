import pandas as pd
import re
from exceptions import InvalidColumnNameError, InvalidColumnTypeError

def validate_column_exists(df: pd.DataFrame, columns: list[str]) -> None:

    non_existing = []

    for x in columns:
        if x not in df.columns:
            non_existing.append(x)

    if non_existing:
        raise InvalidColumnNameError(f"Columns {non_existing} do not exist in the DataFrame")


def validate_column_name(column_name: str) -> None:
    
    pattern = re.compile("^[a-z_]+$")
    
    if not bool(pattern.fullmatch(column_name.strip())):
        raise InvalidColumnNameError()


def validate_numeric_columns(df: pd.DataFrame, columns: list[str]) -> None:

    non_numeric = []
    
    for col in columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            non_numeric.append(col)
            
    if non_numeric:
        raise InvalidColumnTypeError(f"The following columns are not numeric: {non_numeric}")
