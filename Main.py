import tkinter as tk
from tkinter import Frame, Label, Button
from GUI import StudentGUI  # Import giao diện điểm danh (hoặc thay thế bằng class phù hợp)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hệ Thống Quản Lý Sinh Viên")
        self.geometry("900x500")

        # Danh sách menu và màu sắc
        self.menu_items = {
            "Tài khoản": "#FF9999",
            "Môn học": "#99FF99",
            "Thời Khóa Biểu": "#9999FF",
            "Điểm": "#FFFF99",
            "Điểm Danh": "#FF66FF",
            "Học Phí": "#66CCFF",
        }

        # Tạo layout: Menu bên trái + Nội dung bên phải
        self.menu_frame = Frame(self, bg="black", width=180)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = Frame(self, bg="white")
        self.content_frame.pack(side="right", expand=True, fill="both")

        # Thêm các nút menu
        for name, color in self.menu_items.items():
            btn = Button(self.menu_frame, text=name, font=("Arial", 14), width=15,
                         bg=color, fg="black",
                         command=lambda n=name, c=color: self.hien_menu(n, c))
            btn.pack(pady=5, fill="x")

        # Khởi tạo màn hình mặc định
        self.hien_menu("Chào mừng!", "white")

    def hien_menu(self, ten_muc, color):
        """Cập nhật nội dung bên phải theo mục được chọn"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Xóa nội dung cũ

        self.content_frame.config(bg=color)  # Đổi màu nền

        # Hiển thị giao diện tương ứng
        Label(self.content_frame, text=f"📌 {ten_muc}", font=("Arial", 25, "bold"), bg=color).pack(pady=20)

        if ten_muc == "Điểm Danh":
            StudentGUI(self.content_frame)  # Gọi giao diện điểm danh

# Chạy chương trình
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
