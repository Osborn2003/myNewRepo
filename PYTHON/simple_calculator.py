print("====SIMPLE CALCULATOR====")

num1 = int(input("Enter 1st Number: "))
operator = input("Enter Operator: ")
num2 = int(input("Enter 2nd Number: "))
sum = num1 + num2
difference = num1 - num2
quotient = num1 / num2
multiply =  num1 * num2

if operator ==  "+":
    print("Ans: ", sum)
    
elif operator == "-":
    print("Ans: ", difference)
    
elif operator == "*":
    print("Ans: ", multiply)
        
elif operator == "/":
    print("Ans: ", quotient)
    
else:
    print("INVALID INPUT")
    
def cOperator():
        
        print(str(num1) + str(operator) + str(num2))
        
cOperator()
    
    
