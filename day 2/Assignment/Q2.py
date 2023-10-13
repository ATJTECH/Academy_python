import re
num=input("Enter the phone number")
pattern="\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\(\d{3}\)\s-\d{3}-\d{4}"

if re.match(pattern,num):
    print("Vaid number")
else:
    print("Invalid number")
    


