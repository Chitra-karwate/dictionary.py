
a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]


for i in a:
    for v in i:
        # print(i)
        i[v]=int(i[v])
print(a)



for dicts in a:
    for v in dicts:
        dicts[v] = float(dicts[v])
print (a)


