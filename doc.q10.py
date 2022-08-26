n=int(input("enter the number"))
b={}
for i in range(1,n+1):
    b.update({i:i*i})
print(b)
