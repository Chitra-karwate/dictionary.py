a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
cp={}
for d in a:
    if d['item'] not in cp:
        cp[d['item']]=d['amount']
print(cp)

s=0
for i in a:
    if i["amount"]:
        s=s+i["amount"]
print(s)



a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
c={}
for i in a:
    if i["item"] not in c:
        c[i["item"]]=i["amount"]
    else:
        c[i["item"]]=c[i["item"]]+i["amount"]
print(c)