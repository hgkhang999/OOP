class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Tên: {self.ten}, Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}"

sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")

print(sieu_nhan_A)
print(sieu_nhan_B)
