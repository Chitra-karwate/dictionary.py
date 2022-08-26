my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
'item5': 24}
max=0
max1=0
max2=0
for i in my_dict:
    if my_dict [i]>max:
        max=my_dict[i]
for i in my_dict:
    if my_dict[i]>max1 and max!=my_dict[i]:
        max1=my_dict[i]
for i in my_dict:
    if my_dict[i]>max2 and max1!=my_dict[i] and max!=my_dict[i]:
        max2=my_dict[i]
print(max,max1,max2)

