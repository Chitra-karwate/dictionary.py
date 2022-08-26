a={"a":10,"b":5,"c":7,"d":3}
s=1
for i in a:
    s=s*(a[i])
print(s)

b={}
n=int(input("enter the number"))
for i in range(n):
    num=int(input("enter the number"))
    b.update({num:num*num})
print(b)

b={}
n=int(input("enter the number"))
for i in range(1,n+1):
    b.update({i:i*i})
print(b)


b={}
n=int(input("enter the number"))
for i in range(1,11):
    b.update({i:i*n})
print(b)


b={}
n=int(input("enter the number"))
for i in range(1,n+1):
    b.update({i:i*i*i})
print(b)


n=int(input("enter the number"))
i=0
b=[]
for i in range(n):
    e={}
    c=(input("enter the name"))
    d=int(input("enter the age"))
    v=int(input("enter the class"))
    e.update({"name":c})
    e.update({"age":d})
    e.update({"class":v})
    b.append(e)
print(b)

a=["chitra","saikirtee","pinki"]
i=0
c=0
while i<len(a):
    if len(a[i])>c:
        c=len(a[i])
        d=a[i]
    i=i+1
print(d)


i=-1
while i>=-10:
    print(-i)
    i=i-1


a="divya"
b="vidya"
print(a,"is a sister")

thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'a':1
}
a=thisdict.values()
thisdict["year"]=2020
print(a)

for k,v in thisdict.items():
    print(k) 
print(len(thisdict))
x = thisdict.get("model")
print(x)


print(thisdict.items())

thisdict['year']=2000
print(thisdict)


thisdict['a']=2
print(thisdict)

thisdict.update({'a':3})
print(thisdict)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
car["year"] = 2020
print(x)

dict=[{"name":"chitra","age":21},{"name":"neha","pooja":22}]
a=[]
for i in range(len(dict)):
    for x,y in dict[i].items():
        if x=="age":
            a.append(y)
print(a)


a=str(input("enter the name"))
d={}
for i in range(len(a)):
    d.update({a:i})
    print(d)

dict=[{"a":{"drt":1,"0":90},"b":{"vu":8,"vy":4}}]
p={"drt":56,"0":10}
dict["a"]=p
print(dict)


for i in dict:
    print(i)


a={"chitra":5,"pooja":9,"yy":7}
b={"bb":8,"ll":9}
s=0
for i in a:
    s=s+a[i]
print(s)