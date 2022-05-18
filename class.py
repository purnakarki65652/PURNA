class add_sub:
    def __init__(self):
        print("you are going to use arithmatic operation")
    def add(self, num1, num2):
        self.n1=num1
        self.n2=num2
        return self.n1 + self.n2
    def sub(self,num1, num2):
        self.n1 = num1
        self.n2 = num2
        return  self.n1-self.n2
x=10
y=6
opp = add_sub()
print(f'{x}+{y}={opp.add(x,y)}')
print(f'{x}-{y}={opp.sub(x,y)}')