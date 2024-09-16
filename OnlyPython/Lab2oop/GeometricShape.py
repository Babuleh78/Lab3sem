from abc import ABC, abstractmethod

class GeometricalShape(ABC):

    @abstractmethod
    def Area(self):
        pass