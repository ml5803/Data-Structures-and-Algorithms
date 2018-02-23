def findChange(lst01):
    low = 1
    high = len(lst01)

    if(lst01[0]==1):
        return 0

    while(low < high):
        mid = (low+high)//2
        if(lst01[mid]==1 and lst01[mid-1]==0):
            return mid
        elif(lst01[mid]==0):
            low = mid+1
        else:
            high = mid

print(findChange([0,0,0,0,0,1,1,1]))
print(findChange([0,0,0,0,1,1]))
print(findChange([1,1,1,1,1,1]))
print(findChange([0,0,0,0,0,0,0]))