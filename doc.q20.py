d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d2:
    if i  in d1:
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)


my_dict = {}
my_other_dict = {'a': 1}

if not my_dict:
    print("dicttionary", my_dict, "is empty")
else:
    print("dicttionary", my_dict, "is NOT empty")

if not my_other_dict:
    print("dicttionary", my_other_dict, "is empty")
else:
    print("dicttionary", my_other_dict, "is NOT empty")
