# create_tables.py
import psycopg2

# Database connection
connection = psycopg2.connect(
    host="localhost",
    database="store_database",
    user="user",
    password="password",
    port=5432
)

cursor = connection.cursor()

# Creating tables
cursor.execute("""
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    client_type VARCHAR(50) CHECK (client_type IN ('Legal', 'Individual')),
    address VARCHAR(255),
    phone CHAR(10) CHECK (phone ~ '^\d{10}$'),
    contact_person VARCHAR(100),
    account_number VARCHAR(20)
);

CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity_in_store INTEGER NOT NULL
);

CREATE TABLE Sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    client_id INTEGER REFERENCES Clients(client_id),
    product_id INTEGER REFERENCES Products(product_id),
    quantity_sold INTEGER NOT NULL,
    discount DECIMAL(3, 2) CHECK (discount BETWEEN 0.03 AND 0.20),
    payment_method VARCHAR(20) CHECK (payment_method IN ('Cash', 'Non-cash')),
    delivery_needed BOOLEAN,
    delivery_cost DECIMAL(10, 2) CHECK (delivery_cost >= 0)
);
""")
connection.commit()
cursor.close()
connection.close()
