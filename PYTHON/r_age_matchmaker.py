print(f'{"RELATIONSHIP AGE COMPATIBILITY TEST":^200}')
print("")
print("❤️❤️❤️" * 10)
print("")
print("Discover If You And Your Partner Are Age ^COMPATIBLE^")
print("")
print("❤️❤️❤️" * 10)
print("")


gender = input("Enter Gender eg. male/female: ").lower()

def male(): #function, to calculate if the user's input is male.
    def male_calc():
       print("")
       male_1 = int(input(f'{"👨 Hi Sir, Pls Enter Your Age Here: ":>40}'))
       print("")
       female_1 = int(input(f'{" 👩 Enter her age here: ":>27}'))
       diff = male_1 - female_1
       if diff > 10:
           print("")
           print("NOT COMPATIBLE 😔 age gap of " + str(diff) + " yrs makes her too young for you." )
       elif diff < -5:
           print("")
           print("NOT COMPATIBLE 😔 age gap of " + str(diff) + " yrs makes her too old for you.")
       else:
          print("")
          print(f'{"CONGRATS 🎉🎉🎉 You Found The Perfect Match":^65}')
    return male_calc()
    
    
def female(): #function, to calculate if the user's input is female
    def female_calc():
        print("")
        female_2 = int(input(f'{"👩 Hey Ma’am, Pls Enter Your Age Here: ":>40}'))
        print("")
        male_2 = int(input(f'{"👨 Enter His Age Here: " :>25}'))
        print("")
        diff = male_2 - female_2
        if diff > 10:
            print("NOT COMPATIBLE 😔 age gap of " + str(diff) + " yrs makes him too old for you." )
            print("")
        elif diff < -5:
            print("")
            print("NOT COMPATIBLE 😔 age gap of " + str(diff) + " yrs makes him too young for you.")
        else:
            print("")
            print(f'{"CONGRATS 🎉🎉🎉 You Found The Perfect Match":^65}')
    return female_calc()       


if gender == "male":
    male()
elif gender == "female":
    female()
else:
    print("")
    print(f'{"❌INVALID INPUT❌":>40}')
    print("")
    print(f'{"ENTER A VALID ‘GENDER’ male/female":>50}')
    
#written by: Øsbørn C. Ekiøja