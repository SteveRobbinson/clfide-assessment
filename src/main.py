import pandas as pd
from validators import validate_column_exists, validate_column_name, validate_numeric_columns
from utils import parse_role_expression, compute_new_column
from exceptions import InvalidMathExpressionError, InvalidColumnNameError

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    
    try:
        
        validate_column_name(new_column)
        column_names, math_operator = parse_role_expression(role)
        validate_column_exists(df, column_names)
        validate_numeric_columns(df, column_names)

        return compute_new_column(df, new_column, column_names, math_operator)

    except (InvalidMathExpressionError, InvalidColumnNameError) as err:
        print(f"{err}, returning an empty DataFrame")
        return pd.DataFrame([])
