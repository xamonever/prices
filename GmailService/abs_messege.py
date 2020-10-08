from abc import ABC, abstractmethod

class AbstractMessege(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def get_id(self) -> str:
        pass