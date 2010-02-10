# IPython log file

get_ipython().magic("run bessel.py")
x = np.arange(10)
x
x < 5
x [ x < 5 ]
x [ x < 5 ] = 0
x
x = np.arange(10)
x [ x < 3 or x> 7 ] = 0
x [ np.logical_or(x < 3, x> 7) ] = 0
x
x = linspace(0, 2*pi, 200)
y = sin(x)
z = arange(200)
mask = logical_and(z>100, z<150)
plot(y[mask],  x[mask])
figure()
plot(y[mask],  x[mask])
clf()
plot(x[mask],  y[mask])
close("all")
get_ipython().magic("run bessel.py")
close("all")
semilogy()
plot([1,2,3])
close("all")
#?plot
#?legend
close("all")
plot([1,2,3], '--', color='#554422')
x = linspace(0, 2*pi, 200)
y = sin(x)
err = 0.4
yu = y + err/2
yd = y - err/2
plot(x,y, lw=3,color='green')
fill_between(x, yu, yd, color='red', alpha=0.4)
plot(x,y, lw=3,color='green')
get_ipython().magic("logstart clase_0210_log.py")

rcParams.keys()
sorted(rcParams.keys())
plot(x,y)
rcParams['lines.linewidth'] = 4
plot(x,y)
get_ipython().system("ls -F ")
