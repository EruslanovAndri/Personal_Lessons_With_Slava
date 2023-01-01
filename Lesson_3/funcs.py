
def find_max_and_min(my_list: list) -> tuple[int|int]:
    min_ = my_list[0]
    max_ = my_list[0]
    for i in range(1,len(my_list)):
        if max_ < my_list[i]:
            max_ = my_list[i]
        elif min_ > my_list[i]:
            min_ = my_list[i]
    return min_,max_
# my_list = [1,4,6,32,8]
# print(find_max_and_min(my_list[:]))
# print(my_list)
        


