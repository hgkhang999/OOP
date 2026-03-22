import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

A = Point(3, 4)

bx = float(input("Nhập x của B: "))
by = float(input("Nhập y của B: "))
B = Point(bx, by)

C = Point(-B.x, -B.y)

d_BO = math.sqrt(B.x**2 + B.y**2)
d_AB = math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)

print(f"A({A.x}, {A.y})")
print(f"B({B.x}, {B.y})")
print(f"C({C.x}, {C.y})")
print(f"d(B, O) = {d_BO:.4f}")
print(f"d(A, B) = {d_AB:.4f}")