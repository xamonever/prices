from abc import ABC, abstractmethod

from .abs_messege import AbstractMessege 
from .abs_attachment import AbstractAttachment 


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def get_messege(self) -> AbstractMessege:
        pass

    @abstractmethod
    def get_attachment(self) -> AbstractAttachment:
        pass