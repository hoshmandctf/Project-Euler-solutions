# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def number_to_words(n):
    # Define the word representation of numbers from 1 to 19
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
            'eighteen', 'nineteen']

    # Define the word representation of tens from 20 to 90
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n == 1000:
        return 'onethousand'

    words = ''
    hundreds = n // 100
    tens_and_ones = n % 100

    if hundreds > 0:
        words += ones[hundreds] + 'hundred'
        if tens_and_ones > 0:
            words += 'and'

    if tens_and_ones < 20:
        words += ones[tens_and_ones]
    else:
        words += tens[tens_and_ones // 10] + ones[tens_and_ones % 10]

    return words

def count_letters_in_numbers(start, end):
    total_letters = 0
    for n in range(start, end + 1):
        words = number_to_words(n)
        total_letters += len(words)
    return total_letters

# Count the number of letters in numbers from 1 to 1000
total_letters = count_letters_in_numbers(1, 1000)
print("The total number of letters used in writing numbers from 1 to 1000 is:", total_letters)
