import collections

def fib(num):
    if num in (1,2):
        return num
    return fib(num-1)*num


print(fib(5))


letterst = 'asdfghjer5t6yffghbn'
letterst_count = collections.Counter(letterst)
print(letterst_count.most_common(1))
