class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def xuat_thong_tin(self):
        print("Ho ten   :", self.ho_ten)
        print("Tuoi     :", self.tuoi)
        print("Gioi tinh:", self.gioi_tinh)
        print("Dia chi  :", self.dia_chi)


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def xuat_thong_tin(self):
        print("== CONG NHAN ==")
        CanBo.xuat_thong_tin(self)
        print("Bac      :", self.bac)


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def xuat_thong_tin(self):
        print("== KY SU ==")
        CanBo.xuat_thong_tin(self)
        print("Nganh DT :", self.nganh_dao_tao)


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def xuat_thong_tin(self):
        print("== NHAN VIEN ==")
        CanBo.xuat_thong_tin(self)
        print("Cong viec:", self.cong_viec)


class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, can_bo):
        self.danh_sach.append(can_bo)
        print(">> Da them thanh cong:", can_bo.ho_ten)

    def tim_kiem(self, ho_ten):
        ket_qua = []
        for cb in self.danh_sach:
            if ho_ten.lower() in cb.ho_ten.lower():
                ket_qua.append(cb)
        
        if len(ket_qua) == 0:
            print("Khong tim thay can bo nao!")
        else:
            print("Tim thay", len(ket_qua), "can bo:")
            print()
            for cb in ket_qua:
                cb.xuat_thong_tin()
                print()

    def hien_thi(self):
        if len(self.danh_sach) == 0:
            print("Danh sach trong!")
        else:
            print("===== DANH SACH CAN BO =====")
            for i in range(len(self.danh_sach)):
                print("--- Can bo", i + 1, "---")
                self.danh_sach[i].xuat_thong_tin()
                print()


def menu():
    ql = QLCB()

    while True:
        print("====== QUAN LY CAN BO ======")
        print("1. Them moi can bo")
        print("2. Tim kiem theo ho ten")
        print("3. Hien thi danh sach")
        print("4. Thoat")
        print("============================")

        lua_chon = input("Chon chuc nang (1-4): ")

        if lua_chon == "1":
            print("Chon loai can bo:")
            print("1. Cong nhan")
            print("2. Ky su")
            print("3. Nhan vien")
            loai = input("Chon loai (1-3): ")

            ho_ten = input("Ho ten: ")
            tuoi = int(input("Tuoi: "))
            gioi_tinh = input("Gioi tinh (nam/nu/khac): ")
            dia_chi = input("Dia chi: ")

            if loai == "1":
                bac = int(input("Bac (1-10): "))
                cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
            elif loai == "2":
                nganh = input("Nganh dao tao: ")
                cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
            elif loai == "3":
                cong_viec = input("Cong viec: ")
                cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
            else:
                print("Loai khong hop le!")
                continue

            ql.them_moi(cb)

        elif lua_chon == "2":
            ten = input("Nhap ho ten can tim: ")
            ql.tim_kiem(ten)

        elif lua_chon == "3":
            ql.hien_thi()

        elif lua_chon == "4":
            print("Tam biet!")
            break

        else:
            print("Vui long chon 1-4!")

        print()


menu()