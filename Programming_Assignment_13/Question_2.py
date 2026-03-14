# Generate an array of X,Y size with the values of each equals to the ith and jth position in the formula
# i*j
class ArrayGenerator:
    def generate_array(X:int,Y:int)->list:
        array = []
        for i in range(X):
            row=[]
            for j in range(Y):
                row.append(i*j)
            array.append(row)
        return array

if __name__ == "__main__":
    X = 4
    Y = 5
    result = ArrayGenerator.generate_array(X,Y)
    for row in result:
        print(f"{row}",end="")