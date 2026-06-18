import sqlite3
import pytest
from database import init_db, add_customer, DB_PATH

def test_db_creation():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customers'")
    assert cursor.fetchone() is not None
    conn.close()

def test_add_customer():
    init_db()
    add_customer("Тест", "123", "Адрес")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM customers WHERE name='Тест'")
    res = cursor.fetchone()
    conn.close()
    assert res is not None