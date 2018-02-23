def two_sum(srt_lst, target):
    lower = 0
    upper = len(srt_lst)-1

    while (lower < upper):
        if(srt_lst[lower] + srt_lst[upper] > target):
            upper-=1
        elif(srt_lst[lower] + srt_lst[upper] < target):
            lower+=1
        elif(srt_lst[lower] + srt_lst[upper] == target or lower > upper):
            return (lower,upper)
        else:
            return None

print(two_sum([-2,7,11,15,20,21],22))
print(two_sum([-2,7,11,15,20,21],100))