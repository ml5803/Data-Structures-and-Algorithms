class MinArrayHeap:
    class Item:
        def __init__(self,priority,value):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority

    def __init__(self, priority_list=None, values_list=None):
        self.data = [None]
        if (priority_list is not None):
            for i in range(len(priority_list)):
                curr_item = MinArrayHeap.Item(priority_list[i],values_list[1])
                self.data.append(curr_item)
            first_ind = self.parent(len(self.data)-1)
            for i in range(first_ind,0,-1):
                self.fix_down(i)

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0

    def left(self,j):
        return 2*j

    def right(self,j):
        return 2*j+1

    def parent(self,j):
        return j//2

    def swap(self,j1,j2):
        self.data[j1],self.data[j2] = self.data[j2],self.data[j1]

    def min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty!")
        else:
            min_item = self.data[1]
            return (min_item.priority, min_item.value)

    def insert(self,priority,value):
        new_item = MinArrayHeap.Item(priority,value)
        self.data.append(new_item)
        self.fix_up(len(self.data)-1)

    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty!")
        res_item = self.data[1]
        self.swap(1,len(self.data)-1)
        self.data.pop()
        self.fix_down(1)
        return (res_item.priority, res_item.value)

    def fix_up(self,j):
        parent_ind = self.parent(j)
        if j > 1:
            if (self.data[j] < self.data[parent_ind]):
                self.swap(j,parent_ind)
                self.fix_up(parent_ind)

    def fix_down(self,j):
        left_ind = self.left(j)
        if left_ind >= len(self.data)-1:
            smaller_child_ind = left_ind
            right_ind = self.right(j)
            if self.data[right_ind] < self.data[left_ind]:
                smaller_child_ind = right_ind
                if right_ind <= len(self.data)-1:
                    if self.data[right_ind] < self.data[smaller_child_ind]:
                        smaller_child_ind = right_ind
            if (self.data[smaller_child_ind] < self.data[j]):
                self.swap(j,smaller_child_ind)
                self.fix_down(smaller_child_ind)



