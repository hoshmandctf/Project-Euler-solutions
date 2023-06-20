# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

"""
Make sure to place the "names.txt" file in the same directory as the Python script
"""
def calculate_name_score(name):
    score = 0
    for letter in name:
        score += ord(letter) - ord('A') + 1
    return score

def calculate_total_name_scores(filename):
    with open(filename, 'r') as file:
        names = file.read().replace('"', '').split(',')

    names.sort()
    total_score = 0
    for i, name in enumerate(names, start=1):
        name_score = calculate_name_score(name)
        total_score += name_score * i

    return total_score

filename = 'names.txt'
total_name_scores = calculate_total_name_scores(filename)
print("The total of all the name scores in the file is:", total_name_scores)
