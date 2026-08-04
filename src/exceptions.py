class ValidationError(Exception):
    def __init__(self, base_message: str, details: str | None = None):
        self.base_message = base_message
        self.details = details

        error_message = f"{base_message}\n{details}" if details else base_message

        super().__init__(error_message)


class InvalidMathExpressionError(ValidationError):
    def __init__(self, message: str | None = None):
        base_msg = "Given math expression is invalid!"
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
