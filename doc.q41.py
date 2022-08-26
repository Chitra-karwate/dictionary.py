a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
66)}
b={}
for k,s in a.items():
    print(s)
    if s[0]>=6.0 and s[1]>=70:
        b.update({k:s})
print(b)

