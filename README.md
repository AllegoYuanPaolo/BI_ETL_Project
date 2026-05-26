# Business Intelligence ETL Project

# Table of Contents
- [Business Intelligence ETL Project](#business-intelligence-etl-project)
- [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Tech Stack](#tech-stack)
  - [Walkthrough](#walkthrough)
  - [KPIs to Address](#kpis-to-address)
    - [1. Which city has the best market for sales?](#1-which-city-has-the-best-market-for-sales)
    - [2. Which product has the highest sales?](#2-which-product-has-the-highest-sales)
    - [3. Which office rpovides the best sales support?](#3-which-office-rpovides-the-best-sales-support)
    - [4. Which Sales Rep Generates the most revenue?](#4-which-sales-rep-generates-the-most-revenue)
    - [5. Which product line generates the most revenue?](#5-which-product-line-generates-the-most-revenue)
  - [API Enpoints](#api-enpoints)
    - [`/sales` Endpoints](#sales-endpoints)
      - [1. `GET /sales/cities`](#1-get-salescities)
      - [2. `GET /sales/offices`](#2-get-salesoffices)
      - [3. `GET /sales/products`](#3-get-salesproducts)
      - [4. `GET /sales/employee`](#4-get-salesemployee)
      - [5. `GET /sales/product_line`](#5-get-salesproduct_line)
  - [Auxiliary Information](#auxiliary-information)
    - [Model Creation](#model-creation)


## Overview
- This ETL Project's focus is on building a data pipeline, dashboard, and data visualization.  This codebase focuses on the backend code where the pipeline between the two databases: `orderTracking` and `orderStatistics`
## Tech Stack
- The project codebase is comprised of Python
  - FastAPI framework to create APIs and routes
  - Uvicorn to run the web server
  - SQAlchemy as the ORM framework
  - PyMySQL for the MySQL driver
- All of the `pip` dependencies are listed on [requirements.txt](requirements.txt) 

## Walkthrough
- To recreate the database setup that has been used for this codebase; you will find an [`sql file`](sql/db/full_project_db.sql) that contains the database structure and contents
  - This was created with the command:
    ```shell
    mysqldump -u root --databases ordertracking orderstatistics > sql/db/full_project_db.sql
    ```
    - It creates a dump of both databases into a single `.sql` file
  - To use this, follow the given commands:
    ```shell
    C:\path\to\project> mysql -u root
    ...
    mysql> source sql/db/full_project_db.sql
    ```
    - This executes the script in the `.sql` file and recreates the both `orderTracking` and `orderStatistics` database onto your environtment

- To install the `pip` dependencies, create a Virtual ENVirontment first or venv
    ```shell
    cd project/root/path
    python -m venv .venv
    ```
  - This will create a `.venv/` in the project root directory where it will have an isolated python interpreter and packages from the global packages
  - It will automatically open and use the venv; you can confirm this if your terminal looks like so:
    ```shell
    C:\path\to\project>          # venv is not active
    (.venv) C:\path\to\project>  # venv is active
    ```

- Next, use the following command to install the dependencies:
    ```shell
    pip install -r requirements.text
    ```
    - `pip`, or Python's package manager, will recursively install all the listed `requirements.txt`

- To run the web server, simply just run `./main.py` either from the VS Code GUI or by using `python main.py` in the terminal
  - You will now be able to access it via `http://localhost:5010`
    - Opening this should show a JSON message of:
    ```json
    {
        "message": "it works!(✿◕‿◕✿)"
    }
    ```




## KPIs to Address
- These KPIs (Key Performance Indicators) all involve the revenues of various entities involved in the sample business database.  However, an additional metric has been added to provide more insight to the business; Average Order Value (`aov`)
  - This measures the average value of the revenue per order
    - Computed by: `total_revenue` / `total_orders`
### 1. Which city has the best market for sales?
- This question can be answered by computing the total sales and total orders (`total_revenue` and `total_orders`) for each city and then comparing them to find out which city has the highest sales.

**Schema:**
```sql
CREATE TABLE IF NOT EXISTS `Fact_Sales` (
    `sales_id` INT AUTO_INCREMENT PRIMARY KEY,

    `location_id` VARCHAR(50) NOT NULL,
    `total_revenue` DECIMAL(10, 2) NOT NULL,
    `total_orders` INT NOT NULL,
    
);

CREATE TABLE IF NOT EXISTS `Dim_Sales` (
    `location_id` INT AUTO_INCREMENT PRIMARY KEY,
    `customer_city` VARCHAR(50) NOT NULL
);
```
- The source data will be transformed as:
  -  `total_revenue` = `COUNT(order_id)` * `order_total_price` (as grouped by `customer_city`)'
  -  `total_orders` = `COUNT(order_id)` (as grouped by `customer_city`)'

**Logic**
- Since the `Customer` object has a relationship with `Orders` and can be accessed through it, we can use the `customer_city` attribute from the `Customer` object to group the orders and compute the total revenue and total orders for each city. This will allow us to determine which city has the best market for sales.



### 2. Which product has the highest sales?
- This question can be answered by computing the total sales and total orders (`total_revenue` and `total_orders`) for each product and then comparing them to find out which product has the highest sales.

Schema:
```sql
CREATE TABLE IF NOT EXISTS `Fact_Product_Sales` (
    `product_sales_id` INT AUTO_INCREMENT PRIMARY KEY,
    `product_code` INT NOT NULL,
    
    `total_revenue` DECIMAL(10, 2) NOT NULL,
    `total_orders` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Dim_Product_Sales` (
    `product_code` INT AUTO_INCREMENT PRIMARY KEY,
    `product_name` VARCHAR(50) NOT NULL,
);
```
- The source data will be transformed as:
  -  `total_revenue` = `COUNT(order_id)` * `order_total_price` (as grouped by `product_code`)'
  -  `total_orders` = `COUNT(order_id)` (as grouped by `product_code`)'

### 3. Which office rpovides the best sales support?
- This question can be answered by computing the total sales and total orders (`total_revenue` and `total_orders`) for each office and then comparing them to find out which office provides the best sales support.
Schema:
```sql
CREATE TABLE IF NOT EXISTS `Fact_Office_Sales` (
    `office_sales_id` INT AUTO_INCREMENT PRIMARY KEY,
    `office_code` INT NOT NULL,
    
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Dim_Office_Sales` (
    `office_code` VARCHAR(10) PRIMARY KEY,
    `office_city` VARCHAR(50) NOT NULL,
);
```
- The source data will be transformed as:
  -  `total_revenue` = `COUNT(order_id)` * `order_total_price` (as grouped by `office_code`)'
  -  `total_orders` = `COUNT(order_id)` (as grouped by `office_code`)'

### 4. Which Sales Rep Generates the most revenue?
- This question can be answered by computing the total sales (`total_revenue`) of for each sales representative and then comparing them to find out which employee has the most revenue
- Additionally, the total number of orders (`total_orders`) per employee, and their office location (`office_city`) will be taken into account

Schema:
```sql
CREATE TABLE IF NOT EXISTS `Fact_Employee_Renevue` (
    `employee_revenue_id` INT AUTO_INCREMENT PRIMARY KEY,
    `employee_number` INT NOT NULL,
    `office_code` VARCHAR(10) NOT NULL,
    
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Dim_Employee_Revenue` (
    `employee_number` INT AUTO_INCREMENT PRIMARY KEY,
    `employee_name` VARCHAR(50) NOT NULL,
    `office_city` VARCHAR(50) NOT NULL
);
```
- The source data will be transformed as:
  -  `total_revenue` = `COUNT(order_id)` * `order_total_price` (as grouped by `employee_number`)'
  -  `total_orders` = `COUNT(order_id)` (as grouped by `employee_number`)'

### 5. Which product line generates the most revenue?
- This question can be answered by computing the total sales (`total_revenue`) of for each product line and then comparing them to find out which product line generates the most revenue
- Additionally, the total number of orders (`total_orders`) per product line will be taken into account


Schema:
```sql
CREATE TABLE IF NOT EXISTS `Fact_Product_Line_Revenue` (
    `product_line_revenue_id` INT AUTO_INCREMENT PRIMARY KEY,
    `product_line` VARCHAR(50) NOT NULL,
    
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Dim_Product_Line_Revenue` (
    `product_line` VARCHAR(50) PRIMARY KEY,
    `product_line_description` VARCHAR(255) NOT NULL
);
```
- The source data will be transformed as:
  -  `total_revenue` = `COUNT(order_id)` * `order_total_price` (as grouped by `product_line`)'
  -  `total_orders` = `COUNT(order_id)` (as grouped by `product_line`)'


## API Enpoints
- There are two categories of the endpoints:
  - `/etl`
  - `/sales`

### `/sales` Endpoints
#### 1. `GET /sales/cities`
- This retrieves the total revenues by city, idenitified by it's location
- Data to receive:
    ```json
    [
        {
            "city": "string",
            "total_revenue": "float",
            "total_orders": "int",
            "aov": "float"
        }
    ]
    ```

#### 2. `GET /sales/offices`
- This retrieves the office revenues, idenitifed by it's location (city)
- Data to receive:
    ```json
    [
        {
            "office_city": "string",
            "total_revenue": "float",
            "total_orders": "int",
            "aov": "float"
        }
    ]
    ```

#### 3. `GET /sales/products`
- This retrieves the revenues of each products
- Data to receive:
    ```json
    [
        {
            "product": "string",
            "total_revenue": "float",
            "total_orders": "int",
            "aov": "float"
        }
    ]
    ```
#### 4. `GET /sales/employee`
- This retrieves the revenues of each sales representative
- Data to revceive:
    ```json
    [
        {
            "employee_number": "string",
            "employee_name": "string",
            "total_revenue": "float",
            "total_orders": "int",
            "aov": "float"
        }
    ]
    ```
#### 5. `GET /sales/product_line`
- This retrieves the revenues of each product line
- Data to receive:
    ```json
    [
        {
            "product_line": "string",
            "description": "string",
            "total_revenue": "float",
            "total_orders": "int",
            "aov": "float"
        }
    ]
    ```


## Auxiliary Information
### Model Creation
To create models easier, there is a tool that we can use to auto generate the model files. To use it, run the following command in the terminal:

```shell
sqlacodegen_v2 mysql+pymysql://root:password@localhost/database_name --outfile models.py
```
- This tool is in the `sqlacodegen_v2` package, so make sure to install it first using `pip` if you haven't already.
    ```shell
    `pip` install sqlacodegen-v2
    ```

