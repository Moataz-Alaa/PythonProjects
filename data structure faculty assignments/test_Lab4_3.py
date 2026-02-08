def remove_redundant_minus(expression):
    result = []
    is_minus = False

    for char in expression:
        if char == '-':
            is_minus = not is_minus
        elif is_minus:
            result.append('-')
            is_minus = False

        if char != '-':
            result.append(char)

    return ''.join(result)

# Sample usage:
input_1 = "--a+b*---c-d"
output_1 = remove_redundant_minus(input_1)
print(output_1)

input_2 = "----a-+-b---c"
output_2 = remove_redundant_minus(input_2)
print(output_2)