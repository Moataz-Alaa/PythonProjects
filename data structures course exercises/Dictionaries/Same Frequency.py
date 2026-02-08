def check_same_frequency(list1, list2):
    if len(list1) != len(list2):
        return False
    wordfrequancy1 = {}
    for word in list1:
        if word in wordfrequancy1:
            wordfrequancy1[word] += 1
        else:
            wordfrequancy1[word] = 1
    wordfrequancy2 = {}
    for word in list2:
        if word in wordfrequancy2:
            wordfrequancy2[word] += 1
        else:
            wordfrequancy2[word] = 1
    return wordfrequancy1 == wordfrequancy2


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))