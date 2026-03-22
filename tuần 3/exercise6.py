class NhanVien:
    LUONG_MAX = 50_000_000

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    def getTen(self): return self.__tenNhanVien
    def setTen(self, ten): self.__tenNhanVien = ten

    def getLuongCoBan(self): return self.__luongCoBan
    def setLuongCoBan(self, luong): self.__luongCoBan = luong

    def getHeSoLuong(self): return self.__heSoLuong
    def setHeSoLuong(self, heso): self.__heSoLuong = heso

    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    def inTTin(self):
        print(f"Tên: {self.__tenNhanVien}")
        print(f"Lương cơ bản: {self.__luongCoBan}")
        print(f"Hệ số lương: {self.__heSoLuong}")
        print(f"Lương thực tế: {self.tinhLuong()}")

    def tangLuong(self, delta):
        luong_moi = self.tinhLuong() + delta
        if luong_moi > NhanVien.LUONG_MAX:
            print("Lương vượt quá mức tối đa!")
            return False
        self.__luongCoBan += delta / self.__heSoLuong
        return True