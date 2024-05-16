#Defining function def bmi(weight, height):
def bmi(weight, height):
    index = weight / (height *height) 
    return index #sends the return value back

#Calling function and using return value 
patient_5 = bmi (61, 1.83) #stores return value 8
print("underweight:", patient_5 < 18.5)

#Another call
patient_7 = bmi(75, 1.74) 
print("underweight:", patient_7 < 18.5)

print("********POS SLIP********")

print(" ")

def withdrawal(balance, withdraw):
	index = balance - withdraw
	return index

balance = 20000
user_withdraw = int(input())
withdraw = user_withdraw
 
if balance < user_withdraw:
	print("Transaction Declined")
	print("***" * 3)
	print("insufficient funds")
	print("***" * 3)
else:
	print("Transaction Approved")
	

    	