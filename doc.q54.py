a={1: ['Jean Castro,'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b=[]
c={}
for k,v in a.items():
    for j in v:
        # print(j)
        c.update({k:j})
b.append(c)
print(b)



b=[]
c={}
for k, v in a.items():
    for j in v:
        c.update({k:j})
b.append(c)
print(b)