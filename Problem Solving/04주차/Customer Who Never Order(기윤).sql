# Write your MySQL query statement below
SELECT NAME AS Customers
FROM CUSTOMERS
WHERE CUSTOMERS.ID NOT IN (
    SELECT CUSTOMERID
    FROM ORDERS
);