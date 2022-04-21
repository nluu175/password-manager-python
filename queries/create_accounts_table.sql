CREATE TABLE Accounts(
            Username varchar(50) NOT NULL,
            AppName varchar(50) NOT NULL,
            Password varchar(500) NOT NULL,
            LastUpdate timestamp NOT NULL,
            PRIMARY KEY (Username, AppName),
            FOREIGN KEY (Username) REFERENCES Users(Username) 
            );