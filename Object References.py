# all variables are Object References
# all values assigned to variables are actually Objects

x = 100
y = x
print()
print (type(x))         # when declaring x automatically gets stored in internal class 'int'
print (id(x), id(y))    # same ID cos they are referencing same object

x = 200
print(id(y), "-", y)    # ID changes cos it is now referencing a different object
print("# ---------------------------------------- #")
print()


# ---------------------------------------- #


list1 = [1, 2, 3, 4, 5]
# list2 = list1           # creating a backup list of the original [copies obj reference to another]
list2 = list1.copy()    # previous method didn't work so we use the copy command [creates new obj/reference]

list1[0] = 100
print(list1, "-", list2)     # both lists change which defeats the purpose of a backup
print(id(list1), "-", id(list2))    # the copy creates a new object so IDs are different
print("# ---------------------------------------- #")
print()


# ---------------------------------------- #


def addition(num1, num2):       # what a fn does is add an obj ref to the object of the obj ref you passed into the fn
    print ("num1 ID:", id(num1), "-", "num2 ID:", id(num2))
    return num1 + num2

num_1 = int(input("Enter x: "))
num_2 = int(input("Enter y: "))

print ("x ID:", id(x), "-", "y ID:", id(y))  # IDx=ID num_1 and IDy=ID num_2
print("# ---------------------------------------- #")
print()


# ---------------------------------------- #


class Test:
    pass
obj = Test()

if isinstance(obj, Test):       # does object 'obj' belong to class 'Test'
    print ("Belongs")
else:
    print ("Doesn't belong")

print("# ---------------------------------------- #")
print()


# ---------------------------------------- #


def add(a, b):
    c = a*b
    d = a+b

    return c, d


result = add(5, 7)                  # returns in a form of list[tuple in specific]
result1, result2 = add(5, 7)        # returns in a form of 2 obj references
print(result, result1, result2)
print("# ---------------------------------------- #")
print()


# ---------------------------------------- #


class MyList(list):                 # creating your own function for list (hand write fn)
    def repeat(self, my_list, n):         # x=list, n=number of times to repeat
        list_repeat = my_list * n
        return list_repeat

list1 = MyList()
list1 = list1.repeat([1, 2, 3], 5)
print(list1)
print("# ---------------------------------------- #")
