import pandas as pd
from exceptions import InvalidMathExpressionError
from validators import validate_column_name
import operator
from typing import Callable

def parse_role_expression(role: str, allowed_operators: str = '+-*') -> tuple[list[str], str]:
    
    operator = [znak for znak in role if znak in allowed_operators] 
    if len(operator) != 1:
        raise InvalidMathExpressionError(f"Expected 1, got {len(operator)}")

    lista = role.split(operator[0])
    lista = [x.strip() for x in lista]

    for x in lista:
        if len(x) == 0:
            raise InvalidMathExpressionError()

    validate_column_name(lista)

    return lista, operator[0]


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
