# python-exercises/programming/solid/main.py

from single_resp import Duck, Communicator
if __name__ == '__main__':
    d1 = Duck("John")
    d2 = Duck("Peter")
    commn = Communicator("greeting")
    commn.communicate(d1, d2)
