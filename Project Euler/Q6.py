#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def Sum_of_squares(n):
    Sum=0
    for i in range(1,n+1):
        Sum+=i**2
    return Sum
def Square_of_sum(n):
    Sum=0
    for i in range(1,n+1):
        Sum+=i
    return Sum**2
def Difference(n):
    return Square_of_sum(n)-Sum_of_squares(n);
print(Difference(100))