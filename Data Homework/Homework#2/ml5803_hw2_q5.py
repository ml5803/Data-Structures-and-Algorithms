def split_parity(lst):
    even_pointer = len(lst)-1
    odd_pointer = 0
    while(odd_pointer<even_pointer):
        if(lst[odd_pointer]%2==1):
            odd_pointer+=1
        elif(lst[even_pointer]%2==0):
            even_pointer-=1
        else:
            lst[even_pointer],lst[odd_pointer] = lst[odd_pointer],lst[even_pointer]
    return lst

print(split_parity([1,2,3,4]))
print(split_parity([2,2,2,3]))
print(split_parity([1,1,1,4]))