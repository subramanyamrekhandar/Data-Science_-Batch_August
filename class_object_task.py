class Dog:
    
    # initalize the attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def decription(self):
        return f"{self.name} is {self.age} years old"

# creating instance of the class (Dog)
dog1 = Dog("Subbu", 3)

# accessing class atteribute and method
print(dog1.decription())

