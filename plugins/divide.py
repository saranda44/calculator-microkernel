from core.interface import OperatorInterface


class Divide(OperatorInterface):
    def __init__(self):
        super().__init__("divide")

    def get_name(self):
        return self.operator

    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
