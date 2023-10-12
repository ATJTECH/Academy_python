#match using regular expression

import re

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin.
Tesla's revenue is 40 billion.
Tesla's CFO number (999)-333-7777.'''

'''pattern="\d{10}"

print(re.findall(pattern,text))
#['9991116666']'''

#or
'''pattern=re.compile("\d{10}")
print(pattern.match(text))-->
#None
match to comp with first word in passage'''

