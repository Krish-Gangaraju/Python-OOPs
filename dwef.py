import pickle

def write_binary(data):
    file = open("My Database", "wb")
    for i in data:
        pickle.dump(i, file)
    file.close()

def read_binary():
    file = open("My Database", "rb")
    students = []
    try:
        while True:
            content = pickle.load(file)
            students.append(content)
    except EOFError:
        file.close()
    return students

def search(name):   # Retrieve
    content = read_binary()
    for i in content:
        if i[0] == name:
            print(i)
            break
    else:
        print("Name not Found")

def change_marks(name, marks):   # Update
    content = read_binary()
    for i in content:
        if i[0] == name:
            i[2] = marks
    write_binary(content)

def add_student(name, grade, marks):   # Create
    content = read_binary()
    new = [name, grade, marks]
    content.append(new)
    write_binary(content)


s1 = ["Anil", "10th", 80]
s2 = ["Benj", "11th", 75]
s3 = ["Carl", "12th", 78]
obj_toDump = [s1, s2, s3]
write_binary(obj_toDump)

#add_student("Adam", "7th", 86)
print(read_binary())


