#Mobile Billing customer class //

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

a1 = mobile_billing(1731, 90, "PREPAID", 1500, False)
                    
# Color class //
class color():
    
    def __init__(self, hex_value):
        self.red = hex_value[0]
        self.green = hex_value[1]
        self.blue = hex_value[2]
    
    def form_color(self):
        pass

c1 = color((222,11,99))

# Point class //
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

