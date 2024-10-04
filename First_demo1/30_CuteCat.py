class CuteCat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am a {self.age} years {self.color} cat")


cat1 = CuteCat("Bob", "red", 2)
cat1.speak()
