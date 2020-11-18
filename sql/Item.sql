CREATE TABLE Item(
    id INT,
    quantity INT,
    product_id INT,
    purchase_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(product_id) REFERENCES Product(id),
    FOREIGN KEY(purchase_id) REFERENCES Purchase(id)
);