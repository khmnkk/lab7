# insert_data.py
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="store_database",
    user="user",
    password="password",
    port=5432
)

cursor = connection.cursor()

# Inserting Clients data
cursor.execute("""
INSERT INTO Clients (company_name, client_type, address, phone, contact_person, account_number)
VALUES
('Company A', 'Legal', 'Street 1', '1234567890', 'John Doe', '123-456-789'),
('Company B', 'Legal', 'Street 2', '2345678901', 'Jane Smith', '234-567-890'),
('John D', 'Individual', 'Street 3', '3456789012', 'John Doe', '345-678-901'),
('Alice Co', 'Individual', 'Street 4', '4567890123', 'Alice Brown', '456-789-012');
""")

# Inserting Products data
cursor.execute("""
INSERT INTO Products (product_name, price, quantity_in_store)
VALUES
('Product 1', 10.0, 100),
('Product 2', 20.0, 50),
('Product 3', 30.0, 150),
('Product 4', 15.5, 80),
('Product 5', 25.0, 60),
('Product 6', 35.5, 120),
('Product 7', 40.0, 70),
('Product 8', 50.0, 90),
('Product 9', 55.0, 30),
('Product 10', 60.0, 40);
""")

# Inserting Sales data
cursor.execute("""
INSERT INTO Sales (sale_date, client_id, product_id, quantity_sold, discount, payment_method, delivery_needed, delivery_cost)
VALUES
('2024-11-01', 1, 1, 2, 0.05, 'Cash', TRUE, 10.0),
('2024-11-02', 2, 2, 1, 0.10, 'Non-cash', FALSE, 0.0),
('2024-11-03', 3, 3, 3, 0.07, 'Cash', TRUE, 15.0),
('2024-11-04', 4, 4, 2, 0.03, 'Non-cash', TRUE, 5.0),
('2024-11-05', 1, 5, 1, 0.15, 'Cash', FALSE, 0.0),
('2024-11-06', 2, 6, 1, 0.20, 'Non-cash', TRUE, 10.0),
('2024-11-07', 3, 7, 2, 0.12, 'Cash', FALSE, 0.0),
('2024-11-08', 4, 8, 1, 0.05, 'Non-cash', TRUE, 20.0),
('2024-11-09', 1, 9, 3, 0.10, 'Cash', TRUE, 15.0),
('2024-11-10', 2, 10, 2, 0.07, 'Non-cash', FALSE, 0.0);
""")

connection.commit()
cursor.close()
connection.close()

