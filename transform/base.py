from abc import ABC, abstractmethod

class BaseTransform(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError