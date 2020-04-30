# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:33:37 2020

@author: samue
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit








indexresults = []
massresults = []
heightresults = []
radiusresults = []
speedresults = []
timeresults = []

orbitresults = np.genfromtxt('Wendyscoupons2.csv', delimiter=',')
mass2 = np.genfromtxt('massresults(h=6.4e6--2.90e7 s=100000 ms=50)3.csv',delimiter=',')
height2 = np.genfromtxt('heightresults(h=6.4e6--2.90e7 s=100000 ms=50)3.csv',delimiter=',')

indexresults = orbitresults[:,0]
massresults = orbitresults[:,1]
heightresults = orbitresults[:,2] 
radiusresults = orbitresults[:,3]
speedresults = orbitresults[:,4]
timeresults = orbitresults[:,5]

m2 = mass2[:,1]
h2 = height2[:,1]

mass=10
masslist = []
top=200
m = []
h = []
t = []
v = []
r = []
lowest = []
maximum = []
indexlist = []
minterest = []
tinterest = []
vinterest = []
rinterest = []
mass10v = []
mass10t = []
mass10r = []
mass10h = []
m = massresults
h = heightresults
t = timeresults
v = speedresults
r = radiusresults
counter = 0




#maximum.append(h[90][1])
j=0
for i in range(len(h)):
    if h[i]<h[i-1] and h[i]<h[i+1] and j<20:
        lowest.append(h[i])
        j+=1
        
k=0
for i in range(4066,5780):
    if h[i]<h[i-1] and h[i]<h[i+1] and k<20 :
        maximum.append(h[i-1])
        
        k+=1
maximum.append(h[5779])

while mass<=top:
    masslist.append(mass)
    mass +=10

# =============================================================================
# masslist = np.array(masslist)
# logx = np.log(masslist)
# logy = np.log(lowest)
# 
# curve_fit = np.polyfit(logx,logy,1)
# print(curve_fit[0])
# 
# y1 = np.exp(curve_fit[1])*np.exp(curve_fit[0]*masslist)
# =============================================================================







print(lowest)
# calculate polynomial
z = np.polyfit(masslist, lowest, 2)
w = np.polyfit(masslist,maximum,2)
f = np.poly1d(z)
g = np.poly1d(w)
print(f)
print(g)
# calculate new x's and y's
x_new = np.linspace(masslist[0], masslist[-1], 50)
y_new = f(x_new)
y2_new = g(x_new)
x=np.array(range(-10,1800))
y1=3.32*x**2-1152*x+6.66e6
y2=-7.372*x**2+2396*x+2.889e7

n=0

lnmax = np.log(maximum)
print(lnmax)
a,b = np.polyfit(masslist,lnmax,1)

bestfit = np.polyval([a,b],masslist)
print(bestfit)
# =============================================================================
# 
# for j in indexlist:
#   
#     minterest.append(m[j+1])
#     tinterest.append(t[j+1])
#     vinterest.append(v[j+1])
#     rinterest.append(r[j+1])
#     n+=1
#     
# for k in range(indexlist):
#     
#     mass10h.append(h[k+1])
#     mass10t.append(t[k+1])
#     mass10r.append(r[k+1])
# 
# =============================================================================

#fig = plt.figure(figsize=(15,10))

#ax1 = fig.add_subplot(221)
plt.scatter( m, h , label = "Successful Orbit")

plt.title('Plot of Impact Parameter (m) vs. Mass (kg)')
plt.xlabel('Mass of Asteroid (kg)')
plt.ylabel('Impact Parameter/ Vertical Height (m) ')
plt.xlim(0,210)
plt.ylim(0,4e7)
plt.legend(loc= 'upper right')
plt.show()

# =============================================================================
# plt.scatter( mass10t, mass10r, label = "Conditions for an Asteroid to get caught in Earths Orbit")
# #plt.title('Plot of mass (in kg) vs impact parameter (in m) that results in an orbit')
# plt.xlabel('Mass of Asteroid (in kg)')
# plt.ylabel('Impact Parameter\ Vertical Height (in m) ')
# #plt.xlim(0,200)
# plt.legend(loc= 'lower right')
# plt.show()
# =============================================================================
#ax2 = fig.add_subplot(222)
plt.scatter(masslist,maximum,label ="Largest  point")
plt.plot(masslist,maximum,'o')
plt.plot( x_new, y2_new, Label = "Best Fit Line")
mystring = str(y2)
#plt.text(85,2.955e7,mystring)
plt.title("Largest Impact Parameter Resulting in an Orbit")
plt.xlabel('Mass of Asteroid (kg)')
plt.ylabel('Impact Parameter/ Vertical Height (m) ')
plt.xlim(5,205)
plt.ylim(2.8e7,3e7)
plt.legend(loc = "upper left")
plt.show()
#plt.scatter(masslist,lowest, label="lowest point")
#ax3 = fig.add_subplot(223)
#plt.plot(minfit,label="minfit")
#plt.plot(masslist,y1,label="Best fit")
mystring2 = str(y1)
plt.plot(masslist,lowest,'o')
plt.plot( x_new, y_new, Label = "Best Fit Line")
plt.scatter(masslist,lowest, label = "Lowest point")
plt.title("Smallest Impact Parameter Resulting in an Orbit")
plt.xlabel('Mass of Asteroid (kg)')
plt.ylabel('Impact Parameter/ Vertical Height (m) ')
plt.xlim(5,205)
plt.ylim(6.5e6,6.7e6)
#plt.text(20,6.67e6,mystring2)
plt.legend(loc = "upper right")
plt.show()
#ax4 = fig.add_subplot(224)

plt.title("Extending the Fits")
plt.plot(x,y1,label="Extended Min Fit")
plt.plot(x,y2,label="Extended Max Fit")
plt.scatter(m,h, label="Tested orbits")
plt.xlabel('Mass of Asteroid (kg)')
plt.ylabel('Impact Parameter/ Vertical Height (m) ')
plt.scatter(m2,h2,label="Lower accuracy tests")
plt.legend(loc="upper right")

plt.show()