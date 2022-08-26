dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

for k,v in dict1.items():
    if "key1" in dict1:
        print("present in dict")
    else:
        print("not in present")


for k,v in dict1.items():
    for k2,v2 in dict2.items():
        if k==k2:
            if v==v2:
                print(1,"in dict1 and dict2" )



