# Code for Transposing Matrix
m = [[1, 2], [4, 5]]

def transpose (matrix):
    transposed = []
    for x in range(len(matrix[0])):
        temp = []
        for y in range(len(matrix)):
            temp.append(matrix[y][x])
        transposed.append(temp)
    return transposed

print(transpose(m))
print("# ---------------------------------------- #")


# ---------------------------------------- #


# Code to Multiply Matrices
m1 = [[1, 2], [4, 5]]
m2 = [[5, 7], [9, 10]]

# 1  2        5  7
# 4  5        9  10

#23 27
#65 78
output_size = len(m1[0]) * len(m2)
product = []
print(transpose(m2))

for i in range (output_size):
    temp_list = []
    temp_sum = 0
    for j in range (len(m1[0])):
        a = m1[i][j] * m2[i][j]
        temp_sum += a
    temp_list.append(temp_sum)
print(temp_list)