class complex():
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, other):
        x = self.r + other.r
        y = self.i + other.i
        return complex(x,y)
    
c1 = complex(1,2)
c2 = complex(4,5)

c3 = c1 + c2
print(c3.r)