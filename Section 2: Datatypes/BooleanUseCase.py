#Prompt the user to enter their age and whether they have a valid driver’s license (Yes/No).
driver_license = input("Do you have license number (Yes/No)")
try:
    if(driver_license.upper() == "YES" or driver_license.upper() == "NO" ):
        print("We have noted down your feedback for license")
    else:
        print("Invalid license number, please enter either Yes or No")
    
except ValueError:
    print("Invalid character.")

driver_age = input("Please enter your age: ")
try:
    age = int(driver_age)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid age entered. Please enter a number.")

can_drive = False

if(driver_license.upper() == "YES"):
    license = True
else:
    license = False

if(age>= 18 and license == True):
    print("You can drive.")
    can_drive = True
elif(age < 18):
    print( "You are too young to drive.")
elif(age == 18 and license == False):
    print("You cannot drive without a license.")
print(can_drive)

drive_today = input("If you want to drive today (Yes/No)")
try:
    if(drive_today.upper() == "YES" or drive_today.upper() == "NO" ):
        print("We have noted down your feedback for driving")
    else:
        print("Invalid entry, please enter either Yes or No")
    
except ValueError:
    print("Invalid character.")

if(drive_today.upper() == "YES"):
    drive = True
else:
    drive = False

if(can_drive == True and drive == True):
    print("Great! Have a safe drive!")
else:
    print("Okay, maybe next time.")