"""Simple vector implementation."""

class Vector(object):
    def __init__(self, *components):
        """Initialize a vector."""
        if len(components)==1:
            # If we are given a single sequence, try to make it into a tuple to
            # support initialization with regular sequences.
            try:
                components = tuple(components[0])
            except TypeError:
                # This is the exception raised by tuple(x) if x is not iterable
                pass
        self.components = components

    def __eq__(self, other):
        return self.components == other.components

    def __str__(self):
        return 'Vector%s' % (self.components,)

    __repr__ = __str__

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        c = [x+y for x,y in zip(self.components, other.components)]
        return Vector(c)

    def  __mul__(self,  other):
        if isinstance(other, Vector):
            # Dot product
            return sum(x*y for x,y in zip(self.components, other.components))
        else:
            # Product with a scalar
            c = [other*x for x in self.components]
            return Vector(c)

    def __rmul__(self, other):
        return self.__mul__(other)
