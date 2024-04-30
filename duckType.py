class Aeroplane:
    def fly(self):
        print("aeroplane fly with petrol")

class Bird:
    def fly(self):
        print("aeroplane fly with wings")

class Fish:
    def swim(self):
        print("Fish swim in sea")

for obj in Aeroplane(),Bird(),Fish():
    obj.fly()