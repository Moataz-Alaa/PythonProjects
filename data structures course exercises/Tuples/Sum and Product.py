
def sum_product(input_tuple):
    sum = 0
    product = 1
    for element in input_tuple:
        sum += element
        product *= element
    return sum, product

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)