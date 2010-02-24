def log(fname):
    def log_deco(func):        

        def deco_func(*a):
            fh = open(fname,'a')
            print >> fh, "Se llamo", func.func_name,"con argumento",a
            fh.close()
            return func(*a)

        return deco_func
    
    return log_deco

def trace(func):
    
    def deco_func(*a):
        print "Se llamo", func.func_name,"con argumento",str(a)[1:-1].rstrip(',')        
        return func(*a)

    return deco_func

@log('fx.log')
def f(x):
    return x+2

@trace
def f2(x):
    return x+2

@log('fy.log')
def g(x,y):
    return x+y


if __name__ == '__main__':
    print 'f'
    f(3)
    print 'g'
    g(3,4)
