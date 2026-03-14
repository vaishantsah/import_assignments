# Write a Python Program to Multiply Two Matrices?
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=[[9,8,7],
   [6,5,4,],
   [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

def multiply_matrices(a, b):
    for i in range(0,len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

if __name__ == "__main__":
    if len(a[0]) != len(b):
        print("Cannot multiply the matrices. Number of columns in A must be equal to number of rows in B.")
    else:
        result=multiply_matrices(a, b)
        print("Multiplying the following matrix below")
        for i in range(len(result)):
            for j in range(len(result[0])):
                print(f"{result[i][j]}", end=" ")
            print()