# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

# make sure to download words.txt and place it in the same directory!


def word_value(word):
    return sum(ord(char) - ord('A') + 1 for char in word)

def generate_triangle_numbers(limit):
    triangle_numbers = []
    n = 1
    while True:
        triangle_number = (n * (n + 1)) // 2
        if triangle_number > limit:
            break
        triangle_numbers.append(triangle_number)
        n += 1
    return triangle_numbers

def count_triangle_words(filename):
    with open(filename, 'r') as file:
        words = file.read().replace('"', '').split(',')

    max_word_length = max(len(word) for word in words)
    max_word_value = max_word_length * 26  # Maximum possible word value

    triangle_numbers = generate_triangle_numbers(max_word_value)

    count = 0
    for word in words:
        if word_value(word) in triangle_numbers:
            count += 1

    return count

filename = "words.txt"
result = count_triangle_words(filename)
print("The number of triangle words in the provided file is:", result)
