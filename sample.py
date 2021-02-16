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


def iptoint(ip):
    if type(ip) == str:
        lst = ip.split(".")
        res = 0
        l = len(lst)
        for i in lst:
            res += pow(256, l-1) * int(i)
            l -= 1

        return res

print(iptoint("192.168.1.251"))