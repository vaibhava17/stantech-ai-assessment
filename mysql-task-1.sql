-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATE
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order_Items table
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    price_per_unit DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- Create Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

-- Insert dummy data into Customers table
INSERT INTO Customers (customer_name, email, signup_date) VALUES
('Alice', 'alice@example.com', '2022-01-15'),
('Bob', 'bob@example.com', '2022-03-20'),
('Charlie', 'charlie@example.com', '2021-11-05'),
('David', 'david@example.com', '2023-02-12'),
('Eva', 'eva@example.com', '2023-05-07'),
('Frank', 'frank@example.com', '2022-06-10'),
('Grace', 'grace@example.com', '2022-07-14'),
('Hannah', 'hannah@example.com', '2022-09-20'),
('Ivy', 'ivy@example.com', '2023-01-25'),
('Jack', 'jack@example.com', '2023-02-10');

-- Insert dummy data into Products table
INSERT INTO Products (product_name, category) VALUES
('Laptop', 'Electronics'),
('Smartphone', 'Electronics'),
('Shoes', 'Fashion'),
('T-Shirt', 'Fashion'),
('Headphones', 'Electronics'),
('Watch', 'Accessories'),
('Bag', 'Fashion'),
('Tablet', 'Electronics'),
('Keyboard', 'Electronics'),
('Sunglasses', 'Accessories'),
('Dress', 'Fashion');

-- Insert dummy data into Orders table
INSERT INTO Orders (customer_id, order_date, total_amount) VALUES
(1, '2023-06-10', 200.00), -- Alice's 1st order
(1, '2023-08-14', 300.00), -- Alice's 2nd order
(2, '2023-07-22', 150.00), -- Bob's 1st order
(3, '2023-06-15', 400.00), -- Charlie's 1st order
(4, '2023-08-10', 500.00), -- David's 1st order
(1, '2023-01-10', 150.00),  -- Alice's 3rd order
(2, '2023-05-15', 220.00),  -- Bob's 2nd order
(3, '2023-03-12', 130.00),  -- Charlie's 2nd order
(5, '2023-07-25', 400.00),  -- Eva's 2nd order
(6, '2023-03-19', 520.00),  -- Frank's 1st order
(6, '2023-06-21', 350.00),  -- Frank's 2nd order
(7, '2023-02-10', 180.00),  -- Grace's 1st order
(8, '2023-07-14', 90.00),   -- Hannah's 1st order
(9, '2023-08-05', 600.00),  -- Ivy's 1st order
(10, '2023-08-20', 420.00), -- Jack's 1st order
(7, '2023-07-12', 320.00), -- Grace's 2nd order
(1, '2024-08-10', 250.00),  -- Alice's new order
(2, '2024-09-01', 150.00),  -- Bob's new order
(3, '2024-08-20', 320.00),  -- Charlie's new order
(4, '2024-07-15', 400.00),  -- David's new order
(5, '2024-08-05', 350.00),  -- Eva's new order
(1, '2024-08-10', 250.00),   -- Alice's new order
(2, '2024-09-01', 150.00),   -- Bob's new order
(3, '2024-08-20', 320.00),   -- Charlie's new order
(4, '2024-07-15', 400.00),   -- David's new order
(5, '2024-08-05', 350.00),   -- Eva's new order
(6, '2024-06-25', 600.00),   -- Frank's new order
(7, '2024-05-12', 200.00),   -- Grace's new order
(8, '2024-08-15', 450.00),   -- Hannah's new order
(9, '2024-09-02', 380.00),   -- Ivy's new order
(10, '2024-07-28', 500.00);  -- Jack's new order

