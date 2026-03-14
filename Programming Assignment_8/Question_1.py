# 1. Write a Python Program to Add Two Matrices?
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=[[9,8,7],
   [6,5,4,],
   [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(0,len(a)):
    for j in range(0,len(a[1])):
        result[i][j]=a[i][j]+b[i][j]

print("Adding the following matrix below")
print("Matrix A")
for i in range(len(a)):
    for j in range(len(a[0])):
        print(f"{a[i][j]}", end=" ")
    print()

print("\nMatrix B")
for i in range(len(b)):
    for j in range(len(b[0])):
        print(f"{b[i][j]}", end=" ")
    print()

print("\nResultant Matrix")
for i in range(len(result)):
    for j in range(len(result[0])):
        print(f"{result[i][j]}", end=" ")
    print()
