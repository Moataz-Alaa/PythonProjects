def first_second(my_list):
    first = 0
    second = 0
    for i in range(len(my_list)):
        if my_list[i] > first:
            second = first
            first = my_list[i]
        elif my_list[i] > second and my_list[i] != first:
            second = my_list[i]
    return first, second