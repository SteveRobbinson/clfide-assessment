class ValidationError(Exception):
    def __init__(self, base_message: str, details: str | None = None):
        self.base_message = base_message
        self.details = details

        error_message = f"{base_message}\n{details}" if details else base_message

        super().__init__(error_message)


class InvalidMathExpressionError(ValidationError):
    def __init__(self, base_message: str = "Given math expression is invalid!", details: str | None = None):
        super().__init__(base_message, details)


class InvalidColumnNameError(ValidationError):
    def __init__(self, base_message: str = "Input column name is incorrect! Allowed characters: (a-z) and (_).", details: str | None = None):
            super().__init__(base_message, details)

