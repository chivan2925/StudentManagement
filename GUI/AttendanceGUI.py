import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Quản lý thông tin Điểm danh")
root.geometry("900x500")
root.configure(bg="white")

label_title = tk.Label(root, text="Quản lý thông tin Điểm danh", font=("Arial", 18, "bold"), bg="white")
label_title.pack(pady=10)

frame_table = tk.Frame(root, bg="blue")
frame_table.pack(pady=10, padx=10, fill="both", expand=True, side="left")

columns = ["MSSV", "Họ", "Tên", "Nhóm", "Trạng Thái", "Ghi Chú"]
for i, col in enumerate(columns):
    lbl = tk.Label(frame_table, text=col, font=("Arial", 10, "bold"), bg="lightblue", width=12)
    lbl.grid(row=0, column=i, padx=2, pady=2)


frame_search = tk.Frame(root, bg="white")
frame_search.pack(pady=10, padx=10, fill="y", side="right")

lbl_search = tk.Label(frame_search, text="Tìm kiếm theo: ID SINH VIÊN", font=("Arial", 10, "bold"), fg="red", bg="white")
lbl_search.pack()

entry_search = tk.Entry(frame_search, width=20)
entry_search.pack(pady=5)

btn_search = tk.Button(frame_search, text="Tìm kiếm")
btn_search.pack(pady=5)

btn_view_all = tk.Button(frame_search, text="Xem tất cả")
btn_view_all.pack(pady=5)

frame_update = tk.Frame(frame_search, bg="lightblue")
frame_update.pack(pady=20, fill="both", expand=True)

lbl_update = tk.Label(frame_update, text="Chỉnh sửa trạng thái và ghi chú", font=("Arial", 10, "bold"), bg="lightblue")
lbl_update.pack()

fields = ["MSSV", "Họ", "Trạng Thái", "Nhóm", "Tên", "Ghi Chú"]
for field in fields:
    lbl = tk.Label(frame_update, text=field, font=("Arial", 10), bg="lightblue")
    lbl.pack(anchor="w", padx=10, pady=2)
root.mainloop()