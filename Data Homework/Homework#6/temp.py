def __lt__(self, other):
    self_pointer = self.dll.header.next
    other_pointer = other.dll.header.next
    while (self_pointer is not self.dll.trailer and other_pointer is not other.dll.trailer):
        if (self_pointer.data[0] < other_pointer.data[0]):
            self_pointer = self_pointer.next
            other_pointer = other_pointer.next
        elif (self_pointer.data[0] == other_pointer.data[0] and self_pointer.data[1] <= self_pointer.data[1]):
            self_pointer = self_pointer.next
            other_pointer = other_pointer.next
        else:
            return False
    return True