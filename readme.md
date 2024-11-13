# python ETL Task 

APIs for http://127.0.0.1:5000/process_data

## ETL Process Execution

The ETL process is triggered by invoking the API endpoint, which performs the following steps:

1. **Data Ingestion**: 
   - The endpoint loads raw data from MySQL, reading it into a Pandas DataFrame for easy manipulation and transformation.

2. **Data Transformation**: 
   - Within the DataFrame, business rules are applied to transform the data, including calculations for total sales, net sales, region identification, and removal of any duplicates or invalid records.

3. **Data Load**: 
   - The transformed data is loaded back into the MySQL database, where it can be stored and queried as needed. 
   - If existing data is found, the table is replaced or updated with the new, transformed data.

4. **Data Analysis**:
   - SQL queries are executed on the transformed data to retrieve analysis metrics, such as:
     - Total sales count
     - Sales amount by region
     - Average sales amount per transaction
     - Duplicate Order ID checks

5. **JSON Response**:
   - The results of the analysis are returned in JSON format, providing a structured and easy-to-use output of the sales analysis.

By following these steps, the ETL pipeline efficiently loads, transforms, and analyzes the data, providing comprehensive insights into the sales data in a single API call.


## Setup your development environment
### Clone the repository 

    git clone https://github.com/Arjun-Shrivas/python-ETL.git
    cd Python-ETL

### Initialize a virtual environment

    python3.8 -m venv venv
    source venv/bin/activate

### Install required packages

    source venv/bin/activate
    pip install -r requirements.txt


### Create the development database

    mysql -u root -p
    CREATE USER 'root'@'localhost' IDENTIFIED BY 'pass123';
    CREATE DATABASE sales_db;
    GRANT ALL PRIVILEGES ON sales_db.* TO 'root'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;

## Run the development server in Linux

Run with default port 5000

    source venv/bin/activate
    python app.py

## Update the list of dependencies

    pip freeze > requirements.txt
