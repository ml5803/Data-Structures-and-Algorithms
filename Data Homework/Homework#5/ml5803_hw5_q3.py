#Question 3 - Postfix Calculator
class EmptyCollection(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self)==0)

    def push(self,elem):
        self.data.append(elem)

    def pop(self):
        if(self.is_empty()):
            raise EmptyCollection("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty()):
            raise EmptyCollection("Stack is empty")
        return self.data[-1]

class PostfixCalculator:

    def __init__(self):
        self.stack = ArrayStack()
        self.operators = "+-*/"
        self.variables = {}

    def eval_exp(self,exp):
        exp = self.format_exp(exp)
        for token in exp:
            if (token not in self.operators):
                self.stack.push(int(token))
            else:
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                if token == "+":
                    res = arg1 + arg2
                elif token == "-":
                    res = arg1 - arg2
                elif token == "*":
                    res = arg1 * arg2
                elif token == "/":
                    res = arg1 / arg2
                self.stack.push(res)
        return self.stack.pop()

    def format_exp(self,exp):
        exp_lst = exp.split()
        for elem in range(len(exp_lst)):
            if exp_lst[elem] in self.variables.keys():
                exp_lst[elem] = str(self.variables[exp_lst[elem]])
        return exp_lst

    def updateVar(self,var,val):
        self.variables[var] = val

    def items(self):
        return self.variables

    def getKeyValue(self,key):
        return self.variables[key]

    def run(self):
        temp_exp = ""
        run = True
        while (run):
            scanner = input("-->")
            if (scanner == "done()"): #to exit prompt loop
                run = False
            elif (scanner[0].isdigit()): #for expressions without variable
                print(pCalc.eval_exp(scanner))
            else:
                if " = " in scanner: #for assignment statements
                    eq_lst = scanner.split(" = ")
                    ans = pCalc.eval_exp((eq_lst[1]))
                    pCalc.updateVar(eq_lst[0], ans)
                    print(eq_lst[0])
                elif len(scanner) == 1: #for getting value of a variable
                    print(pCalc.getKeyValue(scanner))
                else:
                    print(pCalc.eval_exp(scanner)) #expressions with variables ex: x y +

if __name__ == "__main__":
    pCalc = PostfixCalculator()
    pCalc.run()


