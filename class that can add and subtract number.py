class add_sub():
    #define add method
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    #define subtract method
    def sub(self):
        return  self.x - self.y
x = 10
y = 6
# create instance
opp = add_sub(x,y)
#call method
print(f'{x} + {y} = {opp.add()}')
print(f'{x} - {y} = {opp.sub()}')