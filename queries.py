# queries.py
import psycopg2
from prettytable import PrettyTable

# Database connection
connection = psycopg2.connect(
    host="localhost",
    database="store_database",
    user="user",
    password="password",
    port=5432
)

cursor = connection.cursor()

# Helper function to display query results using PrettyTable
def display_query(query, headers):
    cursor.execute(query)
    table = PrettyTable(headers)
    for row in cursor.fetchall():
        table.add_row(row)
    print(table)

# Query 1: All sales paid in cash, sorted by client name
print("Sales paid in cash, sorted by client name:")
display_query("""
SELECT Clients.company_name, Sales.*
FROM Sales
JOIN Clients ON Sales.client_id = Clients.client_id
WHERE Sales.payment_method = 'Cash'
ORDER BY Clients.company_name;
""", ["Client Name", "Sale ID", "Sale Date", "Client ID", "Product ID", "Quantity Sold", "Discount", "Payment Method", "Delivery Needed", "Delivery Cost"])

# Query 2: All sales with delivery required
print("\nSales with delivery required:")
display_query("""
SELECT * FROM Sales WHERE delivery_needed = TRUE;
""", ["Sale ID", "Sale Date", "Client ID", "Product ID", "Quantity Sold", "Discount", "Payment Method", "Delivery Needed", "Delivery Cost"])

# Query 3: Total amount to be paid by each client including discount
print("\nTotal amount to be paid for each client:")
display_query("""
SELECT Clients.company_name, SUM(Products.price * Sales.quantity_sold * (1 - Sales.discount)) AS total_amount
FROM Sales
JOIN Clients ON Sales.client_id = Clients.client_id
JOIN Products ON Sales.product_id = Products.product_id
GROUP BY Clients.company_name;
""", ["Client Name", "Total Amount"])

# Query 4: Purchases by a specific client (parameterized)
client_id = 1  # Example client ID
print(f"\nPurchases of client ID {client_id}:")
cursor.execute("""
SELECT * FROM Sales WHERE client_id = %s;
""", (client_id,))
table = PrettyTable(["Sale ID", "Sale Date", "Client ID", "Product ID", "Quantity Sold", "Discount", "Payment Method", "Delivery Needed", "Delivery Cost"])
for row in cursor.fetchall():
    table.add_row(row)
print(table)

# Query 5: Count of purchases for each client
print("\nNumber of purchases for each client:")
display_query("""
SELECT Clients.company_name, COUNT(Sales.sale_id) AS purchase_count
FROM Sales
JOIN Clients ON Sales.client_id = Clients.client_id
GROUP BY Clients.company_name;
""", ["Client Name", "Purchase Count"])

# Query 6: Total amount spent by each client, split by payment method (cross-tab query)
print("\nTotal amount spent by each client by payment method:")
display_query("""
SELECT Clients.company_name, 
       SUM(CASE WHEN Sales.payment_method = 'Cash' THEN Products.price * Sales.quantity_sold * (1 - Sales.discount) ELSE 0 END) AS cash_spent,
       SUM(CASE WHEN Sales.payment_method = 'Non-cash' THEN Products.price * Sales.quantity_sold * (1 - Sales.discount) ELSE 0 END) AS non_cash_spent
FROM Sales
JOIN Clients ON Sales.client_id = Clients.client_id
JOIN Products ON Sales.product_id = Products.product_id
GROUP BY Clients.company_name;
""", ["Client Name", "Cash Spent", "Non-Cash Spent"])

# Closing the connection
cursor.close()
connection.close()
