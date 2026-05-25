# Business Intelligence ETL Project

## Destination Schema
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

---

## Model Creation
To create models easier, there is a tool that we can use to auto generate the model files. To use it, run the following command in the terminal:

```shell
sqlacodegen_v2 mysql+pymysql://root:password@localhost/database_name --outfile models.py
```
- This tool is in the `sqlacodegen_v2` package, so make sure to install it first using pip if you haven't already.
    ```shell
    pip install sqlacodegen-v2
    ```

