import numpy as np
import matplotlib.pyplot as plt

# -- Variables --

m, b, k, t, dt = map( float,input("Enter m, b, k, t, dt separated by a space: ").split())
total_time = np.arange(0, t, dt)  # Time array
x = np.zeros(len(total_time))  # Displacement array
v = np.zeros(len(total_time))  # Velocity array
x[0]=1  # Initial displacement
v[0]=0  # Initial velocity

# Damping check

if b**2-(4*m*k)<0:
    damping="Underdamped"
elif b**2-(4*m*k)>0:
    damping="Overdamped"
else:
    damping="Critically Damped"

# Iteration

for i in range(len(total_time)-1):
    a = (-b/m)*v[i]-(k/m)*x[i]
    v[i+1]=v[i]+a*dt
    x[i+1]=x[i]+v[i]*dt

# Plots

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Position vs time

ax[0].plot(total_time, x)
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Position")
ax[0].set_title("Position vs Time")

# Phase space

ax[1].plot(x, v)
ax[1].set_xlabel("Position")
ax[1].set_ylabel("Velocity")
ax[1].set_title("Phase Space")

fig.suptitle(f"Damped Harmonic Oscillator - {damping}")

plt.tight_layout()
plt.show()