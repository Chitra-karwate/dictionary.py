n=int(input("enter the number"))
b={}
for i in range(n):
    c=int(input("enter the number"))
    d=int(input("enter the number"))
    b.update({c:d})
print(b)


a={"chitra":6,"priya":8,"divya":9}
a.update({"nikki":3})
print(a)

b=a.items()
print(b)

b=a.values()
print(b)

del a["chitra"]
print(a)

b=a.keys()
print(b)

a.pop("chitra")
print(a)


b=a.get("chitra")
print(b)

a.clear()
print(a)

a.popitem()
print(a)

print(len(a))

print(type(a))

a={"chitra","neha","pooja","usha","riti"}
b=0
c=dict.fromkeys(a,b)
print(c)

x=a.setdefault("neha","komal")
print(a)

a={1:"a",2:"b"}
print(a.get(4,5))

a={"chitra":12,"age":16,"class":10,"student":{"neha":6,"place":"pune"}}

for i in a:
    if type(a[i])==dict:
        for j in a[i]:
            print(a[i][j])
 
a={"chitra":{"class":9,"nita":8},"maya":{"class":5,"meena":7}}
for key,value in a.items():
    # print(key)
    for k,v in value.items():
        print(k,":",v)





dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for i in(dic1,dic2,dic3):dic4.update(i)
print(dic4)

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


a = [{"id" : 88, "color" : 9}, 
          {"id" : 99, "color" : 5}, 
          {"id" : 20, "color" : 22}, 
          {"id" : 8, "color" : 6}]

b={}
s=0
for i in a:
    # print(i)
    for j in i:
        s=s+i[j]
print(s)






