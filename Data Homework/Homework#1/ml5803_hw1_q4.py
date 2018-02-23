def list_comprehension_a():
    return [10**i for i in range(6)]
print(list_comprehension_a())

def list_comprehension_b():
    return [i*(i+1) for i in range(10)]
print(list_comprehension_b())

def list_comprehension_c():
    return [chr(i+97) for i in range(26)]
print(list_comprehension_c())

