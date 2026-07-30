class ValidationError(Exception):
    pass

class InvalidMathExpressionError(ValidationError):
    def __init__(self, message: str | None = None):
        base_msg = "Given math expression is invalid!\nAllowed operators: +, -, *"
        if message:
            super().__init__(f"{base_msg}\n{message}")
        else:
            super().__init__(f"{base_msg}")

class InvalidColumnNameError(ValidationError):
    def __init__(self, message: str | None = None):
        base_msg = "Input column name is incorrect! Allowed characters: _ and (a-z)"
        if message:
            super().__init__(f"{base_msg}\n{message}")
        else:
            super().__init__(f"{base_msg}")

class InvalidColumnTypeError(ValidationError):
    def __init__(self, message: str | None = None):
        base_msg = "Column type mismatch: numeric type expected"
        if message:
            super().__init__(f"{base_msg}\n{message}")
        else:
            super().__init__(base_msg)
