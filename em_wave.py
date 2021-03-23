"""
    Animated electromagnetic wave.
    Inputs:
        - k: float - abs(wave vector)
        - omega: float - angular frequency
        - dt: float - time step
        - max: float - maximum length of axis
        - amp: float - (scaled) amplitude of the waves
    How it works:
        - animating the sin-waves (E and B components)
        - calculating the length of the shown arrows for discret potitions on the k axis
    Used class:
        - Arrow3D
          Used to create the arrows (see 'lib/Arrow3D.py')
"""

#imports
from lib.imports import *

#user inputs
k = 0.07 #abs(wave vector)
omega = 0.2 #angular frequency = 2*pi/T
dt = 0.1 #time step
max = 100 #maximum length of axis
amp = 100 #(scaled) amplitude of the waves

#constants
T = 2*np.pi / omega
min = -max

#plotting and animation
fig = plt.figure(figsize=(12, 10))
ax = plt.axes(projection='3d')
ax._axis3don = False #no coordinate system
ax.view_init(30, 30) #perspective

time = np.arange(0, T, dt)
N = len(time)
frames = []
dx = 20*max/(N-1)
x = np.arange(min, max, dx)

print("Creating animation...\n")
for i in tqdm.tqdm(range(N)):
    #x,y,z components of the electric field
    Ey = np.linspace(-100, 100, 1000)
    Ex = np.zeros_like(Ey)
    Ez = amp*np.sin(k*Ey-omega*time[i])/2
    #x,y,z components of the magnetic field
    My = np.linspace(-100, 100, 1000)
    Mz = np.zeros_like(My)
    Mx = amp*np.sin(k*My-omega*time[i])/2

    plot1, = ax.plot3D(Ex, Ey, Ez, 'red')
    plot2, = ax.plot3D(Mx, My, Mz, 'blue')

    anilist = [plot1, plot2]
    #creating arrows
    for xs in x:
        z = amp*np.sin(k*xs-omega*time[i])/2
        arrow = Arrow3D([0, 0], [xs, xs], [0, z], mutation_scale=5, lw=1, arrowstyle="-|>", color="r")
        plotarrow = ax.add_artist(arrow)
        anilist.append(plotarrow)
        Y = amp*np.sin(k*xs-omega*time[i])/2
        arrow = Arrow3D([0, Y], [xs, xs], [0, 0], mutation_scale=5, lw=1, arrowstyle="-|>", color="b")
        plotarrow = ax.add_artist(arrow)
        anilist.append(plotarrow)

    frames.append(anilist)

#arrows for indication the direction of E, B and k
a = Arrow3D([0, 0], [-max, max*1.7], [0, 0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
Earrow = Arrow3D([0, 0], [max*1.3, max*1.3], [0, amp/2], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
Marrow = Arrow3D([0, amp/2], [max*1.3, max*1.3], [0, 0], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
ax.add_artist(Earrow)
ax.add_artist(Marrow)
ax.add_artist(a)
ax.text(0, max*1.4, amp/2, r"$\vec{E}$", color="r")
ax.text(amp/2, max*1.45, 0, r"$\vec{B}$", color="b")
ax.text(0, max*1.8, 0, r"$\vec{k}$", color="k")

ax.set_xlim3d(-amp, amp)
ax.set_ylim3d(-100, 100)
ax.set_zlim3d(-amp, amp)

ani = animation.ArtistAnimation(fig, frames, interval=10, blit=True, repeat_delay=0)

print("Saving animation... This may take a couple minutes")
start = Time.time()
ani.save("em_wave.gif")
end = Time.time()
print("Saving finished in {:2.2f} min.".format((end-start)/60))
plt.show()
