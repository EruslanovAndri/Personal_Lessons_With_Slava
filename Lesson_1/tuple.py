# Tuple unchanged form 

t = (1,1,2,3,4)
print(len(t)) # длина кортежа
t += (5,6) # добавление элементов конкатенация 
print(t)
print(t[1:4]) # срез 
print(t[0]) 
print(t.index(4)) # поиск индекса элемента 
print(t.count(1)) # подсчет одинаковых элементов