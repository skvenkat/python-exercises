# python-exercises/programming/solid/main.py

from liskov_substitute import SimpleConversation2, Communicator
from interface_segregation import Duck, Crow

if __name__ == '__main__':
    d1 = Duck("John")
    d2 = Crow("Peter")
    scvs = SimpleConversation2(d1, d2)
    commn = Communicator("greeting")
    commn.communicate(scvs,"")
    commn.communicate(scvs,"greet")
    commn.communicate(scvs,"qa2")
    commn.communicate(scvs,"qa1")
