CREATE TABLE Books (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year_published INT
);

INSERT INTO Books (id, title, author, year_published) VALUES
(1, 'The Wheel of Time', 'Robert Jordan', 1960),
(2, 'A Secret History', 'Donna Tartt', 1949),
(3, 'A Dance of Dragons', 'George R. R. Martin', 1813),
(4, 'Mistborn', 'Brandon Sanderson', 1925),
(5, 'Normal People', 'Sally Rooney', 1851);

SELECT * FROM Books;

SELECT * FROM Books WHERE author = 'Robert Jordan';

UPDATE Books SET year_published = 1950 WHERE id = 2;

DELETE FROM Books WHERE id = 5;

CREATE TABLE Borrowers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(id)
);

INSERT INTO Borrowers (id, name, book_id, borrow_date, return_date) VALUES
(1, 'Alice Johnson', 1, '2024-03-01', '2024-03-15'),
(2, 'Bob Smith', 3, '2024-03-05', '2024-03-20');
