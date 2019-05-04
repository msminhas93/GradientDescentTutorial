from matplotlib.widgets import Slider	
from sympy import symbols
from sympy import diff
from sympy import solve
import sympy
import numpy as np
from sympy import lambdify
import matplotlib.pyplot as plt


def grad_descent_1d(lr=0.01,x0=2.7,n=10):
    # np.random.seed(3000)
#     x0=np.random.uniform(-3,3)
    x0 = x0
    # x0 = 2.8
    f = lambdify(x,y,'numpy')
    x_arr = np.arange(-3,3,0.1)
    y_arr = f(x_arr)
    lr=lr
    x_l = [x0]
    for i in range(int(n)):
        x0=x0-y1.evalf(subs={x:x0})*lr
        x_l.append(x0)
    x_l = np.array(x_l)    
    y_l = f(x_l)
    return x_arr,y_arr,x_l,y_l

x = symbols('x')
y = x**4+x**3-6*x**2
y1 = diff(y)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
lr=0.01
x0 = 2.8
x_arr,y_arr,x_l,y_l = grad_descent_1d(lr=0.01,x0 = 2.8,n=10)
ax.plot(x_arr,y_arr)
ax.plot(x_l[0],y_l[0],'kx',label='Random Initilization');
ax.plot(x_l[-1],y_l[-1],'yx',label='Stop Point');
ax.plot(x_l,y_l,'r-');
ax.legend()
ax.set_title(f'Gradient Descent 1D example');
textstr = '\n'.join([fr'$\rho = {lr:.7f}$',fr'Initial guess: {float(x_l[0]):.2f}',fr'Stop Point: {float(x_l[-1]):.2f}'])
props = dict(boxstyle='square', facecolor='white', alpha=0.5)
ax.text(0.05, 0.7, textstr, transform=ax.transAxes, fontsize=12,
		verticalalignment='top', bbox=props);

axcolor = 'lightgoldenrodyellow'
axlr = plt.axes([0.25, 0.03, 0.65, 0.03], facecolor=axcolor)
axx0 = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor=axcolor)
axnos = plt.axes([0.25, 0.09, 0.65, 0.03], facecolor=axcolor)
slr = Slider(axlr, 'Learning Rate', -5, 1, valinit=-3,valstep=0.1)
sx0 = Slider(axx0, 'Initial Guess', -3, 3, valinit=2.3,valstep=0.01)
sxnos = Slider(axnos, 'Number of iterations', 1, 50, valinit=10,valstep=1)


    

def update(val):
	ax.cla()
	lr = 10**slr.val
	slr.valtext.set_text(f'{lr:.4E}')
	n = sxnos.val
	x0 = sx0.val
	x_arr,y_arr,x_l,y_l = grad_descent_1d(lr=lr,x0 = x0,n=n)
	# plt.autoscale()
	ax.plot(x_arr,y_arr)
	ax.plot(x_l[0],y_l[0],'kx',label='Random Initilization');
	ax.plot(x_l[-1],y_l[-1],'yx',label='Stop Point');
	ax.plot(x_l,y_l,'r-');
	ax.legend()
	ax.set_title(f'Gradient Descent 1D example');
	textstr = '\n'.join([fr'$\rho = {lr:.7f}$',fr'Initial guess: {float(x_l[0]):.2f}',fr'Stop Point: {float(x_l[-1]):.2f}'])
	props = dict(boxstyle='square', facecolor='white', alpha=0.5)
	ax.text(0.05, 0.7, textstr, transform=ax.transAxes, fontsize=12,
			verticalalignment='top', bbox=props);

slr.on_changed(update)
sx0.on_changed(update)
sxnos.on_changed(update)

plt.show()