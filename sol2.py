String1=input()
# first string 
String2=input()
# second string
c=0
# count intially taken as 0
S=String2[-1]
for i in String1:
    if i == S:
        c+=1
print(c)
