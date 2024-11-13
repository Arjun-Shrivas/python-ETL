# python ETL Task 

APIs for http://127.0.0.1:5000/process_data

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