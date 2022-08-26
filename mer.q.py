dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic2:
    if i in dic1:
        dic2[i]=dic2[i]+dic1[i]
        dic1.update(dic2)
        dic1.update(dic3)
print(dic1)

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
b={}
for key in list1:
    for value in list2:
        b[key]=value
        list2.remove(value)
        break
print(b)

my_dict = {
'data1':100,
'data2': -54,
'data3': 247
}
sum=0
for i in my_dict:
    sum=sum+my_dict[i]
print(sum)

Dic= {
1:'NAVGURUKUL',
2: 'IN',  
3:{
'A' : 'WELCOME',
'B' : 'To',
'C' : 'DHARAMSALA'
}
}
Dic[3].pop("A")
print(Dic)


dict1={
"ball":"red",
"bat":4,
"wickets":8,
"ball":"green",
"bat":3
}
b={}
for i in dict:
    if dict[i] not in b:
        b.update(dict)
print(b)
dict = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}

temp = []
res = dict()
for key, val in dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)



seen = []

for k,val in dict1.items():
    if val not in seen:
        del dict1[k]
    else:
        seen.append(val)
for x in dict1.iteritems():
    print (x)

seen = []

for k,val in dict1.items():
    if val in seen:
        del dict1[k]
    else:
        seen.append(val)



for k,val in dict1.items():
    if val in seen:
        del dict1[k]
    else:
        seen.append(val)


for x in dict1.items():
    print (x)


print(seen)
dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for x in dict1:
    for y in range(len(dict1[x])):
        c=c+1
print(c)

n=int(input("enter the number"))
b={}
for i in range(n):
    a=input("enter the name")
    c=int(input("enter the marks"))
    b.update({a:c})
print(b)


a="MISSISSIPPI"
b={}
# c=0
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]=b[i]+1
print(b)


a={}
for i in range(1,16):
    a[i]=i*i
    i=i+1
print(a)


a=[{"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
b=[]
for i in a:
    for j in i:
        if i[j] not in b:
             b.append(i[j]) 
print(b)


dic={1:0,3:2,4:3,2:4}
l=[]
for i in dic:
    l.append(i)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]<l[j+1]:
            tem=l[j]
            l[j]=l[j+1]
            l[j+1]=tem
# print(l)
d={}
for i in range(len(l)):
    for j in dic:
        if l[i]==j:
            d.update({j:dic[j]})
print(d)



a={"bijender":45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in a:
    for j in a:
        # print(j)
        if a[i]<a[j]:
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
print(a)

my_dict = {
'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':50

}

max=0
max1=0
max2=0
for i in my_dict:
    if my_dict [i]>max:
        max=my_dict[i]
for i in my_dict:
    if my_dict[i]>max1 and max!=my_dict[i]:
        max1=my_dict[i]
for i in my_dict:
    if my_dict[i]>max2 and max1!=my_dict[i] and max!=my_dict[i]:
        max2=my_dict[i]
print(max,max1,max2)


dict1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}

temp = []
res = dict()
for key, val in dict1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)