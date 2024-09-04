# Encapsulation
class Person:
    def __init__(self, name, age):
        self._name = name # private
        self._age = age # private
        
    # creating the object method
    def get_name(self):
        return self._name
    
    def set_age(self, age):
        if age > 0:
            self._age = age
        else: 
            print("Age must be possitive value")
            
    def display_info(self):
        print(f"Name: {self._name}, Age: {self._age}")

# creating the instance of the main class like Person
person = Person("Subbu", 24)
person.display_info()

print(person.get_name())
person.set_age(25)
# print(person.set_age())
person.display_info()
    
