import random
import sys


class KoffieSpel:
    def __init__(self):
        self.getal = random.randint(1, 100)
        self.guess = -1

    def play(self):
        self.ask()

    def ask(self, out=sys.stdout):
        out.write("I have a number in mind between 1 and 100, guess which it is: ")
        self.guess = int(input())
        self.check(out=out)

    def check(self, out=sys.stdout):
        while self.guess != self.getal:
            if self.guess > self.getal:
                out.write("to high")
            elif self.guess < self.getal:
                out.write("to low")
            self.guess = int(input())
        out.write("correct")
        exit()


if __name__ == "__main__":
    a = KoffieSpel()
    a.play()
