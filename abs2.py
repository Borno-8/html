from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can think, then walk or run.")

class Snake(Animal):

    def move(self):
        print("I can hiss and bite.")

class Bird(Animal):

    def move(self):
        print("I can fly high.")

class Fish(Animal):

    def move(self):
        print("I can swim very fast.")

class Cheetah(Animal):

    def move(self):
        print("I can run very fast.") 

R = Human()
R.move()

S = Snake()
S.move()

B = Bird()
B.move()

F = Fish()
F.move()

C = Cheetah()
C.move()