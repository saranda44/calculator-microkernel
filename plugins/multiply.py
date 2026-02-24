from core.interface import OperatorInterface


class Multiply(OperatorInterface):
    def __init__(self):
        super().__init__("multiply")

    def get_name(self):
        return self.operator

    def execute(self, a, b):
        return a * b
