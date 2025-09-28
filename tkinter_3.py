import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple Calculator")
# Tạo khung nhập liệu
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Định nghĩa các hàm xử lý
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error") 
# Tạo các nút bấm
button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click("/"))

button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)
# Đặt các nút bấm lên lưới
buttons = [
    button_1, button_2, button_3, button_add,
    button_4, button_5, button_6, button_subtract,
    button_7, button_8, button_9, button_multiply,
    button_clear, button_0, button_equal, button_divide
]

row = 1
col = 0
for button in buttons:
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
# Chạy ứng dụng
root.mainloop()