import tkinter as tk
from tkinter import messagebox
import random

# Cài đặt biến toàn cục
MAX_PRESSES = 10  # Số lần nhấn nút cần thiết
MAX_REPEATS = 2   # Số lần lặp lại cửa sổ lỗi (Tổng cộng 3 cửa sổ)
global current_press_count
global current_repeat_count

current_press_count = 0
current_repeat_count = 0

def shake_window(window):
    """Tạo hiệu ứng rung nhẹ cửa sổ để mô phỏng sự cố hệ thống."""
    # Rung cửa sổ 3 lần với biên độ nhỏ
    for _ in range(3):
        for x_offset in [-3, 3]:
            window.geometry(f"+{window.winfo_x() + x_offset}+{window.winfo_y()}")
            window.update()
            window.after(30)
        window.geometry(f"+{window.winfo_x() - 3}+{window.winfo_y()}")
        window.update()

def handle_close_attempt():
    """Xử lý sự kiện khi nút XÁC NHẬN được nhấn."""
    global current_press_count, current_repeat_count, root, status_label, close_button
    
    current_press_count += 1
    shake_window(root) # Rung nhẹ mỗi khi nhấn
    
    if current_press_count < MAX_PRESSES:
        # ẨN SỐ LẦN CÒN LẠI: Chỉ hiển thị thông báo lỗi chung chung
        status_label.config(text="Lỗi Ghi log sự cố. Vui lòng TIẾP TỤC nhấn để đảm bảo quá trình xác nhận.", fg="#FF4500")
        
        # Thêm hiệu ứng thay đổi màu nút nhẹ
        button_colors = ["#DC143C", "#B22222", "#8B0000"]
        close_button.config(bg=random.choice(button_colors))
        
    else:
        # Đã nhấn đủ số lần
        root.destroy()
        
        # Kiểm tra xem có cần lặp lại thông báo không
        if current_repeat_count < MAX_REPEATS:
            current_repeat_count += 1
            # Hiển thị cửa sổ lặp lại sau 500ms
            tk.Tk().after(500, create_critical_alert_window) 
        else:
            # Hoàn thành 3 lần cửa sổ
            messagebox.showinfo("Khắc phục Sự cố", "✅ Hệ thống đã cô lập Malware. Quá trình gửi báo cáo về SOC (Security Operations Center) đã hoàn tất.")


def create_critical_alert_window():
    """Tạo và hiển thị cửa sổ cảnh báo chuyên nghiệp."""
    global root, status_label, close_button, current_press_count
    
    # 1. Thiết lập cửa sổ chính
    root = tk.Tk()
    root.title("⚠️ LỖI HỆ THỐNG TRỌNG YẾU: CẢNH BÁO BẢO MẬT ⚠️") 
    root.geometry("650x280")
    root.eval('tk::PlaceWindow . center')
    root.attributes('-topmost', True) # Giữ cửa sổ trên cùng
    root.protocol("WM_DELETE_WINDOW", lambda: shake_window(root)) # Ngăn đóng bằng nút X

    # Reset số lần nhấn cho cửa sổ mới
    current_press_count = 0 

    # 2. Nội dung thông báo
    error_title = tk.Label(root, 
                           text="🛑 PHÁT HIỆN KẾT NỐI VỚI C2 SERVER (Command & Control) 🛑", 
                           fg="white", 
                           bg="#8B0000", 
                           font=("Consolas", 16, "bold"),
                           padx=15, pady=10)
    error_title.pack(pady=(20, 10), fill='x')

    # Nội dung chi tiết lỗi với thuật ngữ chuyên nghiệp
    error_message = tk.Label(root, 
                             text="Một Malware đã thiết lập kết nối ra ngoài (Outbound Connection) đến một C2 Server.\n"
                                  "Trạng thái lây nhiễm: **PERSISTENCE ESTABLISHED**.\n"
                                  "Lỗ hổng khai thác: **CVE-2023-40477**.\n"
                                  "Vui lòng nhấn nút XÁC NHẬN để kích hoạt giao thức cô lập (Isolation Protocol).", 
                             font=("Consolas", 11),
                             justify=tk.LEFT)
    error_message.pack(pady=10, padx=20)

    # 3. Label trạng thái nhấn (Không hiển thị số lần còn lại)
    status_label = tk.Label(root, 
                            text="MÃ LỖI: CRITICAL_SEC_VIOLATION_0x9C0001 (Yêu cầu xác nhận thủ công!)", 
                            fg="#FF4500", 
                            font=("Consolas", 10, "bold italic"))
    status_label.pack(pady=5)

    # 4. Nút XÁC NHẬN
    close_button = tk.Button(root, 
                             text="XÁC NHẬN VÀ KÍCH HOẠT ISOLATION PROTOCOL", 
                             command=handle_close_attempt,
                             bg="#DC143C", 
                             fg="white", 
                             font=("Consolas", 13, "bold"),
                             padx=20,
                             pady=10,
                             relief=tk.RAISED) 
    close_button.pack(pady=20)
    
    root.mainloop()

# Bắt đầu chương trình
if __name__ == "__main__":
    create_critical_alert_window()