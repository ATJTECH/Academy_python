import re

text=input("Enter the email")

pattern="\w*@[^yahoo|^hotmail]\w*\.com|\w*@[^yahoo|^hotmail]\w*\.in|\w*@[^yahoo|^hotmail]\w*\.org"

#pattern="\w*@[^yahoo|^hotmail]\w*\.[com|in|org]"
if re.match(pattern,text):
    print("Vaid email")
else:
    print("Invalid email")


