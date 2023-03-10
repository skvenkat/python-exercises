# python-exercises/programming/solid/liskov_substitute.py

from abc import ABC, abstractmethod
from typing import final

from open_close import AbstractConversation

class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def swim(self):
        pass
    
    @abstractmethod
    def do_sound(self) -> str:
        pass
    
class Crow(Bird):
    def fly(self):
        print(f"{self.name} is flying high and fast!")
    
    def swim(self):
        raise NotImplementedError("Crows don't swim!")
    
    def do_sound(self) -> str:
        return "Caw!"

class Duck(Bird):
    def fly(self):
        print(f"{self.name} is not flying high!")
    
    def swim(self):
        print(f"{self.name} is swimming fast!")
    
    def do_sound(self) -> str:
        return "Quack!"

class SimpleConversation2(AbstractConversation):
    def __init__(self, bird1: Bird, bird2: Bird):
        self.bird1 = bird1
        self.bird2 = bird2
    
    def do_conversation(self, conv_type) -> list:
        sentence1, sentence2 = "", ""
        try:
            if conv_type == "greet":
                sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, hello {self.bird2.name}!"
                sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, hello {self.bird1.name}!"
            elif conv_type == "qa1":
                sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, can you swim?"
                sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, {self.bird2.swim()}!"
            elif conv_type == "qa2":
                sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, can you fly? {self.bird1.name}!"
                sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, {self.bird2.fly()}!"
            else:
                sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}"
                sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}"
        except Exception as e:
            print("Conversation went bad...",e)
        return [sentence1, sentence2]

class Communicator:
    def __init__(self, channel):
        self.channel = channel
    
    @final
    def communicate(self, conversation: AbstractConversation, conv_type: str):
        print(*conversation.do_conversation(conv_type),
            f"(via {self.channel})",
            sep = '\n'
        )