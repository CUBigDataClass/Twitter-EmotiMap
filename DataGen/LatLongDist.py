import numpy as n
import math as m


#distance between LA
lo1 = m.radians(-90.05)
lo2 = m.radians(-90.4850)
la1 = m.radians(29.9667)
la2 = m.radians(30.1750)



dlon = abs(lo1-lo2)
dlat = abs(la1-la2)

a = (m.sin(dlat/2)**2) + (m.cos(la1)*m.cos(la2)*(m.sin(dlon/2)**2))
c = 2*m.atan2(m.sqrt(a), m.sqrt(1-a))
d = 3961*c

print(d)
