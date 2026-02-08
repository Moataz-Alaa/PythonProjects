def count_word_frequency(words):
    worddict = {}
    for word in words:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return worddict

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))