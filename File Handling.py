# r = doesn't create file, only able to read its contents
# w = creates file if doesn't exist, can write stuff but will overwrite
# a = creates file if doesn't exist, can write but will not overwrite

# r+ = can read and write but will not create any file and will overwrite
# w+ = can read and write, creates file if not existing, but overwrites [use file.seek(0)]
# a+ = can read and write, creates file if not existing, will not overwrite on existing file

file = open("FileHandling.txt", "w")
file.write("Good morning")
file.close()


file = open("FileHandling.txt", "a")
file.write("\nHow are you")
file.close()

file = open("FileHandling.txt", "r")
string = file.read()
print(string)
file.close()

file = open("FileHandling.txt", "w+")
file.write("Test")
file.seek(0)        # make the cursor go to index zero
print(file.read())  # reads from where the cursor is to the end
file.close()

