'''to find the maximum element in a list of numbers

list=[20,100,30,40]
maximum=max(list)
print("Max is",maximum)'''

def maxi(l):
    max=0
    for i in l:
        if i>max:
            max=i
    return max     

def sum(l):
    s=0
    for i in l:
        s=s+i
    return s

def avger(l,sum1):
    av=0
    ln=len(l)
    av=sum1/ln
    return av
    


        
list=[20,100,30,40]
maxi1=maxi(list)
sum1=sum(list)
print("Max is",maxi1)
print("Sum is",sum1)
print("Average is",avger(list,sum1))

#sum,avg,per

