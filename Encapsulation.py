class Math:
    def add(self, a, b):
        c = a+b
        return c

    def sub(self, a, b):
        c = a-b
        return c

    def multiply(self, a, b):
        c = a+b
        return c

    def divide(self, a, b):
        c = a/b
        return c


obj = Math()
result = obj.add(5, 7)


# ---------------------------------------- #


class Rectangle:
    def __init__(self, length, width):
        self.a = length
        self.b = width

    def area(self):
        c = self.a * self.b
        return c

    def perimeter(self):
        c = 2*self.a + 2*self.b
        return c


obj_rect = Rectangle(5, 7)
rect_area = obj_rect.area()
rect_perimeter = obj_rect.perimeter()


# ---------------------------------------- #


class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        vol = self.length * self.width * self.height
        return vol

    def surface(self):
        surface_area = 2*(self.length * self.width) + 2*(self.length * self.height) + 2*(self.width * self.height)
        return surface_area


obj_cube = Cuboid(5, 5, 5)
cube_volume = obj_cube.volume()
cube_area = obj_cube.surface()


# ---------------------------------------- #


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference

    def area(self):
        area = 3.14 * self.radius * self.radius
        return area


obj_circle = Circle(1)
circle_circumference = obj_circle.circumference()
circle_area = obj_circle.area()


# ---------------------------------------- #


class Test:
    def __init__(self, x):
        self.x = x          # this is an 'instance' variable (each x has its own y)

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x


obj_test1 = Test(100)
obj_test2 = Test(400)
# print(obj_test1.getX())


# ---------------------------------------- #


class VariableTypes:
    def __init__(self):      # all variables in the constructor is an 'instance
        self.x = 0           # this is an 'instance' variable (each x has its own y)

    y = 98                   # this is a 'class' variable (it affects the entire class)
    a = 79                   # doesn't belong to an individual method or object (belongs to entire class)

# when you have self inside - the method belongs to the object you're using
# when you have cls inside - the method or whatever belongs to the entire class
    @classmethod
    def modifyY(cls):
        cls.y += 1

    @classmethod            # this is called a decorator
    def getY(cls):
        return cls.y


obj1 = VariableTypes()
obj2 = VariableTypes()

obj1.modifyY()      # when modify is called increment happens
print(obj1.getY(), "- increment by 1 here cos you used modifyY[before getting Y]")
print(obj2.getY(), "- because Y was incremented in prev line Y is now 99")

obj2.modifyY()      # when modify is called increment happens
print(obj1.getY(), "- incremented again cos modifyY used again[when getY was called]")
print(obj2.getY(), "- because Y was incremented in prev line Y is now 100")

obj1.modifyY()      # when modify is called increment happens [for both obj1 and obj2]
print(obj1.getY(), "- incremented again")

print()
print(VariableTypes.a)          # Here I just called the class
print(obj1.a)                   # Here I needed to get the object/instance and then get a


# ---------------------------------------- #


class Test:
    def add(self, a, b):          # Methods like this is only created when object is created
        pass                      # This method is glued to/dependent on the object creation

    @staticmethod
    def product(a, b):           # Methods like this are created at time of class creation
        c = a*b                  # No self required because it isn't dependant on the object
        return c


print("\n", Test.product(10, 20))

# ---------------------------------------- #
