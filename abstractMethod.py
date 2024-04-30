from abc import ABC, abstractmethod

class Parent:

    def display(self):
        pass

class child(Parent):
    def display(self):
        print("this is diplay method")

obj1=child()
obj1.display()