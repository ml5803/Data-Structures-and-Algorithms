file = open(file_name,'r')
        lst_rep = []
        for line in file:
            line = self.strip_punctuation(line).strip().lower().split(' ')
            for word in line:
                lst_rep.append(word)
        print(lst_rep)
        self.hashmap = ChainingHashTableMap()
        for i in range(len(lst_rep)):
            new_one = False
            if self.hashmap.table[self.hashmap.hash_func(lst_rep[i])] is None:
                self.hashmap[lst_rep[i]] = (lst_rep[i],[i])
                #print(self.hashmap[lst_rep[i]])
            else:
                new_one = True
                for item in self.hashmap.table[self.hashmap.hash_func(lst_rep[i])]:
                    if item == lst_rep[i]:
                        self.hashmap.table[self.hashmap.hash_func(lst_rep[i])][lst_rep[i]][1].append(i)
                        print(self.hashmap.table[self.hashmap.hash_func(lst_rep[i])][lst_rep[i]])
                        new_one = False