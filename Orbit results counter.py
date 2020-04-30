# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:17:09 2020

@author: samue
"""

from vpython import *
import numpy as np
import matplotlib.pyplot as plt

G = 6.7e-11      # Newton's gravitational constant
dt = 30.         # the time step is 60 seconds



######################################
##### OBJECTS AND INITIAL VALUES #####
######################################


Earthpos = vector(0, 0, 0)
Earthmass = 6e24
Earthradius = 6.4e6
#originbox = box(pos = vector(0,0,0),length = 100e2, width = 6.4e6, height = 6.4e100, color = color.red)



craftmass = 2.11e4
               
#craft.trail = curve( color = craft.color )    

# the velocity vector for the craft set to the craft's initial velocity


# the time variable initially set to 0
t = 0
boostertime = 0
craftdirstor = []
i=0
theta = 0
orbit = False
heightresults = []
speedresults = []
radiusresults = []
timeresults = []
massresults = []
orbitcounter = 0
initialr = 0
Temp = 0
pres = 0

epsilon = np.pi/5000



rcraft = 200
c=0.7
A = np.pi*rcraft**2





height_low = 6.4e6

height_up = 2.95e7 + 1000

height_step = 1000

mass_low = 10

mass_up = 200

mass_step = 10


######################
##### ITERATIONS #####
######################

for mass_test in range(int(mass_low),int(mass_up),int(mass_step)):
    craftmass = mass_test
    for height_test in range(int(height_low),int(height_up),int(height_step)): 
    
        t=0
        torbit = 0
        orbitcounter = 0
        Temp = 0
        press = 0
        craftpos = vector(-13e7, height_test, 0)
        initialtheta = np.arctan(craftpos.y/craftpos.x) + np.pi
        rmax = 0
        initialr = mag(craftpos)
        speed_test = ((2*G*Earthmass)/(initialr))**0.5
        
        craftvelocity = vector(speed_test,0,0)
        
        
        while t < 7*24*60*26: # while time is less than one week
            orbit = False
        
            #rate(250)
     
            
            ## Update time
            t = t + dt
          
        
            r = craftpos - Earthpos
           
    
            rMag = mag(r)
            rHat = norm(r)
            
            
            
            hfroms = rMag - Earthradius
            
    
    
            if hfroms<1e8 and hfroms>25000:
                Temp = -131.21 + 0.00299*hfroms
                pres = 2.488 * ((Temp + 273.1)/216.6)**(-11.388)
        
            elif 11000 < hfroms and 25000 > hfroms:
                Temp = -56.46
                pres = 22.65* np.exp(1.73-0.000157*hfroms)
                
            elif hfroms< 11000:
                Temp = 15.04 - 0.00649*hfroms
                pres = 101.29 * ((Temp+273.1)/288.08)**5.256
                
            rho = pres/(0.2869*(Temp + 273.1))    #From PV=NKT
            
            
            drag = 0.5*c*rho*A
            
            Fgrav = -rHat*G*Earthmass*craftmass/rMag**2
    
            Fdrag = -drag*mag2(craftvelocity)*norm(craftvelocity)
            
            
            
            
            
            if rMag>rmax:
                rmax = rMag
                
            if rMag<Earthradius+1e8:
                Fnet = Fgrav + Fdrag
                
            else: 
                Fnet = Fgrav
                
            
        
            craftvelocity = craftvelocity + Fnet/craftmass*dt
        
            
            craftpos = craftpos + craftvelocity*dt 
            
            
            if craftpos.x<0:
                theta = np.arctan(craftpos.y/craftpos.x) + np.pi
            else:
                theta = np.arctan(craftpos.y/craftpos.x)
    
        
            if rMag < Earthradius:
                
                #print("Collision!")
                break # break will terminate the while loop immediately
        
                
            if abs(theta-initialtheta)<epsilon and t>torbit + 100*dt:
                orbitcounter +=1
                torbit = t
              
    
            if orbitcounter == 1:
                orbit = True
                break
            
        
        if orbit:
            radiusresults.append((i,rmax))
            timeresults.append((i,torbit))
            speedresults.append((i,speed_test))
            heightresults.append((i,height_test))
            massresults.append((i,mass_test))
            i+=1


radiusresults = np.array(radiusresults)
timresults = np.array(timeresults)
speedresults = np.array(speedresults)
heightresults = np.array(heightresults)
massresults = np.array(massresults)

# =============================================================================
# print(radiusresults)        
# print()
# print(orbitresults)
# =============================================================================

# =============================================================================
# plt.scatter(massresults,heightresults)
# 
# =============================================================================
# =============================================================================
# plt.ylim(height_low,height_up)
# plt.xlim(speed_low,speed_up)
# =============================================================================
# =============================================================================
# plt.xlabel("Initial Velocity of Astroid")
# plt.ylabel("Furthest point from Earth")
# plt.show()
# plt.scatter(massresults[1,:],heightresults[1,:])
# plt.show()
# =============================================================================




np.savetxt('massresults(h=6.4e6--2.90e7 s=100000 ms=50).csv', massresults, delimiter=',')
np.savetxt('timeresults(h=6.4e6--2.90e7 s=100000 ms=50).csv', timeresults, delimiter=',')
np.savetxt('speedresults(h=6.4e6--2.90e7 s=100000 ms=50).csv', speedresults, delimiter=',')
np.savetxt('heightresults(h=6.4e6--2.90e7 s=100000 ms=50).csv', heightresults, delimiter=',')
np.savetxt('radiusresults(h=6.4e6--2.90e7 s=100000 ms=50).csv', timeresults, delimiter=',')