from abc import ABC,abstractmethod

class Enterprise(ABC):
    @abstractmethod
    def calcYearExpenses():
        pass

class TechShop(Enterprise):
    def __init__(self):
        print("TechShop")

obj= TechShop()

#error