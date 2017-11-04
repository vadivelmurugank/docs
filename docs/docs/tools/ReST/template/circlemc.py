import numpy as np
from matplotlib.pyplot import figure, show
from matplotlib.patches import Arc
from matplotlib.cm import copper

fig = figure()
frame = fig.add_subplot(1,1,1)
n = 2000
x = np.random.random_sample(n)
y = np.random.random_sample(n)
radius = x**2 + y**2
In = (radius <= 1.0)
Out = (radius > 1.0)
frame.plot(x[In], y[In], 'g.')
frame.plot(x[Out], y[Out], 'r.')
arc = Arc((0,0), 2,2, 0,0, 90)
frame.add_patch(arc)
frame.imshow([[0, 0],[1,1]], interpolation='bicubic', cmap=copper,
             vmin=-0.5, vmax=0.5,
             extent=(frame.get_xlim()[0], frame.get_xlim()[1],
                     frame.get_ylim()[0], frame.get_ylim()[1]),
             alpha=1)

frame.set_xlim(0,1)
frame.set_ylim(0,1)
frame.set_aspect(1.0)
show()
