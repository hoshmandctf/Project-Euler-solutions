def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
        if count == n:
            return number
        number += 1

# Find the 10,001st prime number
n = 10001
result = nth_prime(n)

# Print the result
print("The", n, "st prime number is:", result)
