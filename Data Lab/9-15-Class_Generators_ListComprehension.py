class Polynomial:
    def __init__(self,lst):
        if (not lst):
            self.lst = []
        else:
            self.lst = lst

    def __str__(self):
        string = ""

        for i in range(len(self.lst)-1,-1,-1):
            if(self.lst[i] > 0 and i != len(self.lst) -1):
                string += "+"

            if(self.lst[i] != 0):
                string += str(self.lst[i]) + "x^" + str(i)

        return string

    def eval(self,num):
        x = 0.0
        for i in range(len(self.lst)-1,-1,-1):
            x+= self.lst[i] * num ** i
        return x

    def __add__(self,poly):
        pLst = []
        list = self.shorterList(poly,self.lst)

        for x in range(0,len(list[0]) - len(list[1])):
            pLst.append(x)
        for i in range(len(list[0])):
            pLst.append(list[0][i]  + list[1][i+len(list[0])])

        return Polynomial(pLst)

    def shorterList(self,l1,l2):
        if(len(l1)<len(l2)): return [l1,l2]
        else: return [l2,l1]

    def __len__(self):
        return len(self.lst)

x = Polynomial([3,7,0,-9,2])
print(x)
y = x.eval(1)
print(y)
z = x.__add__(x)
print(z)