def a_shift(lst,k):
    for i in range(k):
        lst.append(lst.pop(0))

def b_shift(lst,k,direction="left"):
    if direction == "left":
        for i in range(k):
            lst.append(lst.pop(0))
    elif direction == "right":
        for i in range(k):
            lst.insert(0,lst.pop())

# Testing left:
test=[1,2,3,4,5,6]
b_shift(test,2,"left")
print(test)
# Testing right:
b_shift(test,2,"right") #undo earlier shift
print(test)
