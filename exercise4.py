class ConCho:
    def __init__(self, ten, mau_sac, giong, cam_xuc):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc

    def sua(self): print(f"{self.ten}: Gâu gâu!")
    def vay_duoi(self): print(f"{self.ten} vẫy đuôi!")
    def an(self): print(f"{self.ten} đang ăn.")
    def chay(self): print(f"{self.ten} đang chạy.")


class OTo:
    def __init__(self, hang, kich_thuoc, mau, gia):
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau = mau
        self.gia = gia

    def tang_toc(self): print(f"{self.hang} tăng tốc!")
    def giam_toc(self): print(f"{self.hang} giảm tốc!")
    def dam(self): print(f"{self.hang} đâm!")


class TaiKhoan:
    def __init__(self, ten_tk, so_tk, ngan_hang, so_du):
        self.ten_tk = ten_tk
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self.so_du = so_du

    def rut(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"Rút {so_tien}đ thành công. Số dư: {self.so_du}đ")
        else:
            print("Số dư không đủ!")

    def gui(self, so_tien):
        self.so_du += so_tien
        print(f"Gửi {so_tien}đ thành công. Số dư: {self.so_du}đ")

    def kiem_tra_so_du(self):
        print(f"Số dư tài khoản {self.so_tk}: {self.so_du}đ")