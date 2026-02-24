from core.interface import OperatorInterface


class Add(OperatorInterface):
    def __init__(self):
        super().__init__("add")

    def get_name(self):
        return self.operator

    def execute(self, a, b):
        return a + b
