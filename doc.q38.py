a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
for x,y in a.items():
    if y is not None:
        b.update({x:y})
print(b)

for x,y in a.items():
    if y in "c2":
        print("done")
    else:
        print("no")

if "c2" in a:
    print("bb")
else:
    print("nn")