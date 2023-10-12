'''reg_ex-->regular expression
to find a particular sentence from a para using a pattern'''

Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion.
Tesla's CFO number (999)-333-7777.

'''\d-metacharacter-character set ie [0-9]
Elon-literal-simple set; does not have a special meanig'''

'''file\d.txt-->file1.txt
            file2.txt
            
[A-Z-a-z]ile[0-9].txt-->
SELECTED
file1.txt
file2.txt
file3.txt
file4.txt

dile1.txt
while4.txt
sile5.txt


[A-Z-a-z]ile[0-9].[t,c]\w\w-->
SELECTED
file1.csv'''

\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}-->9991116666,999-333-7777,(999)-333-7777



GROUPING
(file).txt
(file\d).txt
\d*-->0 or more

file\d*.txt-->
file.txt
file1.txt
file2.txt
file3.txt

