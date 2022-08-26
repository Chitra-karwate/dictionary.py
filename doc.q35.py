dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for x in dict1:
    for y in range(len(dict1[x])):
        c=c+1
print(c)
