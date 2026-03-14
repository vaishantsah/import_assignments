# Write a Python Program to Transpose a Matrix?
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

result =[[0,0,0],
         [0,0,0],
         [0,0,0]]

def transpose_matrix(a):
    for i in range(0,len(a)):
        for j in range(0,len(a[1])):
            result[j][i]=a[i][j]
    return result

if __name__ == "__main__":
    result=transpose_matrix(a)
    print("Transposing the following matrix below")
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(f"{result[i][j]}", end=" ")
        print()
