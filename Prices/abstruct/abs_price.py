from abc import ABC, abstractmethod

class AbstractPrice(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def get_input_data(self) -> tuple:
    	pass