
def concatenate_strings(input_tuple):
    sentance = input_tuple[0]
    for i in range(1, len(input_tuple)):
        sentance = sentance + ' ' + input_tuple[i]
    return sentance

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)