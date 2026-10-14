'''# Take input string from user
text = input("Enter a string")

#Output operation using string slicing
print("original:",text)
print("first 3:", text[:3])
print("last 3:", text[-3:])
print("Index 2 to 7:", text[2:8])
print("Every 2nd charcter:",text[::2])
print("Reversed:", text[::-1])'''

''' s1="This a mearged batch. We will complete string today"
print(id(s1))
c=s1.count("a")
print(c)
print(id(s1))'''

'''s1="This a mearged batch. We will complete string today"
print(id(s1))
print(s1)
s1=s1.replace("today","tomorrow")
print(s1)
print(id(s1))'''

'''s1="python programming language"
n=s1.split()
print("Before splitting:",s1)
print("After splitting:",n)
print(type(n))'''

'''s1="13:32:55"
h,m,s=s1.split(":")[0],s1.split(":")[1],s1.split(":")[2]
print(h)
print(m)
print(s)'''

'''l1=["Rajesh","jai","rohit","chetan"]
s1="_".join(l1)
print(s1)'''

'''profile=["pragya","ishika","Priyanshi"]
profile="_".join(profile)
print(profile)'''

'''name="pragya"
s=input("Enter your fixed name")
if name==s. lower():
    print("ok")
else:
    print("ok")
name="sunil kumar sharma"
print(name.lower())
print(name.upper())
print(name.swapcase())
print(name.capitalize())
print(name.title())
print(name.isalnum())
print(name.isalnum())'''

'''val=input("Enter Value")
val=val if val. isalpha() else eval(val)
print(val)
print(type(val))'''

'''name="pragya"
age="16"
place="Basoma"
sub=" {n} lives in {p} and his age is {a}". format(a=age,n= name,p=place)
print(sub)'''

s1=input(" Enter the string")
sub=""
l=s1.split()
for word in 1:
  newstr=word[::2]
  sub+=newstr+" "
print(sub.strip())
