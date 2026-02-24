"""
Interface for calculator operations.
"""

class OperatorInterface:
    def __init__(self, operator):
        self.operator = operator

    def get_name(self):
        pass

    def execute(self, a, b):
        pass
