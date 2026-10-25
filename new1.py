#local variable
'''def m ():
    a=11
    print(a)
m()
output:11    


sum=10
l=[1,2,3,4,5,6,7,8,9]
print(sum(1))

def add(x,y):
    return x+y
def add (x,y,z):
    return x+y+z
def add (x,y,z,w):
    return x+y+z+w

print(add(12,56))
    

#global variable
a=11
b=12
def m():
 print("a from function m():",a)
 print("b from fuction m():",b)
def n():
  print("a from function n():",a)
  print("b from function n():",b)
m()
n()


a = 1
def m1():
    a=2
    print("a value from m1() function:",a)
def m2():
    print("a value from m2 ()function :",a)
m1()
m2()


a=1
def m1():
    global a
    a=2
print("a value from m1() function:",a)
def m2():
    print("a value from m2()function:",a)
    m1()
    m2()

a=1
def m():
    a=2
    print(a)
    print(globals()["a"])
m()


x=1
while(x<=10):
    print(x)
    x+=1 #this is true condition


x=1
while(x==11):
    print(x)
    x+=1
def printdata(x):    
    if x==11:
     return
    else:
     print(x)
     printdata(x+1)
printdata(1)


#forwarding track
def printdata(x):    
    if x==11:
       return
    else:
     printdata(x+1)
     print(x)
printdata(1)'''