# Python Flask Project

## Project Overview

This is a Python Flask project designed to manage and interact with a MySQL database. The project involves creating and managing various tables, including those for company details, photographers, users, and more. The project uses Flask for the web framework and interacts with MySQL using the `mysql-connector-python` library.

## Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Pydantic**
- **MySQL Connector/Python**
- **python-dotenv** (for environment variables)

## Installation Guide

### Setup the Environment

1. **Install Dependencies**

    Install the necessary Python libraries by running:

    ```bash
    pip install python-dotenv flask pandas pydantic mysql-connector-python
    ```

2. **Setup the Database**

    Create the necessary tables in your MySQL database by executing the following SQL commands. These commands will create the required schema for the project.

    ```sql
    -- Create DBSetting Table
    CREATE TABLE DBSetting (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user VARCHAR(50),
        password VARCHAR(50),
        host VARCHAR(50),
        dbname VARCHAR(50)
    );

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
        ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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

    -- Create LoginDetails Table
    CREATE TABLE LoginDetails (
        login_id INT AUTO_INCREMENT PRIMARY KEY,
        mobile VARCHAR(20),
        email VARCHAR(255) UNIQUE,
        password VARCHAR(255) NOT NULL,
        isActive BIT,
        UserType INT,
        AccessToken VARCHAR(100),
        LastLoginDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

    -- Create CountryMas Table
    CREATE TABLE CountryMas (
        CountryId INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(50),
        ISO VARCHAR(50),
        Currency VARCHAR(50),
        PhoneCode VARCHAR(10),
        Longitude DECIMAL(20, 20),
        Latitude DECIMAL(20, 20),
        CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

    -- Create StateMas Table
    CREATE TABLE StateMas (
        StateId INT AUTO_INCREMENT PRIMARY KEY,
        CountryId INT,
        Name VARCHAR(50),
        ISO VARCHAR(50),
        CountryCode VARCHAR(50),
        PhoneCode VARCHAR(10),
        Longitude DECIMAL(20, 20),
        Latitude DECIMAL(20, 20),
        CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (CountryId) REFERENCES CountryMas(CountryId)
    );

    -- Create CityMas Table
    CREATE TABLE CityMas (
        CityId INT AUTO_INCREMENT PRIMARY KEY,
        CountryId INT,
        StateId INT,
        Name VARCHAR(50),
        CountryCode VARCHAR(50),
        StateCode VARCHAR(50),
        Longitude DECIMAL(20, 20),
        Latitude DECIMAL(20, 20),
        CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (CountryId) REFERENCES CountryMas(CountryId),
        FOREIGN KEY (StateId) REFERENCES StateMas(StateId)
    );

    -- Add an index to the photographer_id in User for better performance
    CREATE INDEX idx_photographer_id ON User (photographer_id);
    ```

## Configuration

1. **Create a `.env` File**

    Create a `.env` file in the root directory of your project to store environment variables, such as database credentials:

    ```
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_NAME=your_db_name
    ```

2. **Load Environment Variables**

    Use the `python-dotenv` library to load environment variables from the `.env` file in your Flask application.

## Running the Project

1. **Start the Flask Application**

    Run the Flask application using:

    ```bash
    flask run
    ```

2. **Access the Application**

    Open your browser and navigate to `http://localhost:5000` to access the application.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Contact

For any inquiries, you can reach me at:
- **Email**: your-email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)
