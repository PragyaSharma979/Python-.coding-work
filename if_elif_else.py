'''x = int(input("Enter a number"))
if x<0:
    print("The number is negative number")
else:
    print("The number is positive number")  '''

'''user_name ='Rahul'
x = input("Entera number")
if user_name==x:
     print("The name is valid ")
else:
     print("The name is invalid") '''

'''x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
if x>y:
    print("Biggest Number is:")
    print("biggest second number:")'''

'''x=int(input("Enter First Number:"))
y=int(input("Enter Second Number"))
z=int(input("Enter Third Number"))
if x>y and x>z:
    print("Biggest first number")
else:
    print("Biggest second number")'''

'''a = 10
b = 20
min  = a if a<b else b
print(min)'''

'''x = 1 
while x<=5:
 print(x)
x+=1
print("end")'''

'''x = 10
while(x>=10) and (x<=20):
  print(x)
  x+=2
print("End")'''

'''x = [10,20,30,"python"]
for i in x:
    print(i)'''

'''x = "python"
for ch in x:
    print(ch)'''

'''item_costs = [10,20,30]
sum=0
for x in item_costs:
  sum=sum+x
print(sum)'''

'''x = (input("enter a input:"))
sum = 0
for y in x:
    sum=sum+int(y) 
print(sum)'''

'''for x in range(1,8,2):
    for y in range(x):
        print("*",end=" ")
    print()  

for x in range(5,0,-1):
    for y in range (x):
        if y%2==0:
          print("#",end=" ")
    else:
            print("*",end=" ") 
    print()   '''

'''group = [1,2,3,4]
search = int(input("Enter the element search:"))
for element in group:
    if search == element:
        print("element found in groups")
        break'''

'''for x in range(1,21):
     if x%5!=0:
          continue
     print(x)'''


'''for x in range(1,21):
     if x%5==0:
          continue
     print(x)'''

'''for x in range(1,21):
     if x%5==0:
          pass
     print(x)'''

'''x = 1
if x<=3:
    print("Hi")
    x+=1
else:
    print("hello") '''
'''x = 1
while x<=3:
    print("Hi")
    x+=1
else:
    print("hello")  '''


'''x = 1
while x<=3:
    print("Hi")
    x+=1
else:
    print("hello")

for x in [1,2,3,4]: 
     print("hi")
else:
    print("Hello")        '''

'''cart=[10,20,500,700,50,60]  
for item in cart:
    if item>=500:
        continue
    print("Item:", item) '''

'''group = [1,2,3,4]
search=int(input("Enter the element in search"))
for element in group:
    if search == element:
        print("element found in group")
        break
    else:
        print("element not found") '''


'''n = [1,2,3]
n.remove(1)
print(n)

n = [1,2,3]
n.remove(10)
print(n)'''

'''n = [1,2,3,4,5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)'''

'''n =[1,2,3,4, 'two']
print(n)
n.reverse()
print(n)


n =[1,4,5,2,3]
n.sort()
print(n)
s = [ 'suresh , ramesh , mahesh']
s.sort()
print(s)'''

'''x = [1,2,3,4,5]
y=x
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))'''

'''x = [10,20,30]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))'''

'''a = [1,2,3]
b = [4,5,6]
c= a+b
print(c)

a=[1,2,3]
b = 'bablu'
c=a+b
print(c)'''

'''a = [1,2,3]
print(a)
print(2*a)

print([1,2,3]<[2,2,3])
print([1,2,3]<[1,2,3])
print([1,2,3]<=[1,2,3])
print([1,2,3]<[1,2,4])
print([1,2,3]<[0,2,3])
print([1,2,3]==[1,2,3])'''

'''x =["abc","def","ghi"]
y= ["abc","def","ghi"]
z= ["ABC","BCD","EFG"]
a= ["abc","bcd","efg","hij"]
print(x==y)
print(y==z)
print(a==x)'''

'''abcd = lambda x,y:x**y
print(abcd(4,3))
l1 = [ 1,2,3,4,5,6,7,8]
f=filter(lambda x:x%3==0,l1)
l2=list(f)
print(l2)
f=map(lambda arun:arun%3==0,l1)
l2=list(f)
print(l2)
f=map(lambda i:i**2,l1)
l3=list(f)
print(l3)'''

'''l =[1,2,3,4,5,6,7,8]
from functools import reduce
f=reduce(lambda x,y:x if x>y else y,1)
print(f)'''

'''t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1+t2
print(t3)
print(type(t3))'''

'''t1 = (10,20,30)
t2 = t1*3
print(t2)
print(type(t2))'''

'''t1 = (10,20,30)
t2 = (t1*3)
print(t2)
print(type(t2))'''

'''t = (40,10,30,20)
t1 = sorted(t)
print(t)
print(t1)'''

'''t = (40,10,30,20)
print(min(t)) 
print(max(t)) '''

'''a = 10
b = 20
c = 30
d = 40
t= a,b,c,d
print(t)
print(type(t))'''

'''roll = 100
name = "pragya"
email = "pragya@gmai.com"
phone = "12345678"
t = roll, name, email, phone
print(t)
print(type(t))

l=[]
for x in range (3):
 roll = int(input("Enter roll"))
 name = input("enter name")
 email = input("enter email")
 phone = input("enter phone")
t = roll, name, email, phone
l.append(t)
for r,n,e,p in l:
    print("%5d %-15s %-20s %10s "% (r,n,e,p))'''

'''t =(x**2 for x in range (1,6))
print(type(t))
for x in t:
    print(x)
    print(type(x))
    print(type(t))'''

'''d={}
d[1]="arun"
d[2]="pragya"
d[1]="aashita"
print(d)'''

'''d = {1: 'Ramesh', 2: 'suresh', 3: 'mahesh'}
if 400 in d:
    print(d[400])
else:
    print("key not found")    '''

'''d ={}
n = int(input("Enter number of employees"))
i=1
while i <=n:
    name = input("enter employee name:")
    salary = input("Enter employee salary:")
    d[name]=salary
    i=i+1
for x in d:
    print("the name is :,x")'''




