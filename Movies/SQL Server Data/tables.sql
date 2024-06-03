-- Create Directors table
CREATE TABLE Directors (
    DirectorID INT PRIMARY KEY,
    DirectorName VARCHAR(100),
    CategoryID INT,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Create Genres table
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY,
    GenreName VARCHAR(100),
    AgeGuide VARCHAR(10),
    Notes VARCHAR(MAX)
);

-- Create Categories table
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100),
    Notes VARCHAR(MAX)
);

-- Create Movies table
CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(255),
    DirectorID INT,
    ReleaseDate DATE,
    MovieLength INT,
    GenreID INT,
    CategoryID INT,
    Rating VARCHAR(10),
    Notes VARCHAR(MAX),
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID),
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
