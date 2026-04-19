import json
import os

# --- Cac lop can bo (copy tu bai truoc, them to_dict va from_dict) ---

class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, loai):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.loai = loai  # de biet loai khi load lai

    def to_dict(self):
        return {
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "loai": self.loai
        }

    # ham nay se duoc override o lop con
    def from_dict(d):
        pass

    def __str__(self):
        return f"[{self.loai}] {self.ho_ten} | Tuoi: {self.tuoi} | {self.gioi_tinh} | {self.dia_chi}"


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        # goi __init__ cua lop cha
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, "CongNhan")
        self.bac = bac  # bac tho

    def to_dict(self):
        d = CanBo.to_dict(self)
        d["bac"] = self.bac
        return d

    def from_dict(d):
        return CongNhan(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["bac"])

    def tinh_luong(self):
        return self.bac * 1500000  # gia su moi bac la 1.5tr

    def __str__(self):
        return CanBo.__str__(self) + f" | Bac: {self.bac} | Luong: {self.tinh_luong()} VND"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, "KySu")
        self.nganh = nganh

    def to_dict(self):
        d = CanBo.to_dict(self)
        d["nganh"] = self.nganh
        return d

    def from_dict(d):
        return KySu(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["nganh"])

    def tinh_luong(self):
        return 8000000  # ky su luong co dinh tam tinh vay

    def __str__(self):
        return CanBo.__str__(self) + f" | Nganh: {self.nganh} | Luong: {self.tinh_luong()} VND"


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        CanBo.__init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, "NhanVien")
        self.cong_viec = cong_viec

    def to_dict(self):
        d = CanBo.to_dict(self)
        d["cong_viec"] = self.cong_viec
        return d

    def from_dict(d):
        return NhanVien(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["cong_viec"])

    def tinh_luong(self):
        return 5000000

    def __str__(self):
        return CanBo.__str__(self) + f" | Cong viec: {self.cong_viec} | Luong: {self.tinh_luong()} VND"


# YEU CAU 1: Doc du lieu tu file canbo.csv

def doc_file_csv(ten_file):
    danh_sach = []
    try:
        f = open(ten_file, "r", encoding="utf-8")
        # bo dong dau tien (header)
        dong_dau = f.readline()
        for dong in f:
            dong = dong.strip()
            if dong == "":
                continue
            # tach cac cot
            cot = dong.split(",")
            # kiem tra so cot co dung khong
            if len(cot) < 6:
                print("  [Canh bao] Dong nay bi loi dinh dang, bo qua:", dong)
                continue
            try:
                ho_ten = cot[0].strip()
                tuoi = int(cot[1].strip())
                gioi_tinh = cot[2].strip()
                dia_chi = cot[3].strip()
                loai = cot[4].strip()
                them_info = cot[5].strip()

                # tao doi tuong tuy theo loai
                if loai == "CongNhan":
                    bac = int(them_info)
                    cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
                elif loai == "KySu":
                    cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, them_info)
                elif loai == "NhanVien":
                    cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, them_info)
                else:
                    print("  [Canh bao] Khong biet loai:", loai, "- bo qua")
                    continue

                danh_sach.append(cb)

            except ValueError as e:
                print("  [Loi] Du lieu khong hop le:", e, "- dong:", dong)

        f.close()

    except FileNotFoundError:
        print("[Loi] Khong tim thay file:", ten_file)

    return danh_sach


# YEU CAU 2: Luu vao dict voi key la ho ten

class QuanLyCanBo:
    def __init__(self):
        # dict luu tru: key = ho_ten, value = doi tuong
        self.ds = {}

    def them(self, cb):
        # them can bo vao dict
        if cb.ho_ten in self.ds:
            print("  [Thong bao] Da ton tai can bo:", cb.ho_ten, "- ghi de!")
        self.ds[cb.ho_ten] = cb
        print("  Da them:", cb.ho_ten)
        self.luu_json()  # yeu cau 4: tu dong luu sau moi thao tac

    def xoa(self, ho_ten):
        if ho_ten in self.ds:
            del self.ds[ho_ten]
            print("  Da xoa:", ho_ten)
            self.luu_json()
        else:
            print("  [Loi] Khong tim thay:", ho_ten)

    def tim_theo_ho_ten(self, ho_ten):
        if ho_ten in self.ds:
            return self.ds[ho_ten]
        else:
            print("  Khong tim thay ai ten:", ho_ten)
            return None

    def tim_theo_loai(self, loai):
        # loai: CongNhan / KySu / NhanVien
        ket_qua = []
        for ten in self.ds:
            cb = self.ds[ten]
            if cb.loai == loai:
                ket_qua.append(cb)
        return ket_qua

    def in_3_cao_nhat(self):
        # sap xep theo luong giam dan roi lay 3 nguoi dau
        tat_ca = list(self.ds.values())
        # sort bang cach viet vong lap - chua biet dung sorted() nen lam thu cong
        # dung bubble sort cho don gian
        n = len(tat_ca)
        for i in range(n):
            for j in range(n - i - 1):
                if tat_ca[j].tinh_luong() < tat_ca[j+1].tinh_luong():
                    tam = tat_ca[j]
                    tat_ca[j] = tat_ca[j+1]
                    tat_ca[j+1] = tam

        print("\n--- TOP 3 CAN BO BAC/LUONG CAO NHAT ---")
        dem = 0
        for cb in tat_ca:
            if dem >= 3:
                break
            print(f"  {dem+1}. {cb}")
            dem += 1

    # YEU CAU 3: Luu/tai JSON

    def luu_json(self):
        ten_file = "canbo.json"
        try:
            danh_sach_dict = []
            for ten in self.ds:
                danh_sach_dict.append(self.ds[ten].to_dict())
            f = open(ten_file, "w", encoding="utf-8")
            # ensure_ascii=False de tieng Viet hien dung
            json.dump(danh_sach_dict, f, ensure_ascii=False, indent=2)
            f.close()
            # print("  [Da luu JSON]")  # tat di cho do output sach
        except Exception as e:
            print("  [Loi khi luu JSON]:", e)

    def tai_json(self):
        ten_file = "canbo.json"
        try:
            f = open(ten_file, "r", encoding="utf-8")
            danh_sach_dict = json.load(f)
            f.close()

            self.ds = {}  # xoa het di truoc
            for d in danh_sach_dict:
                loai = d.get("loai", "")
                # khoi phuc dung loai doi tuong
                if loai == "CongNhan":
                    cb = CongNhan.from_dict(d)
                elif loai == "KySu":
                    cb = KySu.from_dict(d)
                elif loai == "NhanVien":
                    cb = NhanVien.from_dict(d)
                else:
                    print("  [Canh bao] Loai la:", loai)
                    continue
                self.ds[cb.ho_ten] = cb

            print(f"  [Da tai JSON] {len(self.ds)} can bo.")
        except FileNotFoundError:
            print("  [Thong bao] Chua co file canbo.json, bat dau moi.")
        except Exception as e:
            print("  [Loi khi tai JSON]:", e)

    # YEU CAU 4: Menu CLI

    def chay_menu(self):
        # load du lieu cu truoc khi bat dau
        self.tai_json()

        while True:
            print("\n========== QUAN LY CAN BO ==========")
            print("1. Doc du lieu tu canbo.csv")
            print("2. Them can bo moi")
            print("3. Xoa can bo")
            print("4. Tim theo ho ten")
            print("5. Tim theo loai")
            print("6. In top 3 luong cao nhat")
            print("7. Hien thi tat ca")
            print("0. Thoat")
            print("=====================================")

            lua_chon = input("Chon: ").strip()

            if lua_chon == "1":
                ten_file = input("Nhap ten file csv (mac dinh: canbo.csv): ").strip()
                if ten_file == "":
                    ten_file = "canbo.csv"
                ds_doc = doc_file_csv(ten_file)
                for cb in ds_doc:
                    self.them(cb)
                print(f"  Da doc {len(ds_doc)} can bo tu file.")

            elif lua_chon == "2":
                print("Chon loai: 1-CongNhan  2-KySu  3-NhanVien")
                loai_chon = input("Loai: ").strip()
                ho_ten = input("Ho ten: ").strip()
                try:
                    tuoi = int(input("Tuoi: ").strip())
                except:
                    print("  Tuoi phai la so!")
                    continue
                gioi_tinh = input("Gioi tinh: ").strip()
                dia_chi = input("Dia chi: ").strip()

                if loai_chon == "1":
                    try:
                        bac = int(input("Bac tho: ").strip())
                    except:
                        print("  Bac phai la so!")
                        continue
                    cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
                elif loai_chon == "2":
                    nganh = input("Nganh: ").strip()
                    cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
                elif loai_chon == "3":
                    cong_viec = input("Cong viec: ").strip()
                    cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
                else:
                    print("  Khong hop le!")
                    continue
                self.them(cb)

            elif lua_chon == "3":
                ten = input("Nhap ho ten can xoa: ").strip()
                self.xoa(ten)

            elif lua_chon == "4":
                ten = input("Nhap ho ten can tim: ").strip()
                ket_qua = self.tim_theo_ho_ten(ten)
                if ket_qua != None:
                    print("  Ket qua:", ket_qua)

            elif lua_chon == "5":
                print("Loai: CongNhan / KySu / NhanVien")
                loai = input("Nhap loai: ").strip()
                ket_qua = self.tim_theo_loai(loai)
                if len(ket_qua) == 0:
                    print("  Khong co ai thuoc loai:", loai)
                else:
                    for cb in ket_qua:
                        print(" ", cb)

            elif lua_chon == "6":
                self.in_3_cao_nhat()

            elif lua_chon == "7":
                if len(self.ds) == 0:
                    print("  Danh sach trong!")
                else:
                    print(f"\n--- DANH SACH ({len(self.ds)} nguoi) ---")
                    for ten in self.ds:
                        print(" ", self.ds[ten])

            elif lua_chon == "0":
                print("Tam biet!")
                break

            else:
                print("  Khong hop le, chon lai di!")


# Tao file CSV mau de test
def tao_file_csv_mau():
    if not os.path.exists("canbo.csv"):
        noi_dung = """ho_ten,tuoi,gioi_tinh,dia_chi,loai,bac_nganh_congviec
Nguyen Van A,30,Nam,Ha Noi,CongNhan,3
Tran Thi B,25,Nu,HCM,KySu,CNTT
Le Van C,40,Nam,Da Nang,NhanVien,Ke toan
Pham Thi D,28,Nu,Can Tho,CongNhan,5
Hoang Van E,35,Nam,Ha Noi,KySu,Dien tu
Vu Thi F,32,Nu,HCM,NhanVien,Nhan su
"""
        f = open("canbo.csv", "w", encoding="utf-8")
        f.write(noi_dung)
        f.close()
        print("[Da tao file canbo.csv mau de test]")


# Chay chuong trinh 
if __name__ == "__main__":
    tao_file_csv_mau()
    ql = QuanLyCanBo()
    ql.chay_menu()