class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong
        self.luong_toi_da = luong_toi_da

    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da

    def xuat_thong_tin(self):
        print("Ma NV       :", self.ma_nv)
        print("Ho ten      :", self.ho_ten)
        print("Nam sinh    :", self.nam_sinh)
        print("Gioi tinh   :", self.gioi_tinh)
        print("Dia chi     :", self.dia_chi)
        print("He so luong :", self.he_so_luong)
        print("Luong toi da:", self.luong_toi_da)
        print("Luong nhan  :", self.tinh_luong(), "VND")


class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        NhanVien.__init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_ld = phu_cap_ld

    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da + self.phu_cap_ld

    def xuat_thong_tin(self):
        print("===== CONG TAC VIEN =====")
        NhanVien.xuat_thong_tin(self)
        print("Thoi han HD :", self.thoi_han_hd)
        print("Phu cap LD  :", self.phu_cap_ld, "VND")


class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        NhanVien.__init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri = vi_tri

    def xuat_thong_tin(self):
        print("===== NHAN VIEN CHINH THUC =====")
        NhanVien.xuat_thong_tin(self)
        print("Vi tri      :", self.vi_tri)


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau, phu_cap_ql):
        NhanVien.__init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bat_dau = ngay_bat_dau
        self.phu_cap_ql = phu_cap_ql

    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da + self.phu_cap_ql

    def xuat_thong_tin(self):
        print("===== TRUONG PHONG =====")
        NhanVien.xuat_thong_tin(self)
        print("Ngay bat dau:", self.ngay_bat_dau)
        print("Phu cap QL  :", self.phu_cap_ql, "VND")


ctv = CongTacVien("CTV001", "Nguyen Van A", 2000, "Nam", "Ha Noi", 1.5, 5000000, "6 thang", 500000)
nvct = NhanVienChinhThuc("NV001", "Tran Thi B", 1995, "Nu", "HCM", 2.0, 5000000, "Ky su phan mem")
tp = TruongPhong("TP001", "Le Van C", 1985, "Nam", "Da Nang", 3.0, 5000000, "01/01/2020", 2000000)

ctv.xuat_thong_tin()
print()
nvct.xuat_thong_tin()
print()
tp.xuat_thong_tin()