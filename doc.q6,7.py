
a={0:10,1:20}
print(a)
a.update({2:30})
print(a)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for i in dic2:
    dic1.update(dic2)
    dic1.update(dic3)
print(dic1)

b={}
n=int(input("enter the number"))
for i in range(n):
    num=int(input("enter the number"))
    b.update({n:n*num})
print(b)


a={1:{1:3,3:4}}
b=a[1][3]
print(b)

n1=int(input("enter the number:-"))
b={}
for i in range(1,n1+1):
    if i%2==0:
        b.update({i:"false"})
    else:
        b.update({i:"true"})
print(b)


a={1:"one",2:"two",3:"three",4:{5:"five",6:"six"}}
for i in a:
    if type(a[i])==dict:
        print(a[i].values())


import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
out_file = open("myfile.json", "w")
  
json.dump(dict1, out_file, indent = 6)
  
out_file.close()