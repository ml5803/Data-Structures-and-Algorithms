def fib_generator(n):
    num1 = 1
    num2 = 1
    for i in range(n):
        yield num1
        num1,num2 = num2, num1+num2

for curr in fib_generator(8):
    print(curr)
