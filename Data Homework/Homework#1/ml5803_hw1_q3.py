def sum_squares(n):
    total = 0
    for i in range(n):
        total+= i**2
    return total
# Test:
print(sum_squares(3)) #1,2 -> 1+4 = 5

def sum_squares_comprehension(n):
    total = sum([i**2 for i in range(3)])
    return total
# Test
print(sum_squares_comprehension(3)) #1,2 -> 1+4 = 5

def sum_odd_squares(n):
    total = 0
    for i in range(n):
        if i%2==1:
            total += i**2
    return total
# Test
print(sum_odd_squares(4))#1,3 -> 1+9 = 10

def sum_odd_squares_comprehension(n):
    total = sum([i**2 for i in range(n) if i%2 == 1])
    return total
# Test
print(sum_odd_squares_comprehension(4))#1,3 -> 1+9 = 10