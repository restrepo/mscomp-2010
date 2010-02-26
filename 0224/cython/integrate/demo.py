import pyximport; pyximport.install()

import integ, integ2

print 'integ :',integ.integrate_f(0, 2, 10000)
print 'integ2:',integ2.integrate_f(0, 2, 10000)
