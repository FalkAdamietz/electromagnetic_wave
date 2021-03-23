#imports
from lib.imports import *

k=0.07
omega = 0.2
T = 2*np.pi / omega
dt = 0.1
max = 100
min = -max
amp = 100

fig = plt.figure()
ax = plt.axes(projection='3d')
ax._axis3don = False
ax.view_init(30, 30)


time = np.arange(0, T, dt)
N = len(time)
frames = []
dx = 20*max/(N-1)
x = np.arange(min, max, dx)

print("Creating animation...\n")
for i in tqdm.tqdm(range(N)):
    Ey = np.linspace(-100,100,1000)
    Ex = np.zeros_like(Ey)
    Ez = amp*np.sin(k*Ey-omega*time[i])/2

    My = np.linspace(-100,100,1000)
    Mz = np.zeros_like(My)
    Mx = amp*np.sin(k*My-omega*time[i])/2

    plot1, = ax.plot3D(Ex, Ey, Ez, 'red')
    plot2, = ax.plot3D(Mx, My, Mz, 'blue')

    anilist = [plot1, plot2]

    for xs in x:
        z = amp*np.sin(k*xs-omega*time[i])/2
        arrow = Arrow3D([0,0],[xs,xs],[0,z], mutation_scale=5, lw=1, arrowstyle="-|>", color="r")
        plotarrow = ax.add_artist(arrow)
        anilist.append(plotarrow)
        Y = amp*np.sin(k*xs-omega*time[i])/2
        arrow = Arrow3D([0,Y],[xs,xs],[0,0], mutation_scale=5, lw=1, arrowstyle="-|>", color="b")
        plotarrow = ax.add_artist(arrow)
        anilist.append(plotarrow)

    frames.append(anilist)


a = Arrow3D([0,0],[-max,max*1.3],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)

ax.set_xlim3d(-amp, amp)
ax.set_ylim3d(-100, 100)
ax.set_zlim3d(-amp, amp)


ani = animation.ArtistAnimation(fig, frames, interval=10, blit=True, repeat_delay=0)

#print("Saving animation... This may take a couple minutes")
#start = time.time()
#ani.save("em_wave.gif")
#end = time.time()
#print("Saving finished in {:2f} min.".format((end-start)/60))
plt.show()
