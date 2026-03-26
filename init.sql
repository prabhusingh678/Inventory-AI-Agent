CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    name TEXT,
    stock INT
);

INSERT INTO inventory (name, stock)
VALUES 
('laptop', 10),
('mouse', 50);