print("CHOOSE SEXUALITY")
for i in range(2):
	print("===" * 10)
	
print("Straight - 0")
print("Bi - 1")
print("Gay - 2")
print("Lesbian - 3")

Sexuality = ["Straight", "Bi", "Gay", "Lesbian"]
Sexual_Orientation = int(input())
print(Sexuality[Sexual_Orientation])
if Sexual_Orientation == 0:
	print("GOD BLESS YOU")
	print("VERY GOOD")
	print("🚫Access Denied🚫")
elif Sexual_Orientation == 1:
	print("Hmm 🧐")
	print("INTERESTING")
	print("🚫Access Denied🚫")
else:
	print("LGTV eeh " * 20)
	print("✅Access Granted✅")
	print("WELCOME TO HELL'S GATE")

name = "Name:"
name_userinput = input()
age = "Age:"
age_userinput = int(input())
location = "Location:"
location_userinput = input()

print(name, name_userinput)
print(age, age_userinput)
print(location, location_userinput)
Sexuality.append("Pandsexual")
print(Sexuality)

bot_greeting = "Hello"
bot_greeting2 = "How are you? It's nice to meet you"
print (bot_greeting, name_userinput, bot_greeting2)

def greet():
	print (name_userinput, "Why are you Gay?")
	print("oops! Padon my manners")
greet()