import math

class HexagonArea:
    def __init__(self, side: float):
        self.side=side
    
    def area(self)->float:
        area=(3*math.sqrt(3)*self.side**2)/2
        return round(area,1)

if __name__=="__main__":
    side =float(input("Enter length :"))
    area=HexagonArea(side)
    print(area.area())