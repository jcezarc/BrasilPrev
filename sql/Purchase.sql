CREATE TABLE Purchase(
    id INT,
    sale_date DATE,
    customer_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(customer_id) REFERENCES Customer(id)
);