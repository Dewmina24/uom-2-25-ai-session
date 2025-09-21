#Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(digits):
    max_palindrome = 0
    for i in range(10**(digits-1), 10**digits):
        for j in range(i, 10**digits):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

print(largest_palindrome_product(3))