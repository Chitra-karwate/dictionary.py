a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
for i in a:
    s=0
    c=0
    for j in range(len(a[i])):
        s=s+a[i][j]
        c=c+1
    print(s//c)


for i in a:
    s=0
    c=0
    for j in a[i]:
        s=s+j
        c=c+1
    print(s//c)
