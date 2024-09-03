class Bird:
    def fly(self):
        print("Flying in the sky")
class Penguin(Bird):
    def fly(slef):
        print("I can't fly")
bird = Bird()
penguin = Penguin()

for animal in (bird, penguin):
    animal.fly()
