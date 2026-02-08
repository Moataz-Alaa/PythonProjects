
def pair_sum(myList, sum):
    pairs = []
    for i in range(0, len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                pairs.append(str(myList[i]) + '+' + str(myList[j]))
    return pairs

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))