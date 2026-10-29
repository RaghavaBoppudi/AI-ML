-- Clean up sample tests first
DROP TABLE sample_table_2; -- Completely delete the child table first

DROP TABLE sample_table; -- Completely delete the parent table next

DROP DATABASE sample_db; -- Completely delete the sample database

-- Creating Database / schema and tables (Data Definition Language)

CREATE DATABASE IF NOT EXISTS sample_db; -- create a sample database
USE sample_db; -- use the database

CREATE TABLE IF NOT EXISTS sample_table ( -- create a sample table
    UserID INT NOT NULL UNIQUE PRIMARY KEY, -- type of id in integer and it will be unique and not null
    Username VARCHAR (10) UNIQUE, -- type of username is a variable character with a limit of 10
    First_Name VARCHAR (10),
    Last_Name VARCHAR (10),
    UNIQUE (UserID, Username) -- IMPORTANT to create a composite key
);


-- Inserting Data into tables (Data Manipulation Language)

INSERT into sample_table (UserID, Username, First_Name, Last_Name)
VALUES
(1, 'rvbpd', 'Raghava', 'Boppudi'),
(2, 'janedoe', 'Jane', 'Doe'),
(3, 'johnsmith', 'John', NULL); -- Use NULL for empty cells - never leave it out

create table if not exists sample_table_2 (
    OrderID INT NOT NULL UNIQUE PRIMARY KEY,
    -- when declaring a FOREIGN KEY, declare the column first and then the CONSTRAINT
    OrderName VARCHAR (10), -- column definition
    UserID INT, -- column definition
    FOREIGN KEY (UserID, OrderName) REFERENCES sample_table(UserID, Username) -- Composite Foreign Key


);

INSERT INTO sample_table_2 (OrderID, OrderName, UserID) VALUES (3, 'johnsmith', 3);

-- Add a new column into a TABLE

ALTER TABLE sample_table
ADD emailID VARCHAR (25),
ADD Age INT CHECK (Age>=18);

-- Rename a column

ALTER TABLE sample_table
RENAME COLUMN Last_name TO SurName;

-- UPDATE is used to update rows, not INSERT.

-- USED CLAUDE HERE - READ FURTHER

UPDATE sample_table SET emailID = 'raghavaboppudi@icloud.com' WHERE UserID = 1;
UPDATE sample_table SET emailID = 'janedoe@gmail.com'         WHERE UserID = 2;
UPDATE sample_table SET emailID = 'johnsmith@gmail.com'       WHERE UserID = 3;

UPDATE sample_table SET Age = 25 WHERE UserID = 1;
UPDATE sample_table SET Age = 30 WHERE UserID = 2;
UPDATE sample_table SET Age = 35 WHERE UserID = 3;

SELECT * FROM sample_table; -- Display Table