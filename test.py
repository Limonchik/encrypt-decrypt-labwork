from utilities import *

from modular_inverse import *

def swapv(a222, b222):
    return b222, a222


for i in range(10):
    print(a1, b1, a2, b2)
    a1 = modular_inverse(a2 * a1, 26)
    b1 = modular_inverse(b2 * b1, 26)
    swapv(a1, a2)
    swapv(b1, b2)