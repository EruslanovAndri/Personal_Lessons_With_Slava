# Множества и операции с ними.

x = {1,2,3}
y = {5,6,7,1}
s = set() # Так задается пустой set 
print(type(s))
print(x|y) # Объединение
print(x&y) # Пересечение
print(x-y) # Разность
print(x>{1,3}) # Надмножество 
x.add('lol') # add to the set X
print(x)
s.add(1)
print(s)

# Генератор множеств
x = {x ** 2 for x in [1,2,3,4]} # Генератор множеств
print(x) # {16, 1, 4, 9}

x = {x for x in 'spam'} # Генератор множеств
print(x) # {'a', 'p', 's', 'm'}

x = {c * 4 for c in 'spam'} 
print(x) # {'pppp', 'ssss', 'aaaa', 'mmmm'}


# Множество можно передовать в функцию list 
# и благодаря этому удалять повторяющие значения

l1 = [1,2,3,4,5,6,5,4,3,2,1]
print(l1)
print(set(l1)) # {1, 2, 3, 4, 5, 6} set
print(list(set(l1))) # [1, 2, 3, 4, 5, 6] list
l2 = list(set(l1)) 
print(l2) # [1, 2, 3, 4, 5, 6]

for i in l1:
    print(i,end=" ") # выдает элемненты
print()
for i in range(len(l1)):
    print(i,end=' ') # выдает индексы 


engineers = {'bob','sue','ann','vic'}
managers = {'tom','sue'}
print('bob' in engineers) # True
print(engineers & managers) # {'sue'}
print(engineers | managers) # {'sue', 'tom', 'vic', 'ann', 'bob'} удаляет повторения
print(engineers - managers) # {'ann', 'vic', 'bob'}
print(managers - engineers) # {'tom'}
print(engineers > managers) # False Все менеджеры являются инженерами?
print({'bob','sue'} < engineers) # True Оба сотрудника инженеры?
print((managers|engineers)>managers) # True Множество всех сотружников является надмножеством менеджеров?
print(managers ^ engineers) # {'tom', 'vic', 'ann', 'bob'} Сотрудники принадлежащие к какой-то одной группе
print((managers | engineers)- (managers ^ engineers)) # {'sue'} Пересечение!

import math
x = 16
print(pow(x,2))
print(math.sqrt(x))