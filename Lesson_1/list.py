
# # def my_empty_list():
# #     my_list = []
# #     return my_list

# # def fill_my_list(my_list: list) -> list:
# #     my_list = []
# #     count = 0
# #     while count <= 5:
# #         num = int(input('--> '))
# #         my_list.append(num)
# #         count += 1
# #     return my_list

# # def find_max(my_list: list[int]) -> int:
# #     for i in range(len(my_list)):
# #         return max(my_list)
        
# # print(f'Max = ',find_max(fill_my_list(my_empty_list())))

# # def get_list_in_list():
# #     new_list = []
# #     count = 0
# #     while count < 2:
# #         for i in range(1,4):
# #             num = int(input('Num -> '))
# #             new_list.append(num)
# #             count += 1
# #     return new_list

# # print(get_list_in_list())

# a = [[11,22,33],
#     [44,55,66],
#     [12,13,14]]

# for i in a:
#     for j in i:
#         print(j,end= ' ')
#     print()

# for i in range(0,3):
#     sum = 0
#     for j in range(0,3):
#         sum += a[i][j]
#     print(f'Sum in {i} row = ',sum)

# for j in range(3):
#     sum = 0
#     for i in range(3):
#         sum += a[i][j]
#     print(f'Sum in {j} colomns = ',sum)



# # def get_empty_list():
# #     n  = int(input('Row -> '))
# #     m = int(input('Colomns -> '))
# #     my_list = []
# #     for i in range(n):
# #         my_list.append([1]*m)
# #     for i in my_list:
# #         print(i)

# # get_empty_list()


# def fill_nested_list():
#     a = []
#     row = int(input('Row -> '))
#     colomn = int(input('Colomn -> ')) 
#     for i in range(row):
#         a.append([0]*colomn)
#         print(a[i])

# fill_nested_list()

# a = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
# def f(a):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if i == j:
#                 a[i][j]=1
#             elif i <= j:
#                 a[i][j]= 0
#             else:
#                 a[i][j] = 2
#     for i in a:
#         print(i)   
        

# f(a)

# s = list(map(int,input().split()))
# print(s)

# def get_sum(s):
#     b = []
#     for i in range(len(s)):
#         res = s[i]**2
#         b.append(res)
#     print(b)

# get_sum(s)

# def find_min(s: list[int]):
#     return min(s)


# print(find_min(s))


m =[[1,2,3],
    [4,5,6],
    [7,8,9]]  
colomn2 = [row[0] for row in m]
print(colomn2) # показывает только столбец из матрицы

m =[[1,2,3],
    [4,5,6],
    [7,8,9]]  
colomn2 = [row[0] + 10 for row in m]
print(colomn2) # показывает только столбец из матрицы и прибавляет 10 к элемету

diagonal = [m[i][i] for i in [0,1,2]]
print(diagonal)

l = [1,2,3,4]
m = l
print(m)
print(l == m)
print(l is m)

import sys
print(sys.getrefcount(1))

# Метод replace позволяет изменить строку.
my_str = "Hope"
changed_str = my_str.replace('o','ttttt')
print(my_str.replace('o',"xxxx"))
print(changed_str)
print(my_str)

# Форматирование строк 
str1 = "This is %d %s bird" % (1,'dead')
print(str1)
str2 = 'This is {0} {1} bird'.format(1,'dead')
print(str2)

str3 = "xxxxSPAMxxxxSPAMxxxx"
where = str3.find('SPAM')
str3 = str3[:where] + 'FIND' + str3[(where+4):]
print(str3)
print(str3.replace("SPAM","GGGG",1))
l= list(str3)
print(type(l))
l[3] = "y"
print(l)
s = "".join(l)
print(s)

x = 12234
res = "Int: %d....%06d...."% (x,x)
print(res)

# dict = {}
# dict['name:'] = input("Enter your name ")
# dict['age:'] = input('Enter your age ')
# print(dict['name:'],dict['age:'].format())

name = input('Enter name ')
age = input('Enter age ')
msg = f'{name},{age}'
print(msg)
    

