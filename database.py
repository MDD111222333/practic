import sqlite3
import os
from logger_config import logger

DB_PATH = 'data/delivery.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_date TEXT NOT NULL,
            status TEXT CHECK(status IN ('новый','в доставке','выполнен','отменён')),
            total REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE RESTRICT
        )
    ''')
    
    conn.commit()
    conn.close()
    logger.info("База данных инициализирована")

def add_customer(name, phone, address):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name, phone, address) VALUES (?, ?, ?)', (name, phone, address))
    conn.commit()
    conn.close()
    logger.info(f"Добавлен клиент: {name}")

def get_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT orders.id, customers.name, orders.order_date, orders.status, orders.total 
        FROM orders 
        JOIN customers ON orders.customer_id = customers.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_order(customer_id, date, status, total):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (customer_id, order_date, status, total) VALUES (?, ?, ?, ?)', 
                   (customer_id, date, status, total))
    conn.commit()
    conn.close()
    logger.info("Добавлен новый заказ")

def get_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT status, COUNT(*) FROM orders GROUP BY status')
    report = cursor.fetchall()
    conn.close()
    return report
