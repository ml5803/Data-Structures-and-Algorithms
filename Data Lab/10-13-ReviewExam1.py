def max(lst):
    if(len(lst) == 1):
        return lst[0]
    else:
        if(lst[0] > max(lst[1:])):
            return lst[0]
        else:
            return max(lst[1:])

print(max([0,1,6,2,5]))

def sumList(lst):
    sum = 0
    if len(lst)== 1 and isinstance(lst[0],int):
        return lst[0]
    elif len(lst) == 1 and isinstance(lst[0],list):
        return sumList(lst[0])
    else:
        if isinstance(lst[0],list):
            sum += sumList(lst[0]) + sumList(lst[1:])
        else:
            sum += lst[0] + sumList(lst[1:])
    return sum

print(sumList([1,2,3,[4,5,[6]]]))

