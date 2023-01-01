
# def my_empty_list():
#     my_list = []
#     return my_list

# def fill_my_list(my_list: list) -> list:
#     my_list = []
#     count = 0
#     while count <= 5:
#         num = int(input('--> '))
#         my_list.append(num)
#         count += 1
#     return my_list

# def find_max(my_list: list[int]) -> int:
#     for i in range(len(my_list)):
#         return max(my_list)
        
# print(f'Max = ',find_max(fill_my_list(my_empty_list())))

# def get_list_in_list():
#     new_list = []
#     count = 0
#     while count < 2:
#         for i in range(1,4):
#             num = int(input('Num -> '))
#             new_list.append(num)
#             count += 1
#     return new_list

# print(get_list_in_list())

a = [[11,22,33],
    [44,55,66],
    [12,13,14]]

for i in a:
    for j in i:
        print(j,end= ' ')
    print()

for i in range(0,3):
    sum = 0
    for j in range(0,3):
        sum += a[i][j]
    print(f'Sum in {i} row = ',sum)

for j in range(3):
    sum = 0
    for i in range(3):
        sum += a[i][j]
    print(f'Sum in {j} colomns = ',sum)



# def get_empty_list():
#     n  = int(input('Row -> '))
#     m = int(input('Colomns -> '))
#     my_list = []
#     for i in range(n):
#         my_list.append([1]*m)
#     for i in my_list:
#         print(i)

# get_empty_list()


def fill_nested_list():
    a = []
    row = int(input('Row -> '))
    colomn = int(input('Colomn -> ')) 
    for i in range(row):
        a.append([0]*colomn)
        print(a[i])

fill_nested_list()

a = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
def f(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                a[i][j]=1
            elif i <= j:
                a[i][j]= 0
            else:
                a[i][j] = 2
    for i in a:
        print(i)   
        

f(a)

s = list(map(int,input().split()))
print(s)

def get_sum(s):
    b = []
    for i in range(len(s)):
        res = s[i]**2
        b.append(res)
    print(b)

get_sum(s)
