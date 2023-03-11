# python-exercises/programming/solid/liskov_substitute.py

from abc import abstractmethod, ABC

class Bird(ABC):

    def __init__(self, name: str) -> None:
        self.name  = name
    
    @abstractmethod
    def do_sound(self) -> str:
        pass

class FlyingBird(Bird):

    @abstractmethod
    def fly(self) -> None:
        pass

class SwimmingBird(Bird):

    @abstractmethod
    def swim(self) -> None:
        pass

class Crow(FlyingBird):

    def fly(self) -> None:
        print(f"{self.name} is flying high & fast!!!")

    def do_sound(self) -> str:
        return "Caw!"

class Duck(SwimmingBird, FlyingBird):

    def fly(self) -> None:
        print(f"{self.name} is not flying high & fast!!!")

    def swim(self) -> None:
        print(f"{self.name} swims in the lake and quack!!!")

    def do_sound(self) -> str:
        return "Quack!"

