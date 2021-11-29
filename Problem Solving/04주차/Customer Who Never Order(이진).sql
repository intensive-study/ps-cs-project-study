SELECT Customers.name as Customers
FROM Customers
    LEFT JOIN Orders on Customers.ID = Orders.CustomerID
WHERE Orders.ID IS NULL