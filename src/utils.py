import pandas as pd
import operator
from typing import Callable
import re

def parse_role_expression(role: str, allowed_operators: str = '+-*') -> tuple[list[str], set[str]]:

    operators = set(allowed_operators).intersection(role)
    parsed_expression = [x.strip() for x in re.split(f"([{''.join(operators)}])", role) if x and x.strip()]

    return parsed_expression, operators


def compute_new_column(df: pd.DataFrame,
                       new_column_name: str,
                       column_names: list[str],
                       math_operator: str,
                       allowed_operators: dict[str, Callable] = {'+': operator.add,
                                                                 '-': operator.sub,
                                                                 '*': operator.mul}
                      ) -> pd.DataFrame:
    
    func = allowed_operators[math_operator]
    df_new = df.copy()
    
    df_new[new_column_name] = func(df_new[column_names[0]], df_new[column_names[1]])
    
    return df_new
