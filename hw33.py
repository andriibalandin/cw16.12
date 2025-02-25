import sqlite3

with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salesmen (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales (
            id INTEGER PRIMARY KEY,
            salesman_id INTEGER,
            customer_id INTEGER,
            product_name TEXT,
            amount INTEGER,
            sale_date DATETIME,
            FOREIGN KEY (salesman_id) REFERENCES Salesmen(id),
            FOREIGN KEY (customer_id) REFERENCES Customers(id)
        );
    ''')

    salesmen_data = [
        (1, 'Іван'),
        (2, 'Петро'),
        (3, 'Віталій')
    ]
    customers_data = [
        (1, 'Перший клієнт'),
        (2, 'Другий клієнт'),
        (3, 'Третій клієнт')
    ]
    sales_data = [
        (1, 1, 1, 'Банан', 100, '2023-01-01 10:00:00'),
        (2, 1, 2, 'Людина', 200, '2023-01-02 11:00:00'),
        (3, 2, 1, 'Запальничка', 150, '2023-01-03 12:00:00'),
        (4, 2, 3, 'Вогнегасник', 300, '2023-01-04 13:00:00'),
        (5, 3, 2, 'Стілець', 250, '2023-01-05 14:00:00'),
        (6, 3, 3, 'Цегла', 50, '2023-01-06 15:00:00')
    ]

    cursor.executemany("INSERT OR IGNORE INTO Salesmen (id, name) VALUES (?, ?);", salesmen_data)
    cursor.executemany("INSERT OR IGNORE INTO Customers (id, name) VALUES (?, ?);", customers_data)
    cursor.executemany("INSERT OR IGNORE INTO Sales (id, salesman_id, customer_id, product_name, amount, sale_date) "
                       "VALUES (?, ?, ?, ?, ?, ?);", sales_data)
    conn.commit()

    salesman_id = 1
    customer_id = 1

    print("\n1. Всі угоди:")
    cursor.execute("SELECT * FROM Sales;")
    for row in cursor.fetchall():
        print(row)

    print(f"\n2. Угоди продавця з id = {salesman_id}:")
    cursor.execute("SELECT * FROM Sales WHERE salesman_id = ?;", (salesman_id,))
    for row in cursor.fetchall():
        print(row)

    print("\n3. Угода з максимальною сумою:")
    cursor.execute("SELECT * FROM Sales ORDER BY amount DESC LIMIT 1;")
    print(cursor.fetchone())

    print("\n4. Угода з мінімальною сумою:")
    cursor.execute("SELECT * FROM Sales ORDER BY amount ASC LIMIT 1;")
    print(cursor.fetchone())

    print(f"\n5. Максимальна угода продавця з id = {salesman_id}:")
    cursor.execute("SELECT * FROM Sales WHERE salesman_id = ? ORDER BY amount DESC LIMIT 1;", (salesman_id,))
    print(cursor.fetchone())

    print(f"\n6. Мінімальна угода продавця з id = {salesman_id}:")
    cursor.execute("SELECT * FROM Sales WHERE salesman_id = ? ORDER BY amount ASC LIMIT 1;", (salesman_id,))
    print(cursor.fetchone())

    print(f"\n7. Максимальна угода покупця з id = {customer_id}:")
    cursor.execute("SELECT * FROM Sales WHERE customer_id = ? ORDER BY amount DESC LIMIT 1;", (customer_id,))
    print(cursor.fetchone())

    print(f"\n8. Мінімальна угода покупця з id = {customer_id}:")
    cursor.execute("SELECT * FROM Sales WHERE customer_id = ? ORDER BY amount ASC LIMIT 1;", (customer_id,))
    print(cursor.fetchone())

    print("\n9. Продавець з максимальною сумою продажів:")
    cursor.execute("""SELECT s.id, s.name, SUM(sa.amount) AS total_sales FROM Salesmen s
                    JOIN Sales sa ON s.id = sa.salesman_id GROUP BY s.id ORDER BY total_sales DESC LIMIT 1;""")
    print(cursor.fetchone())

    print("\n10. Продавець з мінімальною сумою продажів:")
    cursor.execute("""SELECT s.id, s.name, SUM(sa.amount) AS total_sales FROM Salesmen s
                    JOIN Sales sa ON s.id = sa.salesman_id GROUP BY s.id ORDER BY total_sales ASC LIMIT 1;""")
    print(cursor.fetchone())

    print("\n11. Покупець з максимальною сумою покупок:")
    cursor.execute("""SELECT c.id, c.name, SUM(sa.amount) AS total_purchases FROM Customers c
                    JOIN Sales sa ON c.id = sa.customer_id GROUP BY c.id ORDER BY total_purchases DESC LIMIT 1;""")
    print(cursor.fetchone())

    print(f"\n12. Середня сума покупки для покупця з id = {customer_id}:")
    cursor.execute("SELECT AVG(amount) FROM Sales WHERE customer_id = ?;", (customer_id,))
    avg_purchase = cursor.fetchone()[0]
    print(avg_purchase)

    print(f"\n13. Середня сума продаж для продавця з id = {salesman_id}:")
    cursor.execute("SELECT AVG(amount) FROM Sales WHERE salesman_id = ?;", (salesman_id,))
    avg_sale = cursor.fetchone()[0]
    print(avg_sale)
