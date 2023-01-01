# Что такое функция, параметры и аргументы функции

# параметры финкции это то, что находится в скобках после названия функции(number,step)
def get_step(number: int ,step: int) -> int: # первый int указывает на параметры функции и показывает какой у них тип, а второй -> int показывает какого типа будет результат.
    result = number ** step
    print('Result =',result)

try:
    number = int(input('--> '))
    step = int(input('--> '))
except ValueError:
    print('Not a number!!!')
else:
    get_step(number,step)

# Аргументы задаются при вызове финкции и потом они передаются в функцию
# get_step(3,2)

def plus(*args: int) -> int:
    return sum(args)

print(plus(1,3,5,6,7))

dict = {1: 4, 2: 5, 3: 7}
res = dict.get(3,None)
if res is not None:
    print(res)
else:
    print('None')


