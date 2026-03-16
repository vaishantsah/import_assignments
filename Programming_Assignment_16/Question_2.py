import math

class RadiantoDegree:
    def __init__(self, radian:int):
        self.radian=radian
        
    def convert(self)->float:
        degrees=(self.radian*180)/math.pi
        return round(degrees,1)
    
if __name__=="__main__":
    radian=float(input("Enter a number :"))
    convertor=RadiantoDegree(radian=radian)
    print(convertor.convert())