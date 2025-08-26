# Write a function that takes a list of words and returns a new
# list containing only the words that contain more vowels than consonants.

def more_vowels_than_consonants(word_list):
    result = []
    for word in word_list:
        if vowel(word) > 0:
            result.append(word)
    return result

def vowel(word):
    count = 0
    for i in word:
        if i.lower() not in 'aeiou':
            count -= 1
        else:
            count += 1

    return count


# Test
words = ["hello", "eye", "try", "automobile", "sky", "aeiou"]
print(more_vowels_than_consonants(words))  # ➞ ['eye', 'automobile', 'aeiou']
