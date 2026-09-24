class Animal: #Parent class(superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("speaking now...")

class Dog(Animal):
    def speak(self):
        super().speak() #Calling the parent class method
        print("Woof!")


d = Dog("Bruno")
d.speak()
print(d.location)
