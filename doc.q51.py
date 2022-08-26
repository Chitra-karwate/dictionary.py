dict={'V': [1, 4, 6,10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

c=[]
a=[]
for i in dict.values():
    for j in i:
        a.append(j)
        k=0
        b=[]
        while k<len(a):
            if a[k]%2==0:
                b.append(a[k])
            k=k+1
print(b)

m={}
for i in dict:
    b=[]
    for j in dict[i]:
        if j%2==0:
            b.append(j)
            m.update({i:b})
print(m)

b={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

m={}
for i in b:
    a=[]
    for j in b[i]:
        if j%2!=0:
            a.append(j)
    # print(a)
            m.update({i:a})
print(m)