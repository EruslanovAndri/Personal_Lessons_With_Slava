import math


x = 16

print(pow(x,2)) # Возведение в степень = 256
# Обязательно нужно импортировать библиотеку math
print(math.sqrt(x)) # Нахожение квадратного корня из числа = 4.0

x = 1 + 2.0 +3
print(type(x)) # <class 'float'>
print(x) # 6.0

# Какможновыполнитьусечениеиокруглениевещественногочисла?

num = 2.0322 * 100
print(num) # = 203.22
print(int(num)) # отсекает дробную часть = 203
print(math.trunc(num)) # отсекает дробную часть = 203
print(round(num,1)) # округляет результат до указанного кол-во цифр после запятой = 203.2
print(math.floor(num)) # округление вниз = 203

# Как можно преобразовать целое число в вещественное?

num = 15
print(type(num)) # <class 'int'>
print(float(num)) # = 15.0 float
print(type(float(num))) # <class 'float'>

a = 3 
b = a
a = 'spam'
print(a,b)
a = 3
b = a
a = a + 3
print(a,b)