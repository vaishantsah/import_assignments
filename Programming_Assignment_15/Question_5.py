class Shape:
    def area(self)->int:
        return 0
        
class Square(Shape):
    def __init__(self, length:int):
        self.length=length
    
    def area(self):
        return self.length**2
        
if __name__ == "__main__":
    length = int(input("Enter the length of the square: "))
    square = Square(length)
    print(f"The area of the square is: {square.area()}")