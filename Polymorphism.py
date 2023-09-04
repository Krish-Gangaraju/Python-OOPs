class Test:
    var1 = 100
    var2 = 200

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

#hasattr just sees if the 2nd parameter is in the class in the 1st parameter
print(hasattr(Test, 'method1')) #present
print(hasattr(Test, 'method2')) #present
print(hasattr(Test, 'method4')) #not present
print()
print(hasattr(Test, 'var1')) #present
print(hasattr(Test, 'var2')) #present
print(hasattr(Test, 'var3')) #not present

#So now
Test_obj = Test()
#print(Test_obj.method4) #Here you get 'Attribute Error' cos the Attribute Method4 isn't in Test

try:
    Test_obj.method4() #This will give an Attribute Error
except AttributeError:
    print("\nException! The attribute is not in Test")
print("# ---------------------------------------- #")


# ---------------------------------------- #


class Duck:
    def quack(self):
        print("I am Duck and I Quack")

class Goose:
    def quack(self):
        print("I am Goose and I Quack")

class ItQuacks:
    def __init__(self, animal):
        if hasattr(animal, 'quack'):
            animal.quack()
        else:
            animal.bark()

duck_obj = Duck()
goose_obj = Goose()

ItQuacks(duck_obj)  # when this happens ID of animal and duck_obj have to be the same obviously

class Dog:
    def bark(self):
        print("I bark")

dog_obj = Dog()
ItQuacks(dog_obj)   # Attribute Error because class Dog has no attribute quack
print("# ---------------------------------------- #")


# ---------------------------------------- #


class BookX:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


class BookY:
    def __init__(self, pages):
        self.pages = pages


bookX_obj = BookX(17)
bookY_obj = BookY(40)
print(bookX_obj + bookY_obj)
print(bookX_obj.__add__(bookY_obj))
print("# ---------------------------------------- #")


# ---------------------------------------- #


class Novel:
    """ This class is about Novels """
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        if self.pages > other.pages:
            return True
        else:
            return False

    def Doctype_test(self):
        """This method is a test for Docstrings"""
        pass

class Story:
    def __init__(self, pages):
        self.pages = pages

help(Novel)
novel_obj = Novel(350)
story_obj = Story(174)
print(novel_obj > story_obj)
print("# ---------------------------------------- #")


# ---------------------------------------- #


str1 = "zood"
str2 = "morning"
print(str1 > str2)      # ASCII values character by character
