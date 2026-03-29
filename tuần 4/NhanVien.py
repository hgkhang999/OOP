class NhanVien:
    LUONG_MAX = 50000000

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    def getTenNhanVien(self):
        return self.__tenNhanVien
    def setTenNhanVien(self, ten):
        self.__tenNhanVien = ten

    def getLuongCoBan(self):
        return self.__luongCoBan
    def setLuongCoBan(self, luong):
        self.__luongCoBan = luong

    def getHeSoLuong(self):
        return self.__heSoLuong
    def setHeSoLuong(self, heSo):
        self.__heSoLuong = heSo

    def tinhLuong(self):
        luong = self.__luongCoBan * self.__heSoLuong
        return luong

    def tangLuong(self, soTang):
        heSoMoi = self.__heSoLuong + soTang
        luongMoi = self.__luongCoBan * heSoMoi

        if luongMoi > NhanVien.LUONG_MAX:
            print("Khong the tang luong!")
            return False
        else:
            self.__heSoLuong = heSoMoi
            return True

    def inTTin(self):
        print("Ten nhan vien:", self.__tenNhanVien)
        print("Luong co ban:", self.__luongCoBan)
        print("He so luong:", self.__heSoLuong)
        print("Luong thuc nhan:", self.tinhLuong())


nv1 = NhanVien("Nguyen Van A", 5000000, 2.0)
nv1.inTTin()

print("---")
ketQua = nv1.tangLuong(1.5)
if ketQua == True:
    print("Tang luong thanh cong!")
    nv1.inTTin()

print("---")
nv1.tangLuong(10.0)