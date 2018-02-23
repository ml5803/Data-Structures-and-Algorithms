# def insert(self, index, val):
#     if (not 0 <= index <= self.n - 1):
#         raise IndexError(str(index) + "is an invalid index")
#     else:
#         if (self.n < self.capacity):
#             new_array = make_array(self.capacity)
#             for i in range(index):
#                 new_array[i] = self.data[i]
#             new_array[index] = val
#             for j in range(index + 1, self.n + 1):
#                 new_array[j] = self.data[j - 1]
#             self.n += 1
#             self.data = new_array
#         else:
#             new_size = 2 * self.capacity
#             new_array = make_array(new_size)
#             self.capacity = new_size
#             for i in range(index):
#                 new_array[i] = self.data[i]
#             new_array[index] = val
#             for j in range(index + 1, self.n + 1):
#                 new_array[j] = self.data[j - 1]
#             self.n += 1
#             self.data = new_array
#
#
# def insert2(self, index, val):
#     if not 0 <= index <= self.n - 1:
#         raise IndexError(str(index) + " is an invalid index")
#     else:
#         if self.n < self.capacity:
#             for i in range(self.n, index, -1):
#                 self.data[i] = self.data[i - 1]
#             self.data[index] = val
#             self.n += 1
#         else:
#             new_size = 2 * self.capacity
#             new_array = make_array(new_size)
#             self.capacity = new_size
#             for i in range(index):
#                 new_array[i] = self.data[i]
#             new_array[index] = val
#             for j in range(index + 1, self.n + 1):
#                 new_array[j] = self.data[j - 1]
#             self.n += 1
#             self.data = new_array

def duplicates(arr):
    # where we will store our duplicate values
    dups = []

    for i in range(0, len(arr)):
        print(arr)
        # get element in array and check if array is in bounds
        if abs(arr[i]) == len(arr):
            el = -1
        else:
            el = arr[abs(arr[i])]

        # element in array is positive so make it negative
        if el > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]

        # special case if element is zero
        # we set the value at this index to -arr.size as not to
        # mix this number up with the others because we know the
        # numbers are all in the range of 0 to n-1
        elif el == 0:
            arr[abs(arr[i])] = -len(arr)

        # element is negative so it is a duplicate
        else:
            if abs(arr[i]) == len(arr):
                dups.append(0)
            else:
                dups.append(abs(arr[i]))

    return dups


print(duplicates([1,4,4,4,4,4,4,1,2]))