-- Insert dummy data into Order_Items table
INSERT INTO Order_Items (order_id, product_id, quantity, price_per_unit) VALUES
(1, 1, 1, 200.00),  -- Alice bought 1 Laptop
(2, 2, 1, 300.00),  -- Alice bought 1 Smartphone
(3, 3, 2, 75.00),   -- Bob bought 2 Shoes
(4, 1, 2, 200.00),  -- Charlie bought 2 Laptops
(5, 5, 5, 100.00),  -- David bought 5 Headphones
(1, 3, 2, 75.00),    -- Alice bought 2 Tablets
(2, 4, 1, 300.00),   -- Alice bought 1 Smartphone
(3, 2, 1, 150.00),   -- Bob bought 1 Bag
(4, 1, 1, 400.00),   -- Charlie bought 1 Laptop
(5, 3, 2, 100.00),   -- Eva bought 2 Tablets
(6, 5, 1, 520.00),   -- Frank bought 1 Sunglasses
(7, 2, 2, 90.00),    -- Frank bought 2 Bags
(8, 6, 1, 180.00),   -- Grace bought 1 Dress
(9, 4, 1, 90.00),    -- Hannah bought 1 Keyboard
(10, 1, 1, 600.00),  -- Ivy bought 1 Laptop
(11, 7, 2, 210.00),  -- Jack bought 2 Watches
(12, 5, 1, 400.00),  -- Jack bought 1 Sunglasses
(13, 6, 1, 320.00), -- Grace bought 1 Dress
(14, 3, 1, 250.00),   -- Alice bought 1 Tablet
(15, 2, 1, 150.00),   -- Bob bought 1 Bag
(16, 1, 1, 320.00),   -- Charlie bought 1 Laptop
(17, 5, 2, 200.00),   -- David bought 2 Sunglasses
(18, 4, 2, 175.00),   -- Eva bought 2 Keyboards
(14, 3, 1, 250.00),   -- Alice bought 1 Tablet
(15, 2, 1, 150.00),   -- Bob bought 1 Bag
(16, 1, 1, 320.00),   -- Charlie bought 1 Laptop
(17, 5, 2, 200.00),   -- David bought 2 Sunglasses
(18, 4, 2, 175.00),   -- Eva bought 2 Keyboards
(19, 1, 1, 600.00),   -- Frank bought 1 Laptop
(20, 6, 1, 200.00),   -- Grace bought 1 Dress
(21, 4, 3, 150.00),   -- Hannah bought 3 Keyboards
(22, 7, 2, 190.00),   -- Ivy bought 2 Watches
(23, 2, 2, 250.00);   -- Jack bought 2 Bags


-- -------------Task 1 Query-------------

-- Step 1: Calculate the total spending per customer per category in the last year
-- Step 2: Calculate the most purchased category for each customer
-- Step 3: Calculate the total amount spent by each customer
-- Step 4: Combine the results and get the top 5 customers


WITH CustomerSpending AS (
    SELECT 
        o.customer_id,
        c.customer_name,
        c.email,
        p.category,
        SUM(oi.quantity * oi.price_per_unit) AS category_spent
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    JOIN Order_Items oi ON o.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
    WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)  -- Consider only orders from the last year
    GROUP BY o.customer_id, p.category
),
MaxCategorySpending AS (
    SELECT cs1.customer_id, cs1.category AS most_purchased_category
    FROM CustomerSpending cs1
    LEFT JOIN CustomerSpending cs2
        ON cs1.customer_id = cs2.customer_id 
        AND cs1.category_spent < cs2.category_spent
    WHERE cs2.customer_id IS NULL  -- Ensure we get only the max category spent per customer
),
TotalCustomerSpending AS (
    SELECT 
        o.customer_id,
        SUM(oi.quantity * oi.price_per_unit) AS total_spent
    FROM Orders o
    JOIN Order_Items oi ON o.order_id = oi.order_id
    WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)  -- Consider only orders from the last year
    GROUP BY o.customer_id
)
SELECT 
    tcs.customer_id,
    c.customer_name,
    c.email,
    tcs.total_spent,
    mcs.most_purchased_category
FROM TotalCustomerSpending tcs
JOIN Customers c ON tcs.customer_id = c.customer_id
JOIN MaxCategorySpending mcs ON tcs.customer_id = mcs.customer_id
ORDER BY tcs.total_spent DESC
LIMIT 5;

