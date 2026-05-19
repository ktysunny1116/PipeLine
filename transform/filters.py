from .base import BaseTransform

class DataFilter(BaseTransform):
    def __init__(self, name, logic):
        self.name = name
        self.logic = logic

    def execute(self, data):
        return self.logic(data)