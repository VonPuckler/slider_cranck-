import numpy as np
import matplotlib.pyplot as plt
r= 20 #Crank radius
c=45 # Coupler length
 
rpm=300
omega=2*np.pi*rpm/60 #rad/sec
 
def disp(t):
    d1=r*np.cos(omega*t)
    d2=(np.sqrt(c**2-r**2*np.sin(omega*t)*np.sin(omega*t)))
    return d1+d2

time=np.linspace(0,0.5,100)
theta=omega*time*(180/np.pi)
x=disp(time)
print(disp(time))

plt.figure(figsize=(12,9))
plt.plot(theta,x,'black')
plt.ylabel('Displacement (mm)')
plt.show()