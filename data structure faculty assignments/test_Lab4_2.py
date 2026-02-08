def simplify_expression(expression):
    result = []  # The list for storing the characters of the new expression
    current_sign = '+'  # A variable to keep track of the 'real' current sign
    
    for char in expression:
        if char == '-':
            # If the current sign is +, switch to -, and vice versa
            current_sign = '-' if current_sign == '+' else '+'
        elif char == '+':
            # Ignore the plus if the current real sign is minus
            if current_sign == '-':
                result.append(current_sign)
                current_sign = '+'
            # If the current real sign is plus, do nothing (as multiple pluses are redundant)
        else:
            # If we have a 'real' sign before a non-sign character, add it
            if current_sign == '-':
                result.append(current_sign)
            # Reset the current sign after a non-sign character
            current_sign = '+'
            result.append(char)
    
    return ''.join(result)
    
# Let's try the examples
print(simplify_expression("--a+b*---c-d"))  # Output should be a+b*-c-d
print(simplify_expression("----a-+-b---c"))  # Output should be a+b-c