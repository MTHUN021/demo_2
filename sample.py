
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

import random
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
            self.cost = self.distance * 150
        elif self.privilege == "ECONOMY":
            self.cost = self.distance * 20
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


destinations = {"New York":1, "London":2, "Beijing":3, "Tokyo":4, "Bengaluru":5, "Abu Dhabi":6}
distance_time = {12:(5600, 5), 21:(5600, 5), 23:(8200,10), 32:(8200,10), 34:(2100, 3), 43:(2100, 3), 45:(6650,10), 54:(6650,10), 56:(2750,4), 65:(2750,4), 13:(11000,14), 31:(11000,14), 14:(10900, 14), 41:(10900, 14), 15:(13360, 17), 51:(13360, 17), 16:(11040, 14), 61:(11040, 14), 24:(8200,11), 42:(8200,11), 25:(9570,9), 52:(9570,9), 26:(5500,7), 62:(5500, 7), 31: (10980, 13), 13:(10980, 13), 35:(5575, 10), 53:(5575, 10), 36:(6000, 9), 63:(6000, 9), 46:(8200,13), 64:(8200,13), 41:(10850, 13), 14:(10850,13), 42:(6000,13), 24:(6000,13), 43:(6700,11), 34:(6700,11), 51:(13400,12), 15:(13400, 12), 52:(8000,11), 25:(8000,11), 53:(7650,10), 35:(7650,10), 54:(8500,11), 45:(8500,11), 61:(11040,15), 16:(11040,15), 62:(5520, 8), 26:(5520,8), 63:(6000, 7), 36:(6000, 7), 64:(8100, 9), 46:(8100, 9)}

#Please update the distance and time data for calculations purposes.

all_pnr = []

def main():
    src = input("FROM: ")
    dest = input("TO: ")
    dist = distance_time[int(str(destinations[src]) + str(destinations[dest]))][0]
    ti = distance_time[int(str(destinations[src]) + str(destinations[dest]))][1]
    pri = input("FIRST CLASS OR ECONOMY: ")
    
    t1 = travel(src, dest, dist, ti, pri)
    p1 = PNR(random.randrange(1, 1000000), t1)
    print(f"Booking Confirmed with Total Amount {p1.ticket.travel_fare()} press YES OR NO To Confirm")
    if input("") == "YES":
        print(f"TICKET CONFIRMED for {p1}")
        all_pnr.append(p1)
    else:
        print(f"BOOKING CANCELLED")

def check_pnr(val):

    for p1 in all_pnr:
        if p1.PNR_no == val:
            print("TICKET FOUND")
            print(f"--------------------------------------\n| {p1.ticket.source}      >>>>>>>      {p1.ticket.destination}  |\n\n| DISTANCE                     {p1.ticket.distance} |\n\n| TIME:                     {p1.ticket.time} HRS |\n--------------------------------------")
            break

if __name__ == "__main__":
    while True:
        print("1.TICKET BOOKING OR 2.CHECK PNR STATUS AND -1 TO EXIT")
        n = int(input("ENTER OPTION: "))
        if n == 1:
            main()
        elif n == 2:
            check_pnr(int(input("ENTER PNR NO")))
        elif n == -1:
            break

    
