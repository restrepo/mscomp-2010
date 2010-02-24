class count3(object):

    def __init__(self):
        self.count = -1
    
    def __iter__(self):
        print 'Iter llamado'
        return self

    def next(self):
        self.count += 1
        if self.count >=3:
            raise StopIteration()
        
        return self.count 


def count(n, sentinel=None):
    for i in range(n):
        if i==sentinel:
            break
        
        yield i

def c3():
    yield 0
    yield 1
    yield 2
    
