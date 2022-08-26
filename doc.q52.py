a={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=""
for k,v in a.items():
    if k>max:
        max=k
print(max)
