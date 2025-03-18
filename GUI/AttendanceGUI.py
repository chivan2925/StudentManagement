import tkinter as tk
from tkinter import ttk, messagebox
from BUS.AttendanceBUS import AttendanceBUS

class AttendanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý điểm danh")
        self.root.geometry("600x400")

        self.attendance_bus = AttendanceBUS()

        # Label & Entry chọn ngày
        self.label_date = tk.Label(root, text="Ngày:", font=("Arial", 12))
        self.label_date.pack()
        self.entry_date = tk.Entry(root, font=("Arial", 12))
        self.entry_date.pack()

        # Nút lấy dữ liệu điểm danh
        self.btn_fetch = tk.Button(root, text="Lấy danh sách điểm danh", command=self.fetch_attendance)
        self.btn_fetch.pack()

        # Treeview hiển thị dữ liệu
        self.tree = ttk.Treeview(root, columns=("ID", "Face ID", "Schedule ID", "Ngày", "Trạng thái"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Face ID", text="Face ID")
        self.tree.heading("Schedule ID", text="Schedule ID")
        self.tree.heading("Ngày", text="Ngày")
        self.tree.heading("Trạng thái", text="Trạng thái")
        self.tree.pack(expand=True, fill="both")

        # Nút thống kê
        self.btn_statistics = tk.Button(root, text="Thống kê", command=self.show_statistics)
        self.btn_statistics.pack()

    def fetch_attendance(self):
        date = self.entry_date.get()
        if not date:
            messagebox.showerror("Lỗi", "Vui lòng nhập ngày")
            return
        
        self.tree.delete(*self.tree.get_children())  # Xóa dữ liệu cũ
        data = self.attendance_bus.get_attendance_by_date(date)
        for record in data:
            self.tree.insert("", "end", values=(record.attendance_id, record.face_id, record.schedule_id, record.attendance_date, record.status))

    def show_statistics(self):
        data = self.attendance_bus.get_statistics()
        result_text = "\n".join([f"{status}: {count}" for status, count in data])
        messagebox.showinfo("Thống kê", result_text)

    def __del__(self):
        self.attendance_bus.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceGUI(root)
    root.mainloop()
