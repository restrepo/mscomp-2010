# IPython log file

get_ipython().magic("logstart clase_0217_log.py")

get_ipython().system("ls -F -F -o --color ")
get_ipython().magic("run tdd")
get_ipython().magic("run tdd")
get_ipython().system("nosetests ")
get_ipython().system("nosetests --with-doctest tdd.py")
np.test()
get_ipython().magic("run tdd")
get_ipython().system("nosetests --with-doctest -x tdd.py")
get_ipython().system("nosetests --help")
get_ipython().system("nosetests --help | les")
get_ipython().system("nosetests --help | less")
get_ipython().system("nosetests --with-doctest -x --pdb --pdb-failures  tdd.py")
get_ipython().system("nosetests --with-doctest -x --pdb --pdb-failures  tdd.py")
get_ipython().system("nosetests --with-doctest -x --pdb --pdb-failures  tdd.py")
get_ipython().system("nosetests --with-doctest  tdd.py")
get_ipython().system("nosetests --with-doctest  tdd.py:test_failing")
get_ipython().system("nosetests --with-doctest  tdd.py:test_failing")
get_ipython().system("nosetests --with-doctest  tdd.py")
get_ipython().system("ls -F -F -o --color ")
get_ipython().magic("run recarr_simple")
#?loadtxt 
#?np.load*
#?np.*txt*
#?np.*save*
tab.shape
tab
tab['lat']
np.empty(5, dtype=dt)
np.zeros(5, dtype=dt)
_30.byteswap ()
get_ipython().magic("run recarr_simple")
tab.view (np.rec)
tab.view (np.recarray)
tt = tab.view (np.recarray)
tt.tab
tt.station
tt.dtype
tt.fields
tt.field 
#?mlab.csv2rec 
c = mlab.csv2rec ('crox.csv')
c.shape
c.dtype
c[0].date
#?np.argsort 
s = mlab.csv2rec ('crox.csv')
s.sort()
plot(s.date, s.adj_close)
gcf().autofmt_xdate()
draw()
dv = s.volume*s.close
dv.min()
dv.max()
dv.argmax ()
mask = dv > 0.5*dv.max()
figure()
plot(s.date, dv)
gcf().autofmt_xdate()
draw()
ax = gca()
plot(s.date, dv)
gcf().autofmt_xdate()
ax = gca()
ax.scatter(s.date[mask], dv[mask], color='r',zorder=10)
draw()
get_ipython().system("clear ")
c = mlab.csv2rec ('crox.csv')
c.sort()
close("all")
s = c
plot(s.date, s.adj_close)
#?s.sort 
s.sort(order='adj_close')
plot(s.date, s.adj_close)
close("all")
plot(s.date, s.adj_close)
scatter(s.date, s.adj_close)
dv = s.volume*s.close
dv.mean()
dv.max()
d.argmax()
dv.argmax()
s.sort()
dv = s.volume*s.close
dv.argmax()
plot(s.date, dv)
gcf().autofmt_xdate()
draw()
mask = dv > 0.5*dv.max()
mask
scatter(s.date[mask], s.dv[mask], color='r')
scatter(s.date[mask], dv[mask], color='r')
class Simple: pass
s = Simple()
s.x = 1
s2 = Simple()
s.x
s2.x
a = [1,2,3]
a = list(1,2,3)
a = list((1,2,3)
)
class Simple:
    def hola(self, x):
        print "Hola,",x
s = Simple()
s.hola ('hi')
class Simple:
    def __str__(self):
        return "Objeto simple"
s2 = Simple()
print(s)
print(s2)
