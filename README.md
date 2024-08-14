#Installation Guide


-- dotenv
pip install python-dotenv

-- flask
pip install flask 

-- pandas
pip install pandas

-- pydantic
pip install pydantic

-- mysql
pip install mysql-connector-python

-- DBSetting
Create table DBSetting
(
id int primary key Auto_Increment,
user varchar(50),
password varchar(50),
host varchar(50),
dbname varchar(50)
)

-- Create Company Table
CREATE TABLE Company (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
	ownername VARCHAR(255) NOT NULL,
    address VARCHAR(255),
	countryId INT,
	stateId INT,
	cityId INT,
	zipcode VARCHAR(20),
    mobile VARCHAR(20),
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
);

-- Create Photographer Table
CREATE TABLE Photographer (
    photographer_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    hire_date DATE,
	countryId INT,
	stateId INT,
	cityId INT,
	zipcode VARCHAR(20),
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES Company(company_id)
);

-- Create User Table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    photographer_id INT NOT NULL,
	first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
	countryId INT,
	stateId INT,
	cityId INT,
	zipcode VARCHAR(20),
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

-- Create LoginDetails
Create Table LoginDetails(
	login_id int AUTO_INCREMENT PRIMARY KEY,
	mobile VARCHAR(20),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) NOT NULL,
	isActive bit,
	UserType INT,
	AccessToken VARCHAR(100),
	LastLoginDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
)

-- Create CountryMas
CREATE Table CountryMas(
	CountryId int AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(50),
	ISO VARCHAR(50),
	Currency VARCHAR(50),
	PhoneCode VARCHAR(10),
	Longitude decimal(20, 20),
	Latitude decimal(20, 20),
	CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
);

-- Create StateMas
CREATE Table StateMas(
	StateId int AUTO_INCREMENT PRIMARY KEY,
	CountryId INT,
	Name VARCHAR(50),
	ISO VARCHAR(50),
	CountryCode VARCHAR(50),
	PhoneCode VARCHAR(10),
	Longitude decimal(20, 20),
	Latitude decimal(20, 20),
	CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (CountryId) REFERENCES CountryMas(CountryId)
)

-- Create CityMas
CREATE Table CityMas(
	CityId int AUTO_INCREMENT PRIMARY KEY,
	CountryId INT,
	StateId INT,
	Name VARCHAR(50),
	CountryCode VARCHAR(50),
	StateCode VARCHAR(50),
	Longitude decimal(20, 20),
	Latitude decimal(20, 20),
	CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (CountryId) REFERENCES CountryMas(CountryId)
	FOREIGN KEY (StateId) REFERENCES StateMas(StateId)
);

-- Add an index to the photographer_id in User for better performance
CREATE INDEX idx_photographer_id ON User (photographer_id);
