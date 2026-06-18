import tkinter as tk
from tkinter import ttk, messagebox
import database

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Быстрая доставка - Заказы")
        self.root.geometry("600x400")
        
        database.init_db()

        # Кнопки
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Обновить", command=self.load_data).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Добавить тестового клиента", command=self.add_test_customer).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Добавить тестовый заказ", command=self.add_test_order).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Показать отчёт", command=self.show_report).grid(row=0, column=3, padx=5)

        # Таблица
        columns = ("id", "client", "date", "status", "total")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("client", text="Клиент")
        self.tree.heading("date", text="Дата")
        self.tree.heading("status", text="Статус")
        self.tree.heading("total", text="Сумма")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for order in database.get_orders():
            self.tree.insert("", tk.END, values=order)

    def add_test_customer(self):
        database.add_customer("Иван Иванов", "+79991234567", "Москва, ул. Пушкина")
        messagebox.showinfo("Успех", "Тестовый клиент добавлен!")

    def add_test_order(self):
        database.add_order(1, "2025-05-01", "новый", 1500.0)
        self.load_data()

    def show_report(self):
        report = database.get_report()
        text = "\n".join([f"{r[0]}: {r[1]} шт." for r in report])
        if not text:
            text = "Нет данных"
        messagebox.showinfo("Отчет по статусам", text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
