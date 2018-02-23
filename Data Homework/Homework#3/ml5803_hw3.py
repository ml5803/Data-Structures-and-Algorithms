#Question 3
def print_triangle(n):
    if n==0:
        return
    else:
        print_triangle(n-1)
        print(n*"*")

print("This is print_triangle")
print_triangle(4)

def print_oposite_triangle(n):
    if n == 0:
        return
    else:
        print(n*"*")
        print_oposite_triangle(n-1)
        print(n*"*")

print("This is print_oposite_triangle")
print_oposite_triangle(4)

def print_ruler(n):
    if n < 1:
        return
    elif n == 1:
        print("-")
    else:
        print_ruler(n-1)
        print(n*"-")
        print_ruler(n-1)

print("This is print_ruler(4)")
print_ruler(4)

#Question 4
def list_min(lst , low, high):
    if low == high:
        return lst[low]
    elif (lst[low] < list_min(lst, low+1, high)):
        return lst[low]
    else:
        return list_min(lst,low+1,high)

print("This is list_min([1,3,2,0],0,3")
print(list_min([1,3,2,0],0,3))

#Question 5a
def count_lowercase(s , low, high):
    total = 0
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            total+=1
        return total + count_lowercase(s,low+1,high)

#Question 5b
def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low].islower():
            return False
        return True
    else:
        if s[low].islower():
            return not(is_number_of_lowercase_even(s, low+1, high))
        else:
            return (is_number_of_lowercase_even(s, low + 1, high))


print("This is count_lowercase(aBcDef,0,5)")
print(count_lowercase("aBcDef",0,5))
print("This is is_number_of_lowercase_even(abCd),0,3")
print(is_number_of_lowercase_even("abCd",0,3))

#Question 6
def appearances(s , low, high):
    d={}
    if low == high:
        return {s[low]:1}
    else:
        if(s[low] in appearances(s,low+1,high).keys()):
            d.update(appearances(s, low + 1, high))
            d[s[low]] +=1
            return d
        else:
            d.update({s[low]:1})
            d.update(appearances(s, low + 1, high))
            return d

print("This is appearances(Hello world,0,10)")
print(appearances("Hello world", 0, 10))

#Question 7
def flat_list(nested_list, low, high):
    if low == high:
        if type(nested_list[low]) is list:
            return flat_list(nested_list[low],0,len(nested_list[low])-1)
        else:
            return[nested_list[low]]
    elif type(nested_list[low]) is list:
        return flat_list(nested_list[low],0,len(nested_list[low])-1) + flat_list(nested_list,low+1,high)
    else:
        return [nested_list[low]] + flat_list(nested_list,low+1,high)

print("This is flat_list([1,2],3,[4,[5,6,[7],8]]],0,2)")
print(flat_list([[1,2],3,[4,[5,6,[7],8]]],0,2))
