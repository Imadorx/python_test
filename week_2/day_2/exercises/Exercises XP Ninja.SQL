CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    product VARCHAR(100),
    amount DECIMAL
);

SELECT first_name, last_name
FROM customers
ORDER BY last_name ASC, first_name ASC
LIMIT 2;


SELECT first_name, last_name
FROM customers
ORDER BY last_name DESC, first_name DESC
LIMIT 2;

DELETE FROM purchases
WHERE customer_id IN (
    SELECT id FROM customers WHERE first_name = 'Scott'
);


SELECT * FROM customers WHERE first_name = 'Scott';


SELECT p.id AS purchase_id,
       p.product,
       p.amount,
       c.first_name,
       c.last_name
FROM purchases p
LEFT JOIN customers c ON p.customer_id = c.id;


SELECT p.id AS purchase_id,
       p.product,
       p.amount,
       c.first_name,
       c.last_name
FROM purchases p
INNER JOIN customers c ON p.customer_id = c.id;
