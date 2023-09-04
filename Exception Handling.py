# The below should give you the basic concept
# Exception handling is good because the rest of the code will work even when there is an error and it crashes
# Look at Polymorphism code to understand the above
'''
class AgeException(Exception):      # Inheritance makes this class have all the normal exception attributes
    pass

age = -10

try:                            # use try if you're doubtful if the code will work
    if age < 0:
        raise AgeException      # If this is the case flag it by calling this error

except ZeroDivisionError:
    print ("Don't divide by 0")
except AgeException:            # my own Exception
    print ("Age cant be negative")
except:                         # if any error is there it will print this one
    print ("Some error happened")
'''


# ---------------------------------------- #


'''
class MarksException(Exception):
    def __init__(self, message):
        self.message = message
        print("I am constructor of MarksException")


marks = int(input("Enter marks: "))
try:
    if marks > 100:
        raise MarksException("Marks can't be more than 100")     
        # raise creates an object of MarksException, that's why constructor is called

except MarksException as obj:
    print(obj.message)
    # print ("You got more marks than what test was out of??")
except:
    print("A problem occurred")
'''


# ---------------------------------------- #

''''
class MyException(Exception):
    pass

try:
    raise MyException       # raised for no reason

except MyException:
    print("MyException raised")
finally:                    # reaches finally always
    print("I am now in finally")
'''


# ---------------------------------------- #


class TuesError(ZeroDivisionError):
    pass

try:
    raise TuesError

except ZeroDivisionError:
    print("Zero Division Error")
except TuesError:
    print("Tuesday Error")
except:
    print("Some error")


# ---------------------------------------- #

#AssertionError