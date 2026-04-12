from abc import ABC, abstractmethod


class TuoiKhongHopLe(Exception):
    pass


class BacKhongHopLe(Exception):
    pass


class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, t):
        if t < 18 or t > 65:
            raise TuoiKhongHopLe(f"Tuoi phai tu 18 den 65! Tuoi nhap: {t}")
        self._tuoi = t

    @property
    def ho_ten(self):
        return self._ho_ten

    @ho_ten.setter
    def ho_ten(self, ht):
        self._ho_ten = ht

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.mo_ta()} | {self._ho_ten} | {self._tuoi} tuoi | {self.gioi_tinh} | {self._dia_chi}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._ho_ten == other._ho_ten and self._tuoi == other._tuoi

    def __lt__(self, other):
        return self._ho_ten < other._ho_ten


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, b):
        if b < 1 or b > 10:
            raise BacKhongHopLe(f"Bac cong nhan phai tu 1 den 10! Bac nhap: {b}")
        self._bac = b

    def mo_ta(self):
        return f"[Cong Nhan] Bac {self._bac}"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def mo_ta(self):
        return f"[Ky Su] Nganh {self.nganh}"


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"[Nhan Vien] CV: {self.cong_viec}"


ds = [
    CongNhan("Nguyen A", 30, "Nam", "HN", 5),
    KySu("Tran B", 28, "Nu", "HCM", "CNTT"),
    NhanVien("Le C", 35, "Nam", "DN", "Ke toan")
]

print("===== DANH SACH (sorted theo ten ABC) =====")
for cb in sorted(ds):
    print(cb)

print()
ten = input("Nhap ten can tim: ")
kq = [cb for cb in ds if ten.lower() in str(cb).lower()]
if len(kq) == 0:
    print("Khong tim thay!")
else:
    print(f"Tim thay {len(kq)} can bo:")
    for cb in kq:
        print(cb)

print()
print("===== LUU FILE =====")
with open("canbo.txt", "w", encoding="utf-8") as f:
    for cb in ds:
        f.write(repr(cb) + "\n")
print("Da luu vao canbo.txt")

print()
print("===== DOC FILE =====")
with open("canbo.txt", "r", encoding="utf-8") as f:
    print(f.read())

print()
print("===== KIEM TRA EXCEPTION =====")
try:
    cb_loi = CongNhan("Test", 17, "Nam", "HN", 5)
except TuoiKhongHopLe as e:
    print("Loi tuoi:", e)

try:
    cb_loi2 = CongNhan("Test2", 25, "Nam", "HN", 11)
except BacKhongHopLe as e:
    print("Loi bac:", e)