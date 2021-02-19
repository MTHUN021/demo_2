string = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 @#$%^&*()+ 900-434-2155 800-143-4344 144-124-1558 473/234/4244 424/467/5427 "

import re

a = re.findall(r'[aA0]', string)
print(a)

