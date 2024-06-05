CREATE TABLE tEmployee (
    EmpNo INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    JobTitle VARCHAR(100),
    HireDate DATE,
    Salary DECIMAL(10, 2),
    DeptNo INT
);

CREATE TABLE tDepartment (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(100),
    Location VARCHAR(100)
);

--------------------------------------

-- Create Hotel table
CREATE TABLE Hotel (
    hotelNo INT PRIMARY KEY,
    hotelName VARCHAR(100),
    City VARCHAR(100)
);

-- Create Room table
CREATE TABLE Room (
    roomNo INT PRIMARY KEY,
    hotelNo INT,
    roomType VARCHAR(50),
    price DECIMAL(10, 2),
    FOREIGN KEY (hotelNo) REFERENCES Hotel(hotelNo)
);

-- Create Booking table
CREATE TABLE Booking (
    hotelNo INT,
    guestNo INT,
    dateFrom DATE,
    dateTo DATE,
    roomNo INT,
    FOREIGN KEY (hotelNo) REFERENCES Hotel(hotelNo),
    FOREIGN KEY (roomNo) REFERENCES Room(roomNo)
);

-- Create Guest table
CREATE TABLE Guest (
    guestNo INT PRIMARY KEY,
    guestName VARCHAR(100),
    guestAddress VARCHAR(200)
);