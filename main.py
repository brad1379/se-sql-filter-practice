import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')

# # ---------------- Basic query to pull all data ---------------- 
# employees = pd.read_sql("""
# SELECT *
#  FROM employees;
# """, conn)

# print(employees)

# # ---------------- Select all employees with first name Leslie ---------------- 
# employees_named_leslie = pd.read_sql("""
# SELECT *
#  FROM employees
#  WHERE firstName = "Leslie";
# """, conn)

# print(employees_named_leslie)

# # ---------------- Select employees named Leslie and only output firstName, lastName, and jobTitle ---------------- 
# employees_named_leslie = pd.read_sql("""
# SELECT firstName, lastName, jobTitle
#  FROM employees
#  WHERE firstName = "Leslie";
# """, conn)

# print(employees_named_leslie)

# # ---------------- Select employees whose last name is < 5 characters part 1 ---------------- 
# employees_last_name_5_chars = pd.read_sql("""
# SELECT *, length(lastName) as lastname_length
#  FROM employees
#  WHERE lastname_length < 5;
# """, conn)

# print(employees_last_name_5_chars)

# # ---------------- Select employees whose last name is < 5 characters part 2 ---------------- 
# employees_last_name_5_chars_2 = pd.read_sql("""
# SELECT *
#  FROM employees
#  WHERE length(lastName) <= 4;
# """, conn)

# print(employees_last_name_5_chars_2)

# # ---------------- Round price of orders as an integer ---------------- 
# orderDetails = pd.read_sql("""
# SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
#  FROM orderdetails
#  WHERE rounded_price_int >= 100
# """, conn)

# print(orderDetails)

# # ---------------- Find all orders placed in 2005 ---------------- 
# ordered_in_2005 = pd.read_sql("""
# SELECT *, strftime("%Y", orderDate) AS year
#  FROM orders
#  WHERE year = "2005";
# """, conn)

# print(ordered_in_2005)

# # ---------------- Find all employees with that has 'sale' or 'sales' in job title ---------------- 
# sales_employees = pd.read_sql("""
# SELECT *
#  FROM employees
#  WHERE jobTitle LIKE "sale%";
# """, conn)

# print(sales_employees)

# ---------------- Find how many items are priced at least $200 ---------------- 
items_at_least_200 = pd.read_sql("""
SELECT COUNT(priceEach)
 FROM orderDetails
 WHERE priceEach >= 200;
""", conn)

print(items_at_least_200)

conn.close()