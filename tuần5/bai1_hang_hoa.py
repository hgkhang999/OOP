class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def xuat_thong_tin(self):
        print("Ma hang:", self.ma_hang)
        print("Ten hang:", self.ten_hang)
        print("Nha san xuat:", self.nha_sx)
        print("Gia:", self.gia, "VND")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        HangHoa.__init__(self, ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat_thong_tin(self):
        print("===== HANG DIEN MAY =====")
        HangHoa.xuat_thong_tin(self)
        print("Bao hanh:", self.tg_baohanh, "thang")
        print("Dien ap:", self.dien_ap, "V")
        print("Cong suat:", self.cong_suat, "W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        HangHoa.__init__(self, ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat_thong_tin(self):
        print("===== HANG SANH SU =====")
        HangHoa.xuat_thong_tin(self)
        print("Loai nguyen lieu:", self.loai_nguyen_lieu)


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        HangHoa.__init__(self, ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def xuat_thong_tin(self):
        print("===== HANG THUC PHAM =====")
        HangHoa.xuat_thong_tin(self)
        print("Ngay san xuat:", self.ngay_sx)
        print("Ngay het han:", self.ngay_het_han)


sp1 = HangDienMay("tucha01", "Bo PC", "Tay", 15000000, 12, 220, 500)
sp2 = HangSanhSu("lgbt01", "Lang gom Bat Trang", "LGBT", 250000, "Dat set")
sp3 = HangThucPham("datucho01", "Ba mia", "Toctay", 5000, "01/04/2025", "01/07/2025")

sp1.xuat_thong_tin()
print()
sp2.xuat_thong_tin()
print()
sp3.xuat_thong_tin()