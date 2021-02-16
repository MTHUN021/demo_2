#Mobile Billing customer class
class mobile_billing():
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

    def total_bill(self):

        self.bill += self.time * self.callrate + self.sms * self.smsrate + self.carry_amt
        if self.addon:
            self.bill = self.bill +  10
        return self.bill



#Bank account class 
class Bank_account():

    def __init__(self, account_no, balance, overdraft):
        self.account_no = account_no
        self.balance = balance
        self.overdraft = overdraft

        self.interest_rate = 0.04
        self.branch = "Vijaynagar"
    
    def credit(self, value):
        self.balance += value
    
    def debit(self, value):
        self.balance -= value
    
    def comp_int(self, n):
        self.balance *= (1+self.interest_rate)*n   # n in years

    def __str__(self):
        return f"No.{self.account_no} with Total Balance(balance - overdraft) = Rs.{self.balance - self.overdraft}"

                    
# Color class
class color():
    
    def __init__(self, hex_value):
        self.red = hex_value[0]
        self.green = hex_value[1]
        self.blue = hex_value[2]
    
    def form_color(self):
        pass



# Point class
class Point():

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
        return f"({self.p1}, {self.p2})"
    
    def dist_origin(self):        # returns distance of the point from origin
        return round(pow((self.x**2 + self.y**2), 0.5), 3)

class shape():
    pass

#Class Box

class box():
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def volume(self):
        return self.length * self.breadth * self.height
    
    def display(self):
        print(f"Length = {self.length}, Breadth = {self.breadth}, Height = {self.height}")