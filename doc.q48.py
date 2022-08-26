a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b={}
for k,v in a.items():
    for v in a.values():
        b[v]=len(v)
print(b)


a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
b={}
for k,v in a.items():
    for v in a.values():
        b[v]=len(v)
print(b)

