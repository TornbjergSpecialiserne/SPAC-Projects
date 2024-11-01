SELECT * FROM products
ORDER BY UnitPrice DESC;
SELECT * FROM Customers
WHERE Country ='UK' OR Country = "Spain";
SELECT * FROM products
WHERE UnitsinStock > 100 AND UnitPrice >= 25;
SELECT DISTINCT ShipCountry FROM Orders;
SELECT * FROM Orders
WHERE YEAR(OrderDate) = "1996" AND MONTH(OrderDate) = "10";
SELECT * FROM Orders
WHERE ShipRegion IS NULL AND ShipCountry = "Germany" AND Freight >= 100 AND EmployeeID = 1 AND YEAR(OrderDate) = "1996";
SELECT * FROM Orders
WHERE ShippedDate > RequiredDate;
SELECT * FROM Orders
WHERE YEAR(OrderDate) = 1997 AND 1<=MONTH(OrderDate) AND MONTH(OrderDate)<=4 AND ShipCountry = "Canada";
SELECT * FROM Orders
WHERE (EmployeeID = 2 OR EmployeeID = 5 OR EmployeeID = 8) AND ShipRegion IS NOT NULL AND (ShipVia = 1 OR ShipVia = 3)
ORDER BY EmployeeID ASC, ShipVia ASC;
SELECT * FROM Employees
WHERE Region IS NOT NULL AND YEAR(BirthDate)<=1960;
