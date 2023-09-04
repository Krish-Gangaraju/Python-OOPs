class Grandparent:                      # without constructors
    def grandMethod(self):
        print ("I am a method in Grandparent class")

class Parent(Grandparent):
    def parentMethod(self):
        print ("I am a method in Parent class")


class Child(Parent):        # attaching to Parent class to share/inherit things
    def childMethod(self):
        print ("I am a method in Child class")


obj_child = Child()         # the object has the methods in 'Grandparent', 'Parent' and 'Child'
obj_parent = Parent()       # the object has both the methods in 'Grandparent', 'Parent'
obj_grand = Grandparent()   # the object has only the methods in 'Grandparent'


# ---------------------------------------- #


class Father:                           # without constructors
    def eyeColor(self):
        print ("Take my Eye Color")

class Mother:
    def skinColor(self):
        print ("Take my Skin Color")

class Child(Father, Mother):
    pass

child1 = Child()             # the object has the methods of both classes [2 classes]
child1.eyeColor()
child1.skinColor()
print()

# ---------------------------------------- #


class Father:
    def Method1(self):
        print ("Father's method")

class Child(Father):
    def Method1(self):
        print ("Child's method")

child2 = Child()
child2.Method1()           # Method1 is overwritten and if printed you will see "Child's method"
print()

# ---------------------------------------- #


class Father:
    def Method2(self):
        print("Father's method")


class Child(Father):
    def Method2(self):
        print("Child's method")

    def call_FatherMethod(self):
        super().Method2()       # this ensures if Method2 is called it will be from the direct parent

child3 = Child()
child3.call_FatherMethod()
child3.Method2()
print()


# ---------------------------------------- #


class Father:                       # with constructors
    def __init__(self):
        print ("Father's constructor")


class Child(Father):
    def __init__(self):
        super().__init__()
        print ("Child's constructor")

    def call_FatherInit(self):
        #super().__init__()      # this ensures if init is called it will be from the direct parent
        pass                    # but whats the point of initializing like this (basically a method)

child4 = Child()
child4.call_FatherInit()
print()


# ---------------------------------------- #


class String_Addon (str):
    def reverse (self, message):
        rev = ''
        for i in range (len(message)-1, -1,  -1):
            rev += str(message[i])
        return rev

test = String_Addon()
print(test.reverse("hello"))
