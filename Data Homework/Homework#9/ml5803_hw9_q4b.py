import random
class UnsortedArrayMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value

    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for item in self.data:
            if item.key == key:
                item.value = value
                return
        new_item = UnsortedArrayMap.Item(key,value)
        self.data.append(new_item)

    def __getitem__(self, key):
        for item in self.data:
            if item.key == key:
                return item.value
        raise KeyError("KeyError:" + str(key))

    def __delitem__(self, key):
        for ind in range(len(self.data)):
            if(self.data[ind].key == key):
                val = self.data[ind].value
                self.data.pop(ind)
                return val
        raise KeyError("KeyError:" + str(key))

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item.key


class ChainingHashTableMap:
    def __init__(self,N=64,p=40206835204840513073):
        self.N = N
        self.n = 0
        self.table  = [None] * self.N
        self.p = p
        self.a = random.randint(1,self.p-1)
        self.b = random.randint(0,self.p-1)

    def __getitem__(self,key):
        j = self.hash_func(key)
        curr_bucket = self.table[j]
        if(curr_bucket is None):
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        j = self.hash_func(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
        old_size = len(self.table[j])
        self.table[j][key] = value
        new_size = len(self.table[j])
        if new_size > old_size:
            self.n += 1
        if self.n > self.N:
            self.rehash(2*self.N)

    def __delitem__(self, key):
        j = self.hash_func(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error:" + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (len(curr_bucket) == 0):
            self.table[j] = None
        if(self.n < self.N // 4):
            self.rehash(self.N//2)

    def hash_func(self,key):
        return ((self.a * hash(key)) + self.b) % self.p % self.N

    def rehash(self,new_size):
        old_data = []
        for key in self:
            val = self[key]
            p = (key,val)
            old_data.append(p)

        self.N = new_size
        self.n = 0
        self.table = [None] * self.N
        #this could be where you change self.a, self.b if you wish
        for (key,val) in old_data:
            self[key] = val

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def __len__(self):
        return self.n

def intersection_list(lst1,lst2):
    hashmap = ChainingHashTableMap()
    new_lst = []
    if len(lst1) >= len(lst2):
        for item in lst1:
            hashmap[item] = item
    else:
        for item in lst2:
            hashmap[item] = item

    # for elem in hashmap:
    #     print(elem)

    for items in lst2:
        if hashmap.table[hashmap.hash_func(items)] is not None and items in hashmap.table[hashmap.hash_func(items)]:
            new_lst.append(items)

    return new_lst

# print(intersection_list([3, 9, 2, 7, 1],[4, 1, 8, 2]))