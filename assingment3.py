def takeInput():
    A = int(input ("initial number: "))
    B = int(input ("second number: "))
    operator = (input ("Enter operator (+,-,*,/): "))
    displayResult(A,B,operator)

def displayResult(A,B,operator):

    if operator=="+":
        result=A+B
        print (A,"+",B,"=",result)

    elif operator=="-":
        result=A-B
        print (A,"-",B,"=",result)

    elif operator=="*":
        result=A*B
        print (A,"*",B,"=",result)

    elif operator=="/":
        result=A/B
        print (A,"/",B,"=",result)
takeInput()