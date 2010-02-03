#!/usr/bin/env python
"""Simple demonstration of Python's arbitrary-precision integers.

Compute pi using n terms of Wallis' product.

Wallis' formula approximates pi as

   pi(n) = 2 \prod_{i=1}^{n}\frac{4i^2}{4i^2-1}.

"""

# We need exact division between integers as the default, without manual
# conversion to float b/c we'll be dividing numbers too big to be represented
# in floating point.
from __future__ import division
