import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="student_management"
            )
            self.cursor = self.conn.cursor()
            print(" Kết nối Database thành công!")
        except mysql.connector.Error as e:
            print(" Lỗi kết nối Database:", e)

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(" Lỗi SQL:", e)
            return False

    def fetch_data(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(" Lỗi khi lấy dữ liệu:", e)
            return None

    def close_connection(self):
        """Đóng kết nối"""
        self.cursor.close()
        self.conn.close()
