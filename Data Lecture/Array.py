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
            raise IndexError(str(ind) + "is an invalid index")
        elif(ind<0):
            return self.data[self.n+ind]
        return self.data[ind]

    def __setitem__(self,ind, val):
        if (not 0 <= abs(ind) <= self.n - 1):
            raise IndexError(str(ind) + "is an invalid index")
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