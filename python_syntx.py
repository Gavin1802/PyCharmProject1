# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def filter_words(sentence):
    words = sentence.split()

    # TODO: Use a list comprehension to filter `words` based on:
    # - length greater than 4
    # - no digits in the word
    filtered = [ x for x in words if len(x) > 4 and not any(char.isdigit() for char in x) ]

    return filtered


# Test it
sentence = "The quick brown fox jumps over 13 lazy dogs and 4 elephants"
print(filter_words(sentence))  # ➞ ['quick', 'brown', 'jumps', 'elephants']
