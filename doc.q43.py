a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
b={}
for i,j in a:
    b.setdefault(i,[]).append(j)
print(b)

