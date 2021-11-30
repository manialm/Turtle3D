# if:
# a0*x + b0*y = c0
# a1*x + b1*y = c1
# returns x, y
def solve(a0, b0, c0, a1, b1, c1):
    det = a0 * b1 - a1 * b0
    if not det:
        return 0, (c0 / b0 if b0 else 0)
    x = b1 * c0 - b0 * c1
    y = -a1 * c0 + a0 * c1
    return x / det, y / det
