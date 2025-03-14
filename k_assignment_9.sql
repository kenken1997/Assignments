CREATE TABLE Product (
    id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price DECIMAL(10,2)
);

INSERT INTO Product (id, product_name, category, price) VALUES
(1, 'Pillow', 'Bedroom Accessory', 800.00),
(2, 'Headphones', 'Electronics', 50.00),
(3, 'Ladle', 'Kitchen Accessory', 120.00),
(4, 'Notebook', 'Stationery', 5.00),
(5, 'Pen', 'Stationery', 2.00);

CREATE TABLE Sales (
    id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES Product(id)
);

INSERT INTO Sales (id, product_id, quantity_sold, sale_date, total_price) VALUES
(1, 1, 2, '2024-03-10', 1600.00),
(2, 2, 4, '2024-03-11', 200.00),
(3, 3, 1, '2024-03-12', 120.00),
(4, 4, 10, '2024-03-13', 50.00),
(5, 5, 15, '2024-03-14', 30.00);

SELECT * FROM Product;

SELECT product_name, price FROM Product;

SELECT * FROM Sales LIMIT 2;

SELECT * FROM Sales WHERE total_price > 100;

SELECT * FROM Product WHERE category IN (
    SELECT category FROM Product GROUP BY category HAVING COUNT(*) > 1
);

SELECT COUNT(*) AS total_products FROM Product;

SELECT SUM(total_price) AS total_sales FROM Sales;

SELECT AVG(price) AS average_price FROM Product;
