# Строки и работа со стороками.

# Initialization 
s1 = 'Srting1'
s2 = "String2"
s3 = "String's3"
print(s1,s2,s3)
s1 = 'Srting1\n' # Перенос на новую строку
s2 = "\tString2" # Табуляция 
s3 = '\nString\'s3' # Экранирование служебных символов 
print(s1,s2,s3)
s4 = 'a\nb\tc' # a
print(s4)      # b      c

print(len(s4)) # len = 5 byte

# Отключение форматирование строки с помощью символа (r),он отменяет форматирование.
s5 = r'c\new_path_to_folder\\'
print(s5)

# Многострочные комментарии (''' TEXT '''')

s6 = '''Here we can 
        add some text
        or sql requests'''
print(s6)

# Конкатинация строк осуществляется при помощи символа (+).

print('Hi'*3) # Множественное повторение строки * = HiHiHi

s7 = 'asd'
s8 = 9 # Int нет возможности осуществить конкатинацию строк с числом, нужно привести к одному типу.
s9 = str(s8) # приведение int в string
print(s7+s9) # res = asd9

# Цикол for in для поиска вхождений в строку.

s10 = 'Hello, my name is Andrey.'
for n in s10: print(n,end='')
print()
print('H'in s10,end='')
print()
print('Andrey' in s10) # Поиск подстроки.
print(s10[0],s10[-2]) # H y

# Получение срезов от строки.
print(s10[1:7],s10[:10],s10[:-3]) # = (ello,) (Hello, my ) (Hello, my name is Andr)
print(s10[1:15:2]) # = el,m ae третий параметр указывает шаг на смещение.
print(s10[::3])
print(s10[::-1]) # переворачивает строку = .yerdnA si eman ym ,olleH

#  Переобразование типов 
s = "42"
x = 3
print(s+str(x)) # = 423 Так как число 3 преобразовали в строку и прибавили к строке 42+3=423
print(repr(s)) # = '42' выводит строку в терминал обрамленную кавычками
print(s)

s = 'a'
print(ord(s)) # 97 Порядковый номер в таблице символов 
print(chr(97)) # a -> a обратное приеобразование из числа в букву.
x = ord(s)
print(x + 3)
