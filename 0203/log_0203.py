# IPython log file

get_ipython().magic("colors lightbg")
#?
get_ipython().magic("magic ")
get_ipython().magic("quickref ")
#?edit
get_ipython().magic("magic ")
get_ipython().magic("lsmagic ")
import math
#?edit
#?edit?
#?math.sin
#?math.sin?
1+1
#[Out]# 2
print("hello")
_14
#[Out]# 2
_15
_
#[Out]# 2
_i14
#[Out]# u'1+1\n'
import math
get_ipython().system("ls -F ")
get_ipython().magic("cd ")
get_ipython().magic("cd -")
get_ipython().system("cleare")
get_ipython().system("clear")
get_ipython().system("cleare")
x = 1
get_ipython().system("echo x")
get_ipython().system("echo $x")
get_ipython().system("ls -F ")
#?%run 
x
#[Out]# 1
get_ipython().magic("run qsort")
get_ipython().magic("run qsort")
x
#[Out]# 'hola'
y = 1
get_ipython().magic("run qsort")
y
#[Out]# 1
get_ipython().magic("run -i qsort")
import qsort
import qsort
qsort.x
#[Out]# 'hola'
import qsort
qsort.x
#[Out]# 'hola'
reload(qsort)
#[Out]# <module 'qsort' from 'qsort.py'>
qsort.x
#[Out]# 'hola python'
qsort.__name__
#[Out]# 'qsort'
get_ipython().system("clear ")
get_ipython().magic("run qsort")
reload(qsort)
#[Out]# <module 'qsort' from 'qsort.py'>
del qsort
a = [1,2,3]
a
#[Out]# [1, 2, 3]
#?a
#?%logstop 
#?%logstart 
a
#[Out]# [1, 2, 3]
#?a.append 
a.append (99)
a
#[Out]# [1, 2, 3, 99]
a.append ('hola udea')
a
#[Out]# [1, 2, 3, 99, 'hola udea']
a.append (.7878)
a
#[Out]# [1, 2, 3, 99, 'hola udea', 0.78779999999999994]
len(a)
#[Out]# 6
a[0]
#[Out]# 1
a[-1]
#[Out]# 0.78779999999999994
a[2:4]
#[Out]# [3, 99]
a[2:]
#[Out]# [3, 99, 'hola udea', 0.78779999999999994]
a[:4]
#[Out]# [1, 2, 3, 99]
a[:-3]
#[Out]# [1, 2, 3]
a
#[Out]# [1, 2, 3, 99, 'hola udea', 0.78779999999999994]
import  numpy as np
#?np.random.randint 
np.random.randint(0, 10, 100)
#[Out]# array([5, 7, 6, 9, 1, 2, 3, 1, 7, 7, 8, 2, 1, 6, 5, 8, 9, 9, 5, 1, 8, 5, 0,
#[Out]#        5, 6, 9, 3, 0, 0, 5, 9, 3, 3, 8, 7, 1, 8, 9, 9, 6, 5, 1, 7, 6, 8, 6,
#[Out]#        2, 9, 7, 2, 3, 2, 5, 0, 2, 6, 0, 1, 3, 5, 7, 7, 3, 6, 7, 6, 7, 2, 4,
#[Out]#        4, 3, 6, 4, 6, 5, 6, 8, 7, 9, 6, 6, 1, 0, 2, 7, 8, 6, 2, 8, 9, 3, 7,
#[Out]#        1, 4, 9, 2, 8, 3, 7, 5])
[3,4] + [4,5]
#[Out]# [3, 4, 4, 5]
[3,4] + [5] +  [4,5]
#[Out]# [3, 4, 5, 4, 5]
import  numpy as np
import random
get_ipython().magic("run qsort")
a
#[Out]# [1, 2, 3, 99, 'hola udea', 0.78779999999999994]
#?a.remove 
#?a.pop 
a.pop(3)
#[Out]# 99
a
#[Out]# [1, 2, 3, 'hola udea', 0.78779999999999994]
[3,4] + 5 +  [4,5]
[3,4] + [5] +  [4,5]
#[Out]# [3, 4, 5, 4, 5]
import  sys
get_ipython().magic("run qsort")
get_ipython().magic("run qsort")
get_ipython().magic("run qsort")
quicksort ([1,2,3])
#[Out]# [1, 2, 3]
quicksort ([1,2,4,3])
#[Out]# [1, 2, 3, 4]
quicksort ([1])
#[Out]# [1]
quicksort ([\])
quicksort ([])
#[Out]# []
quicksort ([4,5,3,2,1])
#[Out]# [1, 2, 3, 4, 5]
quicksort ([4,5,3,,77,23,11,2,1])
quicksort ([4,5,3,77,23,11,2,1])
#[Out]# [1, 2, 3, 4, 5, 11, 23, 77]
