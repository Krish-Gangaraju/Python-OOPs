# Bubble Sorting
print("# ---------------------------------------- #")
nums = [10, 8, 4, 2, 1]
length = len(nums)

for x in range (length-1):
    for y in range (length-1-x):
        if nums[y] > nums[y+1]:
            nums[y+1], nums[y] = nums[y], nums[y+1]
    print(nums)

print(nums)
print("# ---------------------------------------- #")


# ---------------------------------------- #


decimal = 1000
flag = False
Dec_to_Bin = ""

while flag == False:
    Dec_to_Bin += str(decimal % 2)
    decimal = decimal // 2
    if decimal == 0:
        flag = True
Dec_to_Bin = Dec_to_Bin[::-1]
print ("Decimal to Binary -", Dec_to_Bin)
print("# ---------------------------------------- #")


# ---------------------------------------- #


binary = '1111101000'
length = len(binary)-1
Bin_to_Dec = 0

for i in range (length, -1, -1):
    temp = int(binary[length-i]) * (2**i)
    Bin_to_Dec += temp

print("Binary to Decimal -", Bin_to_Dec)
print("# ---------------------------------------- #")


# ---------------------------------------- #


# Selection Sorting
selects = [10, 8, 4, 2, 1]
length1 = len(selects)
print(selects)

for x in range(length1):
    small = selects[x]
    ind = x
    for y in range(x+1, length1):
        if small > selects[y]:
            small = selects[y]
            ind = y

    selects[x], selects[ind] = selects[ind], selects[x]
    print(selects)

print("# ---------------------------------------- #")


# ---------------------------------------- #


# Insertion Sorting
insertion = [10, 8, 6, 3, 2, 1]
print(insertion)

for i in range (1, len(insertion)):
    key = insertion[i]
    count = i-1

    while count >= 0 and key < insertion[count]:
        insertion[count], insertion[count+1] = insertion[count+1], insertion[count]
        count -= 1
    insertion[count+1] = key
print(insertion)
print("# ---------------------------------------- #")


# ---------------------------------------- #


