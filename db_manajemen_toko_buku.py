import sqlite3

#membuat koneksi dan file database baru
conn = sqlite3.connect("toko_buku.db")
cursor = conn.cursor()

# buat tabel categories (kategori)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL
)
""")

# buat tabel suppliers (suplayer)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Suppliers(
    SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
    SupplierName TEXT NOT NULL,
    ContactName TEXT,
    Phone TEXT
)
""")

# buat tabel books (buku)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL, 
    Author TEXT,
    CategoryID INTEGER,
    SupplierID INTEGER,
    Price REAL,
    Stock INTEGER,
    FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers (SupplierID)
)
""")

# buat tabel Customers (pembeli)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    CustomersID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT NOT NULL,
    Email TEXT
    Phone TEXT
)
""")

# buat tabel employees (pekerja)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeName TEXT NOT NULL,
    Position TEXT,
    Phone TEXT
)
""")

conn.commit()
conn.close()
print("table sudah dibuat!")