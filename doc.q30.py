a= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
b={}
for i in a:
    c=""
    for j in range(len(i)):
        # print(j)
        if i[j]!=" ":
            c=c+i[j]
    b[c]=a[i]
print(b)

