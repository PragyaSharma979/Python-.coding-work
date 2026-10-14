'''s1 = "Amit"
s2 = "Anil"
if s1<s2:
     print(s1)
else:
     print(s2)

s1 = "Amit"
s2 = "Anil"
if s1>s2:
     print(s1)
else:
     print(s2)

     s1= " Amit kumar "
     print(len(s1))

     s1=" Amit Kumar "
     print(len(s1.rstrip().lstrip()))
     print(len(s1.strip()))

     name="pragya sharma"
     print(name.find("a"))
     print(name.find("a",4))
     print(name.find("z"))

     print(name.index("a"))
     print(name.index("a",4))
     print(name.index("z"))'''

'''name="sunil kumar sharma"
first=name[:5]
second=name[:6:11]
last=name[12::]
print(first)
print(second)
print(last)'''

'''name=input("pragya sharma")
first=name[:name.find(" ")]
second=name[name.find(" ")+1:name.rfind(" "):]
last=name[name.rfind(" ")+1::]
print(first)
print(second)
print(last)

#Enter email and print username & domain name seperately
email = input(" Enter email")
pos = email.find("@")
username=email[:pos]
domain =email[pos+1:]
print("username:",username)
print("Domain:",domain)'''

str1="python is a good programming language"
val=str1.count("a")
print(val)
print(str1)
print(id(str1))
str1=str1.replace("good","bad")
print(str1)
print(id(str1))




     