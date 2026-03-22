class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

danh_sach = []

while True:
    ten = input("Nhập tên siêu nhân (Enter để dừng): ")
    if ten == "":
        break
    vu_khi = input("Vũ khí: ")
    mau_sac = input("Màu sắc: ")
    danh_sach.append(SieuNhan(ten, vu_khi, mau_sac))

print("\n=== Danh sách siêu nhân ===")
for sn in danh_sach:
    print(f"Tên: {sn.ten}, Vũ khí: {sn.vu_khi}, Màu sắc: {sn.mau_sac}")