import random
class ChainingHashTableMap:

    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        index_list = self.table[j]
        if index_list is None:
            return []
        return index_list

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = list()
            self.n += 1
        self.table[j].append(value)
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None): yield curr_bucket

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value

class InvertedFile:
    def __init__(self, file_name):
        self.storage = []
        self.map = ChainingHashTableMap()
        with open(file_name, 'r') as f:
            for line in f:
                for word in line.split():
                    if word[-1].isalpha():
                        self.storage.append(word.lower())
                    else:
                        self.storage.append(word[: -1].lower())
        for i in range(len(self.storage)):
            self.map[self.storage[i]] = i

    def indices(self, word):
        return self.map[word]