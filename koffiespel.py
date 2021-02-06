import random
import sys

class KoffieSpel:
    def __init__(self):
        self.getal = random.randint(1, 100)

    def play(self):
        pass

    def ask(self, out=sys.stdout):
        out.write("I have a number in mind between 1 and 100, guess which it is: ")
        guess = input()

if __name__ == "__main__":
    a = KoffieSpel()
    a.play()
