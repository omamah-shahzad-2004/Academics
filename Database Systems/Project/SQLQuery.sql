Create Database DFMS;
Use DFMS;

-- Administrator Login Table
CREATE TABLE AdministratorLogin (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

INSERT INTO [AdministratorLogin] ([username], [password])
VALUES ('John Doe', '123123')


-- Cow Records Table
CREATE TABLE CowRecords (
    animalID INT PRIMARY KEY,
    earID VARCHAR(20) UNIQUE NOT NULL,
    animalType VARCHAR(50) NOT NULL,
    color VARCHAR(50),
    breed VARCHAR(50),
    birthDate DATE,
    weightAtBirth DECIMAL(10,2),
);

-- Daily Milk Production Table
CREATE TABLE DailyMilkProduction (
    date DATE NOT NULL,
    cowID INT,
    amMilkQuantity DECIMAL,
    noonMilkQuantity DECIMAL,
    pmMilkQuantity DECIMAL,
    --FOREIGN KEY (cowID) REFERENCES CowRecords(animalID)
);

-- Employees Table
CREATE TABLE Employees (
    employeeID INT PRIMARY KEY,
	employeeName VARCHAR(50),
	salary INT
);

-- DailyExpenses Table
CREATE TABLE DailyExpenses (
    dateIncurred DATE,
	expensesType VARCHAR(100),
	expensesAmount INT
);

-- DailyIncome Table
CREATE TABLE DailyIncome (
    dateReceived DATE,
	incomeType VARCHAR(100),
	incomeAmount INT
);

-- MilkSale Table
CREATE TABLE MilkSale (
	clientId INT PRIMARY KEY,
    date DATE,
	name VARCHAR(100),
	contact VARCHAR(100),
	amountBought DECIMAL
);









