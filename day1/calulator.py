'''Calculator'''
def cal(num1,num2):
    op=input(("Enter the operation-sum,diff,mul,div,mod "))
    if op=='sum':
        print(num1+num2)
    elif op=='diff':
        print(num1-num2) if num1>num2 else print(num2-num1)
    elif op=='mul':
        print(num1*num2)
    elif op=='div':
        print(num1/num2) if num1>num2 else print(num2/num1)
    elif op=='mod':
        print(num1%num2)
ch='y'
while(ch=='y'):
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    cal(num1,num2)
    ch=input("Do you want to continue y/n?")
    
