def Display(string_text):
    def message():      # this 'inside function' cannot be called alone/by itself/outside
        return "Hello "
    result = message() + string_text
    return result

print(Display("World"))     # simple logic - prints 'Hello World'
print("# ---------------------------------------- #")


# ---------------------------------------- #


def average_marks(a, b, c):
    def total_marks():
        total = a + b + c
        return total

    answer = total_marks() / 3
    return answer

print("Average Marks is", average_marks(5, 5, 5))
print("# ---------------------------------------- #")


# ---------------------------------------- #


def outside(string):
    def inside():
        print(string, "World")

    return inside       # fn not called here because no (), only returning the object reference

x = outside("test")
x()         # function is called here
print("# ---------------------------------------- #")


# ---------------------------------------- #


def transmit(message):
    def DataTransmitter():
        print(message)

    return DataTransmitter

toSpace = transmit("Burn the Sun!")
toSpace()
print("# ---------------------------------------- #")


# ---------------------------------------- #


def fn1(fn2):
    def fn3():
        print("@@@@@@@@@@@@@@@")
        fn2()
        print("&&&&&&&&&&&&&&&")
    return fn3

def fn2():
    print("I am decorated")

fn_to_decorate = fn1(fn2)
fn_to_decorate()
print("# ---------------------------------------- #")


# ---------------------------------------- #


def designer(me):
    def carpenter():
        value = me()
        return value + 2
    return carpenter

def me():
    return 10

secretary = designer(me)
print(secretary())
print("# ---------------------------------------- #")


# ---------------------------------------- #


def Krish(fun):
    print ("Krish has been Called", fun, fun())
    def inner():
        value = fun()
        return value + 2
    return inner

@Krish
def num():
    return 10

print(num())
print("# ---------------------------------------- #")


# ---------------------------------------- #

