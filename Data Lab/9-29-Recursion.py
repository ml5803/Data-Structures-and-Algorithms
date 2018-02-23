import os
def is_palindrome(input_str, low, high):
    if(low == high or (input_str[low]==input_str[high] and low == high -1)):
        return True
    elif(input_str[low]==input_str[high]):
        return True and is_palindrome(input_str,low +1, high-1)
    else:
        return False

print(is_palindrome("kayak",0,len("kayak")-1))
print(is_palindrome("python",0,len("python")-1))
print(is_palindrome("aa",0,len("aa")-1))
print(is_palindrome("abca",0,len("abca")-1))

def binary_search(srt_lst, val, low, high):
    mid = (low + high) //2
    if(srt_lst[mid]==val):
        return mid
    elif(srt_lst[mid] > val and low < high):
        return binary_search(srt_lst,val,low+1,mid)
    elif(srt_lst[mid] < val and low < high):
        return binary_search(srt_lst,val,mid,high-1)

temp = [1,2,3,4,5,6,7]
print(binary_search(temp,5,0,len(temp)-1))
print(binary_search(temp,9,0,len(temp)-1))

def decimal_to_binary(input_int):
    x = int(input_int)
    if(x == 0):
        return ""
    elif(x%2==0):
        return decimal_to_binary(x//2) + "0"
    else:
        return decimal_to_binary(x//2) + "1"

print(decimal_to_binary(6))

def solve_hanoi(n,frm,to,extra):
    if(n == 1):
        print("move disk from ", frm, "to ", to)
    else:
        solve_hanoi(n-1,frm,to,extra)

def disk_usage(path):
    if(os.path.isdir(path)==False):
        return os.path.getsize(path)
    else:
        path_lst= os.listdir(path)
        total = 0
        for i in path_lst:
            total+= disk_usage(os.path.join(path,i))
        return total
print(disk_usage("C:\\Users\\micha\\PycharmProjects\\Data Structures and Algorithms\\"))