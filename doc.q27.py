student= [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]

n = 0
for i in student:
    if i['id']:
        n=n+i['id']
print(n)
