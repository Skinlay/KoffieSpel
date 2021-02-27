import random
import sys


class KoffieSpel:
    def __init__(self):
        self.getal = random.randint(1, 100)

    def play(self):
        self.ask(aantal=0)

    def ask(self, aantal, out=sys.stdout):
        if aantal == 0:
            out.write("I have a number in mind between 1 and 100, guess which it is: ")
        else:
            out.write("Try again! ")
        poging = int(input())
        self.check(poging=poging, out=out)

    def check(self, poging, out=sys.stdout):
        if poging > self.getal:
            out.write("Too high! ")
        elif poging < self.getal:
            out.write("Too low!")
        elif poging == self.getal:
            out.write('Correct!')
            sys.exit(0)
        else:
            out.write('How did you get in this part of the loop? You hacker!')
            sys.exit(1)


if __name__ == "__main__":
    a = KoffieSpel()
    a.play()
