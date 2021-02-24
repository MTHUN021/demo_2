
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

'''
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
'''

import json

string = '''{"name":"Python", "inventor": "guido-van-rossum", "version":"3.9"}'''
d = json.loads(string)
#print(d["inventor"])

d1 = {"name":"Python", "time":"1990", "with":"C"}

class A:
    def __init__(self,x):
        self.x = x
    
    def display(self):
        print(self.x)

class B(A):
    pass

b1 = B(1)
#b1.display()
#print(B.mro())  # method reservation order

class MyTimeError(Exception):
    def __init__(self,mm,ss):
        super().__init__()
        self.mm=mm
        self.ss=ss
    def __str__(self):
        if self.mm > 59:
            return "Invalid Minutes:{0}".format(self.mm)
        elif self.ss > 59:
            return "Invalid Seconds:{0}".format(self.ss)

class MyTime:
    def __init__(self,hh,mm,ss):
        if mm > 59 or ss > 59:
            raise MyTimeError(mm,ss)
        self.hh=hh
        self.mm=mm
        self.ss=ss

    def update(self,hh,mm,ss):
        if mm > 59 or ss > 59:
            raise MyTimeError(mm,ss)
        self.hh=hh
        self.mm=mm
        self.ss=ss
    def display(self):
        print("{0}:{1}:{2}".format(self.hh,self.mm,self.ss))

'''
try:
    t1 = MyTime(10,20,72)
except MyTimeError as te:
    print(te)

s1 = Stack(5)
print(s1.elements)
try:
    s1.pop_ele(6)
    print(s1.elements)
except StackError as s:
    print(s)

def compute(x):
    if x > 100:
        raise ValueError(x)

    return x**2

try:
    print(compute(101))
except ValueError as e:
    print(f"{e} is out of range")


import logging

logging.basicConfig(level=logging.INFO)


logging.warning('classical warning')           # Warning is default without any level
logging.info('i told u so')
logging.debug("This is a debug")
logging.error("This is an error")
logging.critical('This is critical')



logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

'''
