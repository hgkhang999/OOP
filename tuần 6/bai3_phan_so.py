from math import gcd


class MauSoBangKhong(Exception):
    pass


class PhanSo:
    def __init__(self, tu, mau):
        self.tu_so = tu
        self.mau_so = mau

    @property
    def tu_so(self):
        return self._tu_so

    @tu_so.setter
    def tu_so(self, t):
        self._tu_so = t

    @property
    def mau_so(self):
        return self._mau_so

    @mau_so.setter
    def mau_so(self, m):
        if m == 0:
            raise MauSoBangKhong("Mau so khong duoc bang 0!")
        self._mau_so = m

    def toi_gian(self):
        g = gcd(abs(self._tu_so), abs(self._mau_so))
        tu = self._tu_so // g
        mau = self._mau_so // g
        if mau < 0:
            tu = -tu
            mau = -mau
        return PhanSo(tu, mau)

    def is_toi_gian(self):
        g = gcd(abs(self._tu_so), abs(self._mau_so))
        return g == 1

    def __add__(self, other):
        tu = self._tu_so * other._mau_so + other._tu_so * self._mau_so
        mau = self._mau_so * other._mau_so
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu = self._tu_so * other._mau_so - other._tu_so * self._mau_so
        mau = self._mau_so * other._mau_so
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        tu = self._tu_so * other._tu_so
        mau = self._mau_so * other._mau_so
        return PhanSo(tu, mau).toi_gian()

    def __truediv__(self, other):
        tu = self._tu_so * other._mau_so
        mau = self._mau_so * other._tu_so
        return PhanSo(tu, mau).toi_gian()

    def __eq__(self, other):
        ps1 = self.toi_gian()
        ps2 = other.toi_gian()
        return ps1._tu_so == ps2._tu_so and ps1._mau_so == ps2._mau_so

    def __lt__(self, other):
        return self._tu_so * other._mau_so < other._tu_so * self._mau_so

    def __gt__(self, other):
        return self._tu_so * other._mau_so > other._tu_so * self._mau_so

    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps._tu_so, ps._mau_so))

    def __str__(self):
        ps = self.toi_gian()
        if ps._mau_so == 1:
            return str(ps._tu_so)
        return f"{ps._tu_so}/{ps._mau_so}"

    def __repr__(self):
        return f"PhanSo({self._tu_so}, {self._mau_so})"


ds = []
n = int(input("Nhap so luong phan so: "))
for i in range(n):
    print(f"Phan so thu {i + 1}:")
    tu = int(input("  Tu so: "))
    mau = int(input("  Mau so: "))
    try:
        ps = PhanSo(tu, mau)
        ds.append(ps)
    except MauSoBangKhong as e:
        print("Loi:", e)

print()
print("===== DANH SACH PHAN SO TOI GIAN =====")
for ps in ds:
    print(ps)

print()
print("===== SAP XEP TANG DAN =====")
for ps in sorted(ds):
    print(ps)

print()
if len(ds) >= 2:
    ps1 = ds[0]
    ps2 = ds[1]
    print(f"Tinh toan voi {ps1} va {ps2}:")
    print("Cong  :", ps1 + ps2)
    print("Tru   :", ps1 - ps2)
    print("Nhan  :", ps1 * ps2)
    print("Chia  :", ps1 / ps2)
    print("Bang nhau?", ps1 == ps2)

print()
print("===== KIEM TRA set() dung __hash__ =====")
ps_a = PhanSo(2, 4)
ps_b = PhanSo(1, 2)
print(f"{repr(ps_a)} va {repr(ps_b)} co gia tri bang nhau (2/4 = 1/2)")
tap_hop = set()
tap_hop.add(ps_a)
tap_hop.add(ps_b)
print("So phan tu trong set (neu hash dung thi = 1):", len(tap_hop))

print()
print("===== KIEM TRA EXCEPTION =====")
try:
    ps_loi = PhanSo(1, 0)
except MauSoBangKhong as e:
    print("Loi:", e)