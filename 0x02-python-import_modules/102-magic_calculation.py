#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        z = add(a, b)
        for j in range(4, 6):
            z = add(z, j)
        return z
    else:
        return sub(a, b)
    return 0
