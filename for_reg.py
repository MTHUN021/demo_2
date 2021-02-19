string = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 @#$%^&*()+ 900-434-2155 800.143.4344 144*124-1558 473/234/4244 424/467/5427 "

import re

print(re.search(r'[98]00[-.]\d{3}[.-]\d{4}', string))


