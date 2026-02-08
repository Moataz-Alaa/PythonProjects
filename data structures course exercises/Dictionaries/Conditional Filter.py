def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}