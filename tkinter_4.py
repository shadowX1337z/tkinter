import tkinter,time,webbrowser,subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import font
root = Tk()
root.geometry("500x400")
root.title("Đăng kí")
root.config(bg = "#00ffd5")
root.resizable(width=False,height=False)

#===canvas===
nen_desktop_dangki = Canvas(root,width = 400,height = 300,bg="#ADFFF5",highlightthickness = 0)
nen_desktop_dangki.place(x=50,y=30)


loi_thong_tin_name = Label(nen_desktop_dangki, text="", fg="#ff0000", bg="#ADFFF5")
loi_thong_tin_name.place(x=20,y=100)

loi_thong_tin_password = Label(nen_desktop_dangki, text="", fg="#ff0000", bg="#ADFFF5")
loi_thong_tin_password.place(x=20,y=200)

# === HIỆU ỨNG NÚT ===
def trong_nut_dang_ki(event):
    dang_ky_button.config(bg="#32d424")
def trong_nut_dang_nhap(event):
    dang_nhap_button.config(bg="#32d424")
def ra_ngoai_nut_dang_ki(event):
        dang_ky_button.config(bg="#00ff22")
def ra_ngoai_nut_dang_nhap(event):
        dang_nhap_button.config(bg="#00ff22")
def inbox_khoa():
     webbrowser.open("https://www.facebook.com/pham.anh.khoa.842202#")

# === CÁC THÀNH PHẦN GIAO DIỆN ===
dang_ki_head = Label(root,text="ĐĂNG KÍ",fg="#2200ff",bg="#ADFFF5",font=("Arial",20))
dang_ky_ten_head = Label(root,text="Nhập tên tại đây",fg="#00407d",bg="#ADFFF5")
dang_ky_password_head = Label(root,text="Nhập mật khẩu tại đây",fg="#00407d",bg="#ADFFF5")
dang_ky_ten = Entry(root,width=35,font=("Arial",14))
dang_ky_password = Entry(root,width=35,font=("Arial",14),show = "*")
ver_listbox = Listbox(root,height=1)
ver_listbox.insert(END,"inbox admin")

# === DANH SÁCH NGƯỜI DÙNG ===
luu_list_user = {}

def luu_info():
    name = dang_ky_ten.get()
    password = dang_ky_password.get()
    if  name == "" and password == "":
        loi_thong_tin_name.config(text="Vui lòng điền vào ô này")
        loi_thong_tin_name.config(text="Vui lòng điền vào ô này")
        return False

    # Kiểm tra tên
    if name == "":
        loi_thong_tin_name.config(text="Vui lòng điền vào ô này")
        return False
    else:
        loi_thong_tin_name.config(text="")
    for kiem_tra_space_va_ki_tu_dac_biet_ten in name:
        if kiem_tra_space_va_ki_tu_dac_biet_ten == " ":
            thong_loi_thieu_thong_tin_name.config(text="Tên không được có khoảng trắng")
            return False
        if kiem_tra_space_va_ki_tu_dac_biet_ten == "!" or kiem_tra_space_va_ki_tu_dac_biet_ten == "@" or kiem_tra_space_va_ki_tu_dac_biet_ten == "#" or kiem_tra_space_va_ki_tu_dac_biet_ten == "$" or kiem_tra_space_va_ki_tu_dac_biet_ten == "%" or kiem_tra_space_va_ki_tu_dac_biet_ten == "^" or kiem_tra_space_va_ki_tu_dac_biet_ten == "&" or kiem_tra_space_va_ki_tu_dac_biet_ten == "*" or kiem_tra_space_va_ki_tu_dac_biet_ten == "(" or kiem_tra_space_va_ki_tu_dac_biet_ten == ")" or kiem_tra_space_va_ki_tu_dac_biet_ten == "-" or kiem_tra_space_va_ki_tu_dac_biet_ten == "+" or kiem_tra_space_va_ki_tu_dac_biet_ten == "=" or kiem_tra_space_va_ki_tu_dac_biet_ten == "{" or kiem_tra_space_va_ki_tu_dac_biet_ten == "}" or kiem_tra_space_va_ki_tu_dac_biet_ten == "[" or kiem_tra_space_va_ki_tu_dac_biet_ten == "]" or kiem_tra_space_va_ki_tu_dac_biet_ten == "|" or kiem_tra_space_va_ki_tu_dac_biet_ten == "\\" or kiem_tra_space_va_ki_tu_dac_biet_ten == ":" or kiem_tra_space_va_ki_tu_dac_biet_ten == ";" or kiem_tra_space_va_ki_tu_dac_biet_ten == "\"" or kiem_tra_space_va_ki_tu_dac_biet_ten == "'" or kiem_tra_space_va_ki_tu_dac_biet_ten == "<" or kiem_tra_space_va_ki_tu_dac_biet_ten == ">" or kiem_tra_space_va_ki_tu_dac_biet_ten == "," or kiem_tra_space_va_ki_tu_dac_biet_ten == "." or kiem_tra_space_va_ki_tu_dac_biet_ten == "/" or kiem_tra_space_va_ki_tu_dac_biet_ten == "?":
            thong_loi_name_co_ki_tu_dac_biet.config(text="Tên không được có kí tự đặc biệt")
            return False
              
    # Kiểm tra mật khẩu
    if password == "":
        thong_loi_thieu_thong_tin_password.config(text="Vui lòng điền vào ô này")
        return False
    elif len(password) <= 8:
        thong_loi_so_chi_co_so.config(text="""*Mật khẩu quá yếu
            *mật khẩu cần lớn hơn 8 kí tự""")
        return False
    elif password.isdigit():
        thong_loi_so_chi_co_so.config(text="*mật khẩu cần có chữ cái và kí tự đặc biệt")
        return False
    elif password.isalpha():
        print("*Mật khẩu bao gồm số,chữ cái,kí tự đặc biệt")
        return False
    thong_loi_thieu_thong_tin_password.config(text="")
    luu_list_user[name] = password
    return True

#====hàm xử lí click vào nút đăng kí ===
def xu_li_nut_dang_ki_nhap():
    name = dang_ky_ten.get()
    password = dang_ky_password.get()
    time_luu_info = time.localtime()
    print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] |NAME_USER|>{name}")
    print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] |PASSWORD|>{password}")

def bam_nut_dang_ki():
    if luu_info():  #lưu thành công
        xu_li_nut_dang_ki_nhap()
        name = dang_ky_ten.get()
        password = dang_ky_password.get()
        xu_li_nut_dang_ki_nhap()
        messagebox.showinfo("THÔNG BÁO", "Đăng kí thành công!")
        thong_loi_thieu_thong_tin_name.config(text="")
        thong_loi_thieu_thong_tin_password.config(text="")

def bam_nut_dang_nhap():
    if luu_info():  #lưu thành công
        xu_li_nut_dang_ki_nhap()
        name = dang_ky_ten.get()
        password = dang_ky_password.get()
        xu_li_nut_dang_ki_nhap()
        messagebox.showinfo("THÔNG BÁO", "Đăng nhập thành công!")
        thong_loi_thieu_thong_tin_name.config(text="")
        thong_loi_thieu_thong_tin_password.config(text="")

def bam_nut_goi_dang_nhap():
    root.title("ĐĂNG NHẬP")
    dang_ki_head.config(text="ĐĂNG NHẬP",fg="#2200ff",bg="#9dffad",font=("Arial",20))
    root.config(bg="#E2FF6D")
    nen_desktop_dangki.config(bg="#9dffad")
    dang_ky_ten_head.config(bg="#9dffad")
    dang_ky_ten.config(bg="#9dffad")
    dang_ky_password_head.config(bg="#9dffad")
    dang_ky_password.config(bg="#9dffad")
    thong_loi_thieu_thong_tin_name.config(bg="#9dffad")   
    thong_loi_thieu_thong_tin_password.config(bg="#9dffad")  
    thong_loi_name_co_ki_tu_dac_biet.config(bg="#9dffad")  
    thong_loi_so_chi_co_so.config(bg="#9dffad")  
    dang_ky_ten.delete(0,END)
    dang_ky_password.delete(0,END)
    dang_ky_button.place_forget() 
    goi_dang_nhap_button.place_forget()
    dang_nhap_button.place(x=190,y=270)
    goi_dang_ki_button.place(x=375,y=350)
    thong_loi_thieu_thong_tin_name.config(text="")
    thong_loi_thieu_thong_tin_password.config(text="")
    version.config(bg="#E2FF6D")

def bam_nut_goi_dang_ki():
    root.title("ĐĂNG KÍ")
    dang_ki_head.config(text="ĐĂNG KÍ",fg="#2200ff",bg="#ADFFF5",font=("Arial",20))
    root.config(bg="#00ffd5")
    nen_desktop_dangki.config(bg="#ADFFF5")
    dang_ky_ten_head.config(bg="#ADFFF5")
    dang_ky_ten.config(bg="#ADFFF5")
    dang_ky_password_head.config(bg="#ADFFF5")
    dang_ky_password.config(bg="#ADFFF5")
    thong_loi_thieu_thong_tin_name.config(bg="#ADFFF5")  
    thong_loi_thieu_thong_tin_password.config(bg="#ADFFF5")  
    thong_loi_name_co_ki_tu_dac_biet.config(bg="#ADFFF5") 
    thong_loi_so_chi_co_so.config(bg="#ADFFF5")
    dang_ky_ten.delete(0,END)
    dang_ky_password.delete(0,END)
    dang_nhap_button.place_forget() 
    goi_dang_ki_button.place_forget()
    dang_ky_button.place(x=190,y=270)
    goi_dang_nhap_button.place(x=375,y=350)
    thong_loi_thieu_thong_tin_name.config(text="")
    thong_loi_thieu_thong_tin_password.config(text="")
    version.config(bg="#00ffd5")

#======== hàm ========
def nhan_ver(event):
    if event is None:
        inbox_khoa()
        return
    listbox_visible = False
    x = event.x_root - root.winfo_rootx()
    y = event.y_root - root.winfo_rooty()
    ver_listbox.place(x=x,y=y+20)
    ver_listbox.lift()
    selection = ver_listbox.curselection()
    if not selection:
        return
    value = ver_listbox.get(selection[0])
    if value == "inbox admin":
        inbox_khoa()

#===tạo nút đăng kí===
dang_ky_button = Button(root,text="ĐĂNG KÍ",fg="#b300ff",bg="#00ff22",font=("Arial",15),command=bam_nut_dang_ki)
dang_nhap_button = Button(root,text="ĐĂNG NHẬP",fg="#b300ff",bg="#00ff22",font=("Arial",15),command=bam_nut_dang_nhap)
font_underline_ = font.Font(family="Arial", size=12, underline=1)
goi_dang_nhap_button = Button(root,text="ĐĂNG_NHẬP",fg="#0034C5",bg="#00ffd5",font=font_underline_,bd=0,highlightthickness=0, relief="flat",command = bam_nut_goi_dang_nhap)
goi_dang_ki_button = Button(root,text="ĐĂNG KÍ",fg="#0034C5",bg="#E2FF6D",font=font_underline_,bd=0,highlightthickness=0, relief="flat",command=bam_nut_goi_dang_ki)
version = Button(root,text="ver_6w44a27h10",fg="#272727",bg="#00ffd5",command =lambda: nhan_ver(None),highlightthickness =0,relief="flat")

def luu_info_vao_file(name, password):
    with open("data_info_user.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}:{password}\n")

# === HÀM GHI LOG ===
def click_vao_nhap_password(event):
     time_luu_info = time.localtime()
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng click vào ô nhập liệu mật khẩu")
def nhap_vao_nhap_password(event):
     time_luu_info = time.localtime()
     thong_loi_thieu_thong_tin_password.config(text="")
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng nhập vào ô nhập liệu password")
def nhap_vao_nhap_name(event):
     time_luu_info = time.localtime()
     thong_loi_thieu_thong_tin_name.config(text="")
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng nhập vào ô nhập liệu tên")
def click_vao_nhap_name(event):
     time_luu_info = time.localtime()
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng click vào ô nhập liệu tên")
def nhan_nut_trong_ban_phim(event):
     time_luu_info = time.localtime()
     print(f'[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng nhấn phím "{event.keysym}"')


# === ĐẶT VỊ TRÍ ===
dang_ki_head.place(x=180,y=34)
dang_ky_ten_head.place(x=58,y=80)
dang_ky_ten.place(x=57,y=100)
dang_ky_password_head.place(x=58,y=180)
dang_ky_password.place(x=58,y=200)
dang_ky_button.place(x=190,y=270)
goi_dang_nhap_button.place(x=375,y=350)

#===gộp hàm===
def log_nhap_ten(event):
     nhap_vao_nhap_name(event)
     nhan_nut_trong_ban_phim(event)
def log_nhap_password(event):
     nhap_vao_nhap_password(event)
     nhan_nut_trong_ban_phim(event)

# === GẮN SỰ KIỆN ===
dang_ky_button.bind("<Enter>",trong_nut_dang_ki)
dang_ky_button.bind("<Leave>",ra_ngoai_nut_dang_ki)
dang_nhap_button.bind("<Leave>",ra_ngoai_nut_dang_nhap)
dang_nhap_button.bind("<Enter>",trong_nut_dang_nhap)
dang_ky_ten.bind("<FocusIn>",click_vao_nhap_name)
dang_ky_ten.bind("<Key>",log_nhap_ten)
dang_ky_password.bind("<FocusIn>",click_vao_nhap_password)
dang_ky_password.bind("<Key>",log_nhap_password)
version.place(x=3,y=1)

root.mainloop()