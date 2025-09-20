## Given x (int) print a christmas tree of height x
def print_christmas_tree(x):
    for i in range(x):
        print(" " * (x - i - 1) + "*" * (2 * i + 1))

## x0 = "apple", y0 = "adcsjncjsppaxjjnaxle" --> True if all characters of x0 are in y0 in order, y0 = "bsdpple" --> False, y0 = "paple" --> False
def is_subsequence(x0, y0):
    i, j = 0, 0
    while i < len(x0) and j < len(y0):
        if x0[i] == y0[j]:
            i += 1
        j += 1
    return i == len(x0)


print_christmas_tree(15)
print(is_subsequence("apple", "adcsjncjsppaxjjnaxle"))
print(is_subsequence("car", "computer"))
print(is_subsequence("ton", "python"))
