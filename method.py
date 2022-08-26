a={"first":"1", 
"second": "2", 
"third": "3", 
"four": "4", 
"five":"5", 
"six":"6",
"seven":"7"}

print(a)

print(len(a))

print(type(a))

x=a.get("second")
print(x)

b=a.copy()
print(b)

b=a.popitem()
print(b)

a.update({"seven":"8"})
print(a)

b=a.pop("six")
print(b)

a.clear( )
print(a)

del a["four"]
print(a)

b=a.items()
print(b)

b=a.keys()
print(b)


b=a.values()
print(b)

print(min(a))

print(max(a))

a= {'name': 'Phill', 'age': 22}
x = a.setdefault('mother',"9")
# print(x)
print(a)


keys = {'Mumbai','Bangalore','Chicago','New York'}
value = 'city'
dictionary = dict.fromkeys(keys, value)
print(dictionary)


a=[1,5,6,8]
b=["w","t","u","g"]
c={}
for i in range(len(a)):
    c.update({a[i]:b[i]})
print(c)


a={"ankita":9,"5":7,"chitra":9}
c=[]
b=[]
for k,v in a.items():
    c.append(k)
    b.append(v)
print(c)
print(b)

c=[]
d=[]
for i in a:
    c.append(a[i])
    d.append(i)
print(c,d)



thisdict={"brand":"ford","model":"mustang","year":1945,"year":2020}
if "year" in thisdict:
    print("uuu")
else:
    print("nn")



a={"brand":"ford","model":"mustang","year":1945,"year":2020}
del a["year"]
print(a)

b=a.pop("year")
print(b)

b=a.values()
print(b)
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


Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
Third_value = Dictionary1.setdefault('d',"apple")
print("Third_value:", Third_value)
print(Dictionary1)



