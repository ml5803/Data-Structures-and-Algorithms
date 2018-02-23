#Question 1
def split_by_sign(lst, low, high):
    if low == high:
        return [lst[low]]
    else:
        if lst[low] < 0:
            return [lst[low]] + split_by_sign(lst, low +1, high)
        else:
            return split_by_sign(lst,low+1,high) + [lst[low]]

print("This is split_by_sign([-1,2,-3,4,-5],0,4)")
print(split_by_sign([-1,2,-3,4,-5],0,4))

#Question 2
def permutation(lst, low, high):
    res = []
    if low == high:
        res = [lst]
    else:
        for i in range(high - low +1):
            rest = lst[:]
            temp = rest[low]
            rest[low] = rest[high-i]
            rest[high-i] = temp
            res.extend(permutation(rest,low+1,high))
    return res

print("This is permutation([1,2,3],0,2)")
print(permutation([1,2,3],0,2))

#Question 3
import ctypes #provides low-level arrays

def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self,val):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self,new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def __getitem__(self, ind):
        if (not 0 <= abs(ind) <= self.n - 1):
            raise IndexError(str(ind) + " is an invalid index")
        elif(ind<0):
            return self.data[self.n+ind]
        return self.data[ind]

    def __setitem__(self,ind, val):
        if (not 0 <= abs(ind) <= self.n - 1):
            raise IndexError(str(ind) + " is an invalid index")
        elif(ind<0):
            self.data[self.n+ind] = val
        else:
            self.data[ind] = val

    def __str__(self):
        s = "["
        for i in range(self.n-1):
            s+= str(self.data[i]) + " "
        s+= str(self.data[self.n-1]) + "]"
        return str(s)

    def __repr__(self):
        s = "["
        for i in range(self.n - 1):
            s += str(self.data[i]) + " "
        s += str(self.data[self.n - 1]) + "]"
        return str(s)

    def __add__(self,other):
        newList = MyList()
        newList.resize(self.n + other.n)
        for i in range(self.n):
            newList.append(self.data[i])
        for j in range(other.n):
            newList.append(other.data[j])
        return newList

    def __iadd__(self,other):
        self.resize(self.n + other.n)
        for i in other.data:
            self.append(i)
        return self

    def __mul__(self,other):
        new_list = MyList()
        new_list.resize(other * self.n)
        for i in range(other):
            for j in range(self.n):
                new_list.append(self.data[j])
        return new_list

    def __rmul__(self,other):
        new_list = MyList()
        new_list.resize(other * self.n)
        for i in range(other):
            for j in range(self.n):
                new_list.append(self.data[j])
        return new_list

    #Question 3 - Part A
    def insert(self,index,val):
        if not 0 <= index <= self.n - 1:
            raise IndexError(str(index) + " is an invalid index")
        self.append(val)
        for i in range(self.n-1, index, -1):
            self.data[i],self[i-1] = self.data[i-1], self.data[i]

    #Question 3 - Part B
    def pop(self):
        if self.n == 0:
            raise IndexError("Nothing to be removed.")
        temp = self.data[self.n-1]
        self.data[self.n-1] = None
        self.n -= 1
        if self.n < self.capacity//4:
            self.resize(self.capacity//2)
        return temp

    #Question 3 - Part D Extra Credit
    def popIndex(self, index):
        if self.n == 0:
            raise IndexError("Nothing to be removed.")
        temp = self.data[index]
        for i in range(index,self.n-1):
            self.data[i] = self.data[i + 1]
        self.data[self.n-1] = None
        self.n -= 1
        if self.n < self.capacity//4:
            self.resize(self.capacity//2)
        return temp


print("This is MyList.insert()")
x = MyList()
x.append(1)
x.append(2)
x.insert(0,0)
x.append(4)
x.insert(3,3)
x.insert(0,-1)
print(x)
print("This is MyList.pop()")
print(x.pop())
print(x.popIndex(0))
print(x)

# def find_duplicates_ignore(lst):
#     dups = []
#
#     for i in range(0, len(lst)):
#         print(lst)
#         el = lst[i]
#         if isinstance(el,int):
#             lst[el] = [lst[el],"ref"]
#         elif isinstance(el,list):
#             if isinstance(lst[el[0]],list) and lst[el[0]][1] != "ref":
#                 dups.append(lst[el[0]][0])
#                 lst[el[0]][1] = "add"
#
#             else:
#                 lst[el[0]] = [lst[el[0]],"ref"]
#     return dups

#Question 4
def find_duplicates(lst):
    dups = []
    temp = [""] * len(lst)
    for i in lst:
        if temp[i] == "ref":
            temp[i] = "added"
            dups.append(i)
        else:
            temp[i] = "ref"
    return dups

print("This is find_duplicates([2,4,4,1,2])")
print(find_duplicates([2,4,4,1,2]))

#Question 5
def remove_all(lst,value):
    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            count+=1
    for j in range(count):
        lst.remove(value)

print("This is remove_all()")
y = [1,2,3,4,1,1,1]
remove_all(y,1)
print(y)
