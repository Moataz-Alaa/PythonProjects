
def recursiveRange(num):
    assert num == abs(num) and int(num) == num , 'Number must be positive integer'
    if num == 0:
        return 0
    return num + recursiveRange(num - 1)

num = 10
result = ((num + 1)*num)//2

print(recursiveRange(num))
print('True result: ' + str(result))