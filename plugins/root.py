from core.interface import OperatorInterface


class Root(OperatorInterface):
    def __init__(self):
        super().__init__("root")

    def get_name(self):
        return self.operator

    def execute(self, a, b):
        if a < 0:
            raise ValueError("Cannot calculate a root of a negative number")
        if b == 0:
            raise ValueError("Cannot calculate a root with zero as the index")
        return a ** (1 / b)
