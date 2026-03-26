CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    quantity INT
);

INSERT INTO products (name, quantity) VALUES
('Laptop', 5),
('Mouse', 50),
('Keyboard', 8),
('Monitor', 15);