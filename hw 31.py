import sqlite3


with sqlite3.connect("students_grades.db") as conn:
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        city TEXT NOT NULL,
        country TEXT NOT NULL,
        birth_date DATE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        group_name TEXT NOT NULL,
        average_grade REAL NOT NULL,
        subject_min_grade TEXT NOT NULL,
        subject_max_grade TEXT NOT NULL
    );
    ''')

    print("Таблиця оцінок створена")


with sqlite3.connect("hospital.db") as conn:
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        building INTEGER NOT NULL CHECK (building BETWEEN 1 AND 5),
        financing REAL NOT NULL CHECK (financing >= 0) DEFAULT 0,
        name NVARCHAR(100) NOT NULL UNIQUE CHECK (name <> '')
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name NVARCHAR(100) NOT NULL UNIQUE CHECK (name <> ''),
        severity INTEGER NOT NULL CHECK (severity >= 1) DEFAULT 1
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL CHECK (name <> ''),
        surname TEXT NOT NULL CHECK (surname <> ''),
        phone CHAR(10),
        salary REAL NOT NULL CHECK (salary > 0)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Examinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name NVARCHAR(100) NOT NULL UNIQUE CHECK (name <> ''),
        day_of_week INTEGER NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
        start_time TIME NOT NULL CHECK (start_time BETWEEN '08:00' AND '18:00'),
        end_time TIME NOT NULL CHECK (end_time > start_time)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        building INTEGER NOT NULL CHECK (building BETWEEN 1 AND 5),
        floor INTEGER NOT NULL CHECK (floor >= 1),
        name NVARCHAR(20) NOT NULL UNIQUE CHECK (name <> '')
    );
    ''')

    print("Таблиці лікарні створені")
