def inequality_expression(expression:str)->bool:
    expression = expression.replace(" ", "")
    try:
        return eval(expression)
    except Exception as e:
        return str(e)

if __name__=="__main__":
    expression=input("Enter an inequality equation: ")
    print(inequality_expression(expression))