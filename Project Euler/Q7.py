#What is the 10001 st prime number?

def nth_prime(n):
    """Returns the nth prime number."""
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    primes = []
    candidate = 2  
    
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > candidate:  
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    
    return primes[-1]

print(nth_prime(10001)) 
