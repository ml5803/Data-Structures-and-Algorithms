'''
    The MAP ADT
'''

'''
    Model: A collection that stores values mapped by keys
    Operations:
                - m=Map() - creates a new collection
        (insert)- m[k] = v - adds the value v, mapped by k, into m
                         if there exists a value that is mapped by k, it would be replaced by v
          (find)- m[k] - returns value associated with k in m
                         or raises a KeyError if there is no such value
        (delete)- del m[k] - removes (and returns) the value that is associated with k in m (or raises a KeyError)
                - len(m) - returns # of entries in m
                - iter(m) - returns an iterator of the keys in m
'''

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
