from abc import ABC, abstractmethod


class GiaKhongHopLe(Exception):
    pass


class MaHangTrungLap(Exception):
    pass


class HangHoa(ABC):
    _ds_ma_hang = []

    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        if ma_hang in HangHoa._ds_ma_hang:
            raise MaHangTrungLap(f"Ma hang '{ma_hang}' da ton tai!")
        HangHoa._ds_ma_hang.append(ma_hang)

        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self.gia = gia

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, gia_moi):
        if gia_moi < 0:
            raise GiaKhongHopLe(f"Gia khong duoc am! Gia nhap vao: {gia_moi}")
        self._gia = gia_moi

    @abstractmethod
    def xuat_thong_tin(self):
        pass

    @abstractmethod
    def loai_hang(self):
        pass

    def __str__(self):
        return f"[{self._ma_hang}] {self._ten_hang} - {self._gia} VND"

    def __eq__(self, other):
        return self._ma_hang == other._ma_hang

    def __lt__(self, other):
        return self._gia < other._gia

    def __hash__(self):
        return hash(self._ma_hang)


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        HangHoa.__init__(self, ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def loai_hang(self):
        return "Hang Dien May"

    def xuat_thong_tin(self):
        print("===== HANG DIEN MAY =====")
        print("Ma hang:", self._ma_hang)
        print("Ten hang:", self._ten_hang)
        print("Nha san xuat:", self._nha_sx)
        print("Gia:", self._gia, "VND")
        print("Bao hanh:", self.tg_baohanh, "thang")
        print("Dien ap:", self.dien_ap, "V")
        print("Cong suat:", self.cong_suat, "W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        HangHoa.__init__(self, ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def loai_hang(self):
        return "Hang Sanh Su"

    def xuat_thong_tin(self):
        print("===== HANG SANH SU =====")
        print("Ma hang:", self._ma_hang)
        print("Ten hang:", self._ten_hang)
        print("Nha san xuat:", self._nha_sx)
        print("Gia:", self._gia, "VND")
        print("Loai nguyen lieu:", self.loai_nguyen_lieu)


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        HangHoa.__init__(self, ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def loai_hang(self):
        return "Hang Thuc Pham"

    def xuat_thong_tin(self):
        print("===== HANG THUC PHAM =====")
        print("Ma hang:", self._ma_hang)
        print("Ten hang:", self._ten_hang)
        print("Nha san xuat:", self._nha_sx)
        print("Gia:", self._gia, "VND")
        print("Ngay san xuat:", self.ngay_sx)
        print("Ngay het han:", self.ngay_het_han)


ds = []

try:
    sp1 = HangDienMay("tucha01", "Bo PC", "Tay", 15000000, 12, 220, 500)
    sp2 = HangSanhSu("lgbt01", "Lang gom Bat Trang", "LGBT", 250000, "Dat set")
    sp3 = HangThucPham("datucho01", "Ba mia", "Toctay", 5000, "01/04/2025", "01/07/2025")
    ds.append(sp1)
    ds.append(sp2)
    ds.append(sp3)
except GiaKhongHopLe as e:
    print("Loi gia:", e)
except MaHangTrungLap as e:
    print("Loi ma hang:", e)

for sp in ds:
    sp.xuat_thong_tin()
    print()

print("===== IN BANG __str__ =====")
for sp in ds:
    print(sp)

print()
print("===== SAP XEP THEO GIA =====")
ds_sorted = sorted(ds)
for sp in ds_sorted:
    print(sp)

print()
print("===== KIEM TRA __eq__ =====")
sp_test = HangThucPham("test01", "Test", "Test", 5000, "01/01/2025", "01/01/2026")
print("sp3 == sp_test (gia bang nhau nhung ma khac):", sp3 == sp_test)
print("sp3 == sp3:", sp3 == sp3)

print()
print("===== KIEM TRA set() dung __hash__ =====")
tap_hop = set(ds)
tap_hop.add(sp1)
print("So luong phan tu trong set (khong trung):", len(tap_hop))

print()
print("===== LUU FILE =====")
with open("danh_sach_hang_hoa.txt", "w", encoding="utf-8") as f:
    for sp in ds:
        f.write(str(sp) + "\n")
print("Da luu vao file danh_sach_hang_hoa.txt")

print()
print("===== DOC FILE =====")
with open("danh_sach_hang_hoa.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
    print(noi_dung)