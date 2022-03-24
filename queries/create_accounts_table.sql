CREATE TABLE Accounts(
            Username varchar(50) NOT NULL,
            DomainName varchar(50) NOT NULL,
            Password varchar(50) NOT NULL,
            LastUpdate timestamp NOT NULL,
            PRIMARY KEY (Username, DomainName),
            FOREIGN KEY (Username) REFERENCES Users(Username) 
            );