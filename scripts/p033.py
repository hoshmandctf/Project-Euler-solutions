# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

from fractions import Fraction

curious_fractions = []

# Loop through possible numerators (10 to 98) and denominators (11 to 99)
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if numerator % 10 != 0 and denominator % 10 != 0:
            common_digit = None
            num_digits = set(str(numerator))
            den_digits = set(str(denominator))
            
            # Find the common digit between the numerator and denominator
            if num_digits.intersection(den_digits):
                common_digit = num_digits.intersection(den_digits).pop()
            
            if common_digit:
                # Remove the common digit from numerator and denominator
                num_remain = int(str(numerator).replace(common_digit, '', 1))
                den_remain = int(str(denominator).replace(common_digit, '', 1))
                
                # Check if the simplified fraction is equivalent to the original fraction
                if num_remain / den_remain == numerator / denominator:
                    curious_fractions.append(Fraction(numerator, denominator))

product_of_fractions = Fraction(1, 1)
for fraction in curious_fractions:
    product_of_fractions *= fraction

result_denominator = product_of_fractions.denominator
print("Value of the denominator in lowest common terms:", result_denominator)
