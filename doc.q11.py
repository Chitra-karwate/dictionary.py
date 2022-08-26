"11"
a = {'a': 4, 'b': 2, 'c':6,'d':8}
b = {'e': 3, 'f': 6, 'g':9,'h':7}
for i in b:
    a.update(b)
print(a)

"13"
a = {"a": 4, "b": 2, "c":9,"d":8}
s=0
for i in a:
    s=s+a[i]
print(s)
"14"
m=1
for i in a:
    m=m*a[i]
print(m)

"15"
for i in a:
    print(a[i])

"18"
max=0
for i in a:
    if a[i]>max:
        max=a[i]
print(max)

min=0
for i in a:
    if a[i]<5:
        min=a[i]
print(min)


# "16"
# fruits = ['mango', 'pear', 'apple','papaya']
# price = [90, 78, 110, 60]

# fruits_price = zip(fruits, price)
# b = {}
# for x, y in fruits_price:
#     if x in b:
#         pass 
#     else:
#         b[x] = y
# print(b)



# a = {1:2 ,2:1 ,4:3 ,3:4 ,6:5 ,5:6 }
# print(sorted(a.keys()))
# print(sorted(a.items()))

# a = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
# for key, value in a.items():
#     print(key,value)
