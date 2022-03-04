1. What are the different tables present in MySQL?
InnoDB
MyISAM (Default)

2. How do you add a column in MySQL?
ALTER TABLE table_name
ADD column_name datatype;

3. How do you add a table? How about delete?
CREATE TABLE table_name( 
    column1 datatype
);
DROP TABLE table_name;

4. How would you add a foreign/primary key?
You can either add it in the CREATE TABLE statement or ALTER TABLE to add it later.

CREATE TABLE Test (
    testID int NOT NULL,
    test2ID int,
    PRIMARY KEY (testID),
    FOREIGN KEY (test2ID) REFERENCES Test2(test2ID)
);

ALTER TABLE Test
ADD FOREIGN KEY (test2ID) REFERENCES Test2(test2ID);

ALTER TABLE Test
ADD PRIMARY KEY (testID);

5. How do you connect to MySQL?
On Windows just type in your username and password that you set up
On Linux run <mysql -u root -p> there will be a password prompt

6. Change table name
RENAME old_table_name TO new_table_name;