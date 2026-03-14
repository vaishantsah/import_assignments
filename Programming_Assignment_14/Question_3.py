# Define a class Person and its two child classes: Male and Female.
# All classes have a method `getGender` which prints the gender.

class Person:
    def __init__(self, name=None):
        self.name = name

    def getGender(self):
        raise NotImplementedError("Subclasses must implement this method")


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


if __name__ == "__main__":
    p=Person("vaishant")
    m = Male("a")
    f = Female("b")
    m.getGender()
    f.getGender()