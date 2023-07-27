# this is a test
import math
import numpy as np
import matplotlib.pyplot as plt
H = 0 # Entropia de Shannon
p = 0 # probabilidade
q = 1 - p
str=[]

print ("p:", p, "q:", q, "H:", H)
for i in range(1, 100):
    p = i/100
    q = 1 - p
    p1 = p*math.log(p, 2)
    q1 = (q)*math.log(q, 2)
    H = -(p1+q1)
    print ("p:", round(p1, 2), "q:", round(q1, 2), "H:", round(H, 2))
    str.append(H)
print(str)
plt.plot(str)
plt.show()
