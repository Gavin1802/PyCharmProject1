def categorize_words(word_list):
    dict = {"short": [], "med": [], "long": []}

    for word in word_list:
        length = len(word)

        if 1 <= length <= 3:
            dict['short'].append(word)
        elif 4 <= length <= 7:
            dict['med'].append(word)
        else:
            dict['long'].append(word)

    return dict


words = ["hi", "world", "cat", "encyclopedia", "book", "a", "syntax"]
print(categorize_words(words))
