from core.interface import OperatorInterface


class Power(OperatorInterface):
    def __init__(self):
        super().__init__("power")

    def get_name(self):
        return self.operator

    def execute(self, a, b):
        return a**b
