
def reverse(strng):
    if len(strng) == 0:
        return ''
    if len(strng) == 1:
        return strng
    return reverse(strng[1:]) + strng[0]

print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'