#Mobile Billing customer class
import webcolors
class mobile_billing:
    def __init__(self, time, sms, service, carry_amt, addon):
        self.time = time            # total outgoing call time
        self.sms = sms              # total outgoing sms
        self.service = service      # Type of service
        self.carry_amt = carry_amt  # Previous unpaid balance
        self.addon = addon          # Any add-on service
        self.bill = 0               # Bill amount at start of the month

        if self.service == 'POSTPAID':
            self.callrate = 0.01
            self.smsrate = 1
        else:
            self.callrate = 0.005
            self.smsrate = 0.5
    
    def update_time(self, n):
        self.time += n
    
    def update_sms(self, n):
        self.sms += n

    def total_bill(self):

        self.bill += self.time * self.callrate + self.sms * self.smsrate + self.carry_amt
        if self.addon:
            self.bill = self.bill +  10
        return self.bill

#Bank account class 
class Bank_account:


    def __init__(self, account_no, balance, overdraft):
        self.account_no = account_no
        self.balance = balance
        self.overdraft = overdraft
        self.interest_rate = 0.04
        self.branch = "Vijaynagar"
    

    def credit(self, value):
        self.balance += value
        return self.balance
    

    def debit(self, value):
        if self.balance <= 0:
            raise Exception
        self.balance -= value
        return self.balance
    

    def comp_int(self, n):
        self.balance *= (1+self.interest_rate)*n   # n in years


    def __str__(self):
        return f"No.{self.account_no} with Total Balance(balance - overdraft) = Rs.{self.balance - self.overdraft}"

                    
# Color class
class color:
    

    def __init__(self, hex_value):
        self.red = hex_value[0]
        self.green = hex_value[1]
        self.blue = hex_value[2]
        self.hex_value = hex_value
    

    def form_color(self):
        try:
            return webcolors.rgb_to_name(self.hex_value)
        except ValueError:
            print("Invalide color code")
    

# Point class
class Point:


    def __init__(self, x, y):
        self.x = x                # X Co-ordinate
        self.y = y                # Y Co-ordinate


    def quad(self):               # returns quadrant of the point
        if self.x > 0:
            if self.y > 0:
                return 1
            else:
                return 2
        else:
            if self.y > 0:
                return 3
            else:
                return 4


    def __str__(self):
        return f"({self.x}, {self.y})"
    

    def dist_origin(self):        # returns distance of the point from origin
        return round(pow((self.x**2 + self.y**2), 0.5), 3)


#Class Circle/Rectangle/Triangle        
class circle:


    def __init__(self, radius):
        self.radius = radius
        

    def circumference(self):                           #An example of Polymorphism
        return 2*3.141*self.radius                     #Operator overloading not allowed,  function defined latest/recent will be taken 
    

    def area(self):
        return 3.141 * (self.radius ** 2)

class triangle:


    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
        self.s = (self.a + self.b + self.c)/2


    def area(self):
        return pow(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c), 0.5)
    

    def circumference(self):
        return self.a + self.b + self.c

class rectangle():


    def __init__(self, a,b):
        self.a = a
        self.b = b


    def area(self):
        return self.a * self.b
    

    def circumference(self):
        return 2 * (self.a + self.b)


#Class Box
class box:


    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
    

    def volume(self):
        return self.length * self.breadth * self.height
    

    def display(self):
        print(f"Length = {self.length}, Breadth = {self.breadth}, Height = {self.height}")

#class IP address
class ipaddress:


    def __init__(self, int_address):
         self.address = int_address


    def address_str(self):            #converts integer to "a.b.c.d format"
        s = ""
        k = 3
        while k >=0:
            s += str((self.address // pow(256, k))%256) + "."
            k -= 1

        return s[:-1]
                                                                                                     
                                                                                                
