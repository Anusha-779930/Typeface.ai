String1=input()
String2=input()
c=0
S=String2[-1]
for i in String1:
    if i == S:
        c+=1
print(c)
