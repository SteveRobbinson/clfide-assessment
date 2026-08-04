import pandas as pd
from utils import parse_role_expression, add_calculated_column
from validators import has_valid_column_name, has_required_columns, are_columns_numeric_type

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str):

    parsed_expression, operators = parse_role_expression(role)

    if len(operators) != 1:
        return pd.DataFrame([])

    if len(parsed_expression) != 3:
        return pd.DataFrame([])

    if parsed_expression[1] not in operators:
        return pd.DataFrame([])


    expression_columns = list(set(parsed_expression).difference(operators))

    for col in [new_column, *expression_columns]:
        if not has_valid_column_name(col):
            return pd.DataFrame([])

    if not has_required_columns(df, expression_columns):
        return pd.DataFrame([])

    if not are_columns_numeric_type(df, expression_columns):
        return pd.DataFrame([])

    return add_calculated_column(df, new_column, expression_columns, list(operators)[0])
