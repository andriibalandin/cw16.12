import sqlite3

with sqlite3.connect("students_grades.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
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
            subject_min_grade INTEGER NOT NULL,
            subject_max_grade INTEGER NOT NULL
        );
    """)

    students = [
        ("Іван Петренко", "Київ", "Україна", "2002-05-10", "ivan.petrenko@example.com", "380671737568", "Група A", 85.0, 70, 95),
        ("Марія Іванова", "Львів", "Україна", "2001-11-20", "maria.ivanova@example.com", "380681234568", "Група B", 90.5, 80, 98),
        ("Олександр Сидоров", "Одеса", "Україна", "2004-03-15", "oleksandr.sydorov@example.com", "380691234569", "Група A", 75.0, 65, 88),
        ("Борис Коваленко", "Дніпро", "Україна", "2000-07-30", "boris.kovalenko@example.com", "380701234570", "Група C", 82.3, 72, 90),
        ("Олена Шевченко", "Харків", "Україна", "2002-12-05", "olena.shevchenko@example.com", "380711274571", "Група B", 88.8, 78, 93)
    ]

    cursor.executemany("""INSERT OR IGNORE INTO student_grades 
        (full_name, city, country, birth_date, email, phone, group_name, average_grade, subject_min_grade, subject_max_grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, students)

    cursor.execute("SELECT * FROM student_grades;")
    print("\n1. Вся інформація про студентів:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT full_name FROM student_grades;")
    print("\n2. ПІБ студентів:")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT average_grade FROM student_grades;")
    print("\n3. Середні оцінки студентів:")
    for row in cursor.fetchall():
        print(row[0])

    specified_min_grade = 70
    cursor.execute("SELECT full_name FROM student_grades WHERE subject_min_grade > ?;", (specified_min_grade,))
    print(f"\n4. Студенти з мінімальною оцінкою, більшою ніж {specified_min_grade}:")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT DISTINCT country FROM student_grades;")
    print("\n5. Унікальні країни студентів:")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT DISTINCT city FROM student_grades;")
    print("\n6. Унікальні міста студентів:")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT DISTINCT group_name FROM student_grades;")
    print("\n7. Унікальні назви груп:")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT DISTINCT subject_min_grade FROM student_grades;")
    print("\n8. Унікальні значення subject_min_grade:")
    for row in cursor.fetchall():
        print(row[0])

    lower_bound, upper_bound = 65, 80
    cursor.execute("SELECT full_name, subject_min_grade FROM student_grades WHERE subject_min_grade BETWEEN ? AND ?;",
                   (lower_bound, upper_bound))
    print(f"\n9. Студенти з мінімальною оцінкою у діапазоні {lower_bound}-{upper_bound}:")
    for row in cursor.fetchall():
        print(row[0], row[1])

    cursor.execute("""SELECT full_name FROM student_grades 
            WHERE (CAST(strftime('%Y', 'now') AS INTEGER) - CAST(strftime('%Y', birth_date) AS INTEGER)) >= 20;""")
    print("\n10. Студенти, яким виповнилося 20 років:")
    for row in cursor.fetchall():
        print(row[0])

    min_age, max_age = 18, 22
    cursor.execute("""SELECT full_name FROM student_grades WHERE (CAST(strftime('%Y', 'now') AS INTEGER) - 
                    CAST(strftime('%Y', birth_date) AS INTEGER)) BETWEEN ? AND ?;""", (min_age, max_age))
    print(f"\n11. Студенти з віком у діапазоні {min_age}-{max_age} років:")
    for row in cursor.fetchall():
        print(row[0])

    specific_name = "Борис"
    cursor.execute("SELECT full_name FROM student_grades WHERE full_name LIKE '%' || ? || '%';", (specific_name,))
    print(f"\n12. Студенти з ім'ям, що містить '{specific_name}':")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT full_name, phone  FROM student_grades WHERE phone LIKE '%7%7%7%' ;")
    print("\n13. Студенти, у телефонному номері яких є три сімки:")
    for row in cursor.fetchall():
        print(row[0], row[1])

    letter = 'i'
    pattern = letter.lower() + '%'
    cursor.execute("SELECT email FROM student_grades WHERE lower(email) LIKE ?;", (pattern,))
    print(f"\n14. Електронні адреси студентів, що починаються з '{letter}':")
    for row in cursor.fetchall():
        print(row[0])

    conn.commit()


with sqlite3.connect("fruits_vegetables.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vegetables_and_fruits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL CHECK (type IN ('vegetable', 'fruit')),
            color TEXT NOT NULL,
            calories INTEGER NOT NULL,
            description TEXT,
            UNIQUE(name, type)
        );
    """)

    fruits_vegetables = [
        ("Apple", "fruit", "red", 52, "Sweet and crunchy"),
        ("Banana", "fruit", "yellow", 96, "Soft and sweet"),
        ("Carrot", "vegetable", "orange", 41, "Crunchy and healthy"),
        ("Tomato", "vegetable", "red", 18, "Juicy and often mistaken for a fruit"),
        ("Cucumber", "vegetable", "green", 16, "Refreshing and hydrating"),
        ("Strawberry", "fruit", "red", 33, "Small and sweet"),
        ("Blueberry", "fruit", "blue", 57, "Small and full of antioxidants")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO vegetables_and_fruits (name, type, color, calories, description)
        VALUES (?, ?, ?, ?, ?);
    """, fruits_vegetables)

    calorie_limit = 20
    cursor.execute("SELECT name, calories FROM vegetables_and_fruits WHERE type = 'vegetable' AND calories < ?;",
                   (calorie_limit,))
    print(f"\n1. Овочі з калорійністю менше {calorie_limit}:")
    for row in cursor.fetchall():
        print(row[0], row[1])

    lower_cal, upper_cal = 30, 60
    cursor.execute("SELECT name, calories FROM vegetables_and_fruits WHERE type = 'fruit' AND calories BETWEEN ? AND ?;",
                   (lower_cal, upper_cal))
    print(f"\n2. Фрукти з калорійністю у діапазоні {lower_cal}-{upper_cal}:")
    for row in cursor.fetchall():
        print(row[0], row[1])

    search_word = 'Tom'
    cursor.execute("SELECT name FROM vegetables_and_fruits WHERE type = 'vegetable' AND name LIKE '%' || ? || '%';",
                   (search_word,))
    print(f"\n3. Овочі, у назві яких є слово '{search_word}':")
    for row in cursor.fetchall():
        print(row[0])

    search_desc = 'sweet'
    cursor.execute("SELECT name FROM vegetables_and_fruits WHERE description LIKE '%' || ? || '%';", (search_desc,))
    print(f"\n4. Овочі та фрукти, у описі яких є слово '{search_desc}':")
    for row in cursor.fetchall():
        print(row[0])

    cursor.execute("SELECT name, color FROM vegetables_and_fruits WHERE color IN ('yellow', 'red');")
    print("\n5. Овочі та фрукти жовтого або червоного кольору:")
    for row in cursor.fetchall():
        print(row[0], row[1])

    conn.commit()
    