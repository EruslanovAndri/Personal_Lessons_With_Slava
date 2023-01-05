# Dictionary example

# d = {}
# d['name'] = 'Andrey'
# d['age'] = 39
# d['job'] = ['sales manager']
# print(d)
# print('res = ',d['job'])
# d['job'].append('new position')
# print(d['name'])


d = {}
d['name'] = 'Andrey'
d['age'] = 39
d['job'] = ['sales manager']
key = list(d.keys())
print(key)
key.sort()
print(key)
for k in key:
    print(k,'=>',d[k])

