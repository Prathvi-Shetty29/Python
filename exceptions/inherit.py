class Mammal:
    def walk(self):
        print("walk")



class Dog(Mammal):
    def bark(self):
        print("barking")

class Cat(Mammal) :
    pass


rocky=Dog()
rocky.walk()
rocky.bark()
