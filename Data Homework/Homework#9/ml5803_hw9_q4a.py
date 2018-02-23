def intersection_list(lst1,lst2):
    srt1 = sorted(lst1) #python's sorted runs in O(nlogn)
    srt2 = sorted(lst2)
    new_lst = []
    cursor1 = 0
    cursor2 = 0
    while(cursor1 < len(srt1) and cursor2 <len(srt2)):
        #print(cursor1,cursor2)
        if srt1[cursor1] == srt2[cursor2]:
            new_lst.append(srt1[cursor1])
            cursor1 += 1
            cursor2 += 1
        elif srt1[cursor1] > srt2[cursor2]:
            cursor2 += 1
        else:
            cursor1 += 1

    return new_lst

#print(intersection_list([3, 9, 2, 7, 1],[4, 1, 8, 2]))