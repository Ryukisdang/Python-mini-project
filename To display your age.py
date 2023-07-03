# to display your age
def calculateAge():
    loop=False
    while loop==False:
        currentYear=int(input("Enter current year: "))
        birthDate=int(input("Enter Birthdate year: "))
        calculate=currentYear-birthDate
        displayAge=f'This is your age {calculate}'
        if currentYear>birthDate:
            loop=True
            print(displayAge)
        else:
            loop=False
            print("WANNA TRY MORE PEOPLE AGE")
calculateAge()

