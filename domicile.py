def check_domicile(age,domicile):
    domicile=domicile.lower()

    if age>=18 and domicile=="lahore":
        print("You are eligible to vote ")
    else:
        print("You are not eligible to vote ") 


age=int(input("Enter your age : "))
domicile=input("Enter your domicile city : ")

check_domicile(age,domicile)    