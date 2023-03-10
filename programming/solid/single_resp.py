# python-exercises/programming/solid/single_resp.py

class Duck:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def fly(self) -> None:
        print(f"{self.name} is not flying very high!")
    
    def swim(self) -> None:
        print(f"{self.name} swims in the lake, river & pond")
    
    def do_sound(self) -> str:
        return f"Quack!"

class Communicator:
    def __init__(self, channel):
        self.channel = channel
    
    def communicate(self, duck1: Duck, duck2: Duck):
        sentence1 = f"{duck1.name}: {duck1.do_sound()}, Hello {duck2.name}!!!"
        sentence2 = f"{duck2.name}: {duck2.do_sound()}, Hello {duck1.name}!!!"

        conversation = [sentence1, sentence2]
        print(*conversation, f"(via {self.channel})", sep = '\n')



    
