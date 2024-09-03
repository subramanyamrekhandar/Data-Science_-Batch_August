# inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("subclass must implement this method")
class Dog(Animal):
    def speak(self):
        return f"{self.name} says something"
#creating instance of dog
dog = Dog("Buddy")

print(dog.speak())
