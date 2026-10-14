'''def abcd():
    print("FF")

abcd()  
abcd()    
abcd()    
abcd()      

def addnum(a,b):
    print("sum is",a+b)
addnum(20,10) 
addnum(30.9,40.8)  

def addnum(a,b): 
    print(f"sum is {a+b:.2f}")
addnum(20,10) 
addnum(30.9,40.8) 

def sum(a,b):
    c=a+b
    return c
x = sum(1,2)
print("sum of two numbers is :",x)

def m1 ():
    print("this function is returning nothing")
    #function calling
m1()
x=m1()
print(x)

def m1(a,b):
 c = a+b
 d = a-b
 return c, d 
#calling function 
x,y = m1(10,5)
print("sum of a and b :",x)
print("substraction of a and b:",y)

def m1():
    print("first function information")
def m2():
    print("second function information")
    m1()
m2() 

def add():
    print("we assigned function to variable")
    # assign function to variable
    sum = add
    #calling function
    sum()

def message(text):
    print(text)
    
def printmessage (x) :
    x("HELLO WORLD")
printmessage(message)'''       