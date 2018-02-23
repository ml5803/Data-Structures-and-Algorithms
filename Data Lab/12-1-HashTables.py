class OpenAddressingHashMap:
    class Item:
        def __init__(self,key,value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.capacity = 7
        self.size = 0
        self.array = [None] * 7

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __getitem__(self,k):
        val = hash(k)%self.capacity
        if self.array[val].key == k:
            return self.array[val].value
        else:
            i = 1
            while((hash(k)+i)%self.capacity != val):
                if self.array[(hash(k)+i)%self.capacity].key == k:
                    return self.array[(hash(k)+i)%self.capacity].value
            raise KeyError("Key Error")

    def __setitem__(self, k, v):
        try:
            self[k] = v
        except:
            if self.array[hash(k)%self.capacity] is None:
                self.array[hash(k) % self.capacity] = OpenAddressingHashMap.Item(k,v)
            else:
                i=1
                while(self.array[(hash(k) % self.capacity)+1] is not None):
                    i+=1
                self.array[(hash(k) % self.capacity)+i] = OpenAddressingHashMap.Item(k, v)

    def __delitem__(self,k):
        pass

    def __iter__(self):
        pass

    def rehash(self):
        pass
