def pythogoren_triplet(sum_value):
    for a in range(1, sum_value):
        for b in range(a, sum_value - a):
            c = sum_value - a - b
            if a * a + b * b == c * c:
                print(a, b, c)
                return a * b * c
                
    return None
print(pythogoren_triplet(1000))