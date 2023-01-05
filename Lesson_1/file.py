
with open('data.txt', 'w',encoding='UTF-8') as data:
    data.write('Hello\n')
    data.write('World\n')


with open('data.txt','r',encoding='UTF-8') as data:
    f = data.read()

print(f.split())

for i in range(len(f)):
    #print(f[i].upper())
    print(f[i].replace('l','L'))