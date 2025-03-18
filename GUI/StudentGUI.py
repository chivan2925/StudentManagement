
import tkinter as tk
from tkinter import Frame, Label, Button, Entry, ttk, messagebox

class StudentGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#FF9999")
        self.pack(fill="both", expand=True)
        
        Label(self, text="📌 Quản lý Sinh Viên", font=("Arial", 20, "bold"), bg="#FF9999").pack(pady=10)

        # Khung nhập liệu
        frame_input = Frame(self, bg="#FF9999")
        frame_input.pack(pady=5)

        Label(frame_input, text="Mã SV:", font=("Arial", 12), bg="#FF9999").grid(row=0, column=0, padx=5)
        self.masv_entry = Entry(frame_input, font=("Arial", 12))
        self.masv_entry.grid(row=0, column=1, padx=5)

        Label(frame_input, text="Tên SV:", font=("Arial", 12), bg="#FF9999").grid(row=0, column=2, padx=5)
        self.tensv_entry = Entry(frame_input, font=("Arial", 12))
        self.tensv_entry.grid(row=0, column=3, padx=5)

        Button(frame_input, text="Thêm", font=("Arial", 12), bg="#66CC66", command=self.them_sinh_vien).grid(row=0, column=4, padx=5)
        Button(frame_input, text="Xóa", font=("Arial", 12), bg="#FF6666", command=self.xoa_sinh_vien).grid(row=0, column=5, padx=5)

        # Bảng dữ liệu sinh viên
        columns = ("Mã SV", "Tên SV")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("Mã SV", text="Mã SV")
        self.tree.heading("Tên SV", text="Tên SV")
        self.tree.pack(pady=10, fill="both", expand=True)

    def them_sinh_vien(self):
        """Thêm sinh viên vào danh sách"""
        masv = self.masv_entry.get()
        tensv = self.tensv_entry.get()
        if masv and tensv:
            self.tree.insert("", "end", values=(masv, tensv))
            self.masv_entry.delete(0, tk.END)
            self.tensv_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")

    def xoa_sinh_vien(self):
        """Xóa sinh viên khỏi danh sách"""
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Lỗi", "Vui lòng chọn sinh viên để xóa!")

# Chạy độc lập để test
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Sinh Viên")
    root.geometry("600x400")
    app = StudentGUI(root)
    root.mainloop()
