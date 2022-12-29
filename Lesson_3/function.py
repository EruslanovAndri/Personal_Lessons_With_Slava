# Что такое функция, параметры и аргументы функции

# параметры финкции это то, что находится в скобках после названия функции(number,step)
def get_step(number,step:int)-> int: # первый int указывает на параметры функции и показывает какой у них тип, а второй -> int показывает какого типа будет результат.
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


