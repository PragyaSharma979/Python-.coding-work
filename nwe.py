'''#function can be store in variable
def add(a,b):
    return a+b  
def sub(a,b):
    return a-b
def calculate (func ,a,b):
    return func(a,b)   
print(calculate(add,10,20))
print(calculate(sub,10,20)) 


def outer_function ():
    [print("This is outer function")]
    def inner_function():
       print("This is inner function")
       inner_function()
outer_function()   


def outer_function ():
    [print("This is outer function")]
    def inner_function():
       print("This is inner function")
       return inner_function
func1=outer_function
func1()   

#keyword argument
def details(name,age):
    print("name: ",name)
    print("age: ",age)

details("amit",25)#passing as positional arguments
details(age=25,name="yogesh")#passing as keyword arguments

#default arguments
def details(name,age=18):
    print("name:",name)
    print("age:",age)
details("Amit")#passing only name,age will take default  value  

#variable length arguments
def add(x,y):
    pass

print(add(10,20))

def add(x,*y):
    print(type(y))
    sum=0
    for i in y:
        sum=sum+1
        return sum+x
print(add(10,20))
print(add(10,20,30,)) 
print(add(10,20,30,40,)) 
print(add(10,20,30,40,50))   


#keyword variable length arguments
def details(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,":",value)
details(name="sagar",age=22,city="panipat")
details(a=10,b=20,c=30)
details(id=101,name="pragya",age=18)'''