#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
def lcm(a, b):
    return a * b // gcd(a, b)
def lcm_multiple(n):
    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)
    return multiple

print(lcm_multiple(20))