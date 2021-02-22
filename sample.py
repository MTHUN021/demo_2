
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

class travel:

    
    def __init__(self, source, destination, distance, time, privilege):
        self.source = source
        self.destination = destination
        self.distance = distance
        self.time = time
        self.privilege = privilege
        self.cost = 0


    def travel_fare(self):
        if self.privilege == "FIRST CLASS":
            self.cost = self.distance * 1000
        elif self.privilege == "ECONOMY":
            self.cost = self.distance * 200
        return self.cost


#t1 = travel("New York", "Beijing", 8000, 10, "ECONOMY")
#t2 = travel("London", "New York", 6000, 6, "FIRST CLASS")
#t3 = travel("Bengaluru", "Abu Dhabi", 3000, 3, "BUSINESS CLASS")
    

class PNR:

    def __init__(self, PNR_no, ticket):
        self.PNR_no = PNR_no
        self.ticket = ticket
    
    def __str__(self):
        return f"PNR NO --> [{self.PNR_no}] Travelling From {self.ticket.source} To {self.ticket.destination}"

#p1 = PNR("24613", t1)
#print(p1)


destinations = {1:"New York", 2:"London", 3:"Beijing", 4:"Tokyo", 5:"Bengaluru", 6:"Abu Dhabi"}
distance_time = [["New York", "London"]] # Source to Destination with 8000Km

def main():
    src = input("FROM: ")
    dest = input("TO: ")
    dist = distance_time[[src, dest]][0]
    ti = distance_time[[src, dest]][1]
    pri = input("FIRST CLASS OR ECONOMY")
    
    t1 = travel(src, dest, dist, ti, pri)
    p1 = PNR(3948, t1)
    print(f"Booking Confirmed with Total Amount {p1.ticket.travel_fare()} press YES OR NO To Confirm")
    if input("") == "YES":
        print(f"TICKET CONFIRMED for {p1}")
    else:
        print(f"BOOKING CANCELLED")


if __name__ == "main":
    main()
