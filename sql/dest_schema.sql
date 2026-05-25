CREATE DATABASE IF NOT EXISTS `orderStatistics`;
USE `orderStatistics`;


-- Which city has the best market for sales?
CREATE TABLE IF NOT EXISTS `Dim_Sales` (
    `location_id` INT AUTO_INCREMENT PRIMARY KEY,
    `customer_city` VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Fact_Sales` (
    `sales_id` INT AUTO_INCREMENT PRIMARY KEY,
    `location_id` INT NOT NULL,
    `total_revenue` DECIMAL(10, 2) NOT NULL,
    `total_orders` INT NOT NULL,
    CONSTRAINT `fk_fact_sales_location` FOREIGN KEY (`location_id`) REFERENCES `Dim_Sales` (`location_id`)
);



-- Which product has the highest sales?
CREATE TABLE IF NOT EXISTS `Dim_Product_Sales` (
    `product_code` VARCHAR(15) PRIMARY KEY,
    `product_name` VARCHAR(70) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Fact_Product_Sales` (
    `product_sales_id` INT AUTO_INCREMENT PRIMARY KEY,
    `product_code` VARCHAR(15) NOT NULL,
   
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL,
   
    CONSTRAINT `fk_fact_product_code` FOREIGN KEY (`product_code`) REFERENCES `Dim_Product_Sales` (`product_code`)
);


-- Which office provides the best sales support?
CREATE TABLE IF NOT EXISTS `Dim_Office_Sales` (
    `office_code` VARCHAR(10) PRIMARY KEY,
    `office_city` VARCHAR(50) NOT NULL,
    `sales_rep_employee_number` INT UNSIGNED NOT NULL
);

CREATE TABLE IF NOT EXISTS `Fact_Office_Sales` (
    `office_sales_id` INT AUTO_INCREMENT PRIMARY KEY,
    `office_code` VARCHAR(10) NOT NULL,
    `sales_rep_employee_number` INT UNSIGNED NOT NULL,
    
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL,
    
    CONSTRAINT `fk_fact_office_code` FOREIGN KEY (`office_code`) REFERENCES `Dim_Office_Sales` (`office_code`)
);


-- Which sales rep generates the most revenue?
CREATE TABLE IF NOT EXISTS `Dim_Employee_Revenue` (
    `employee_number` INT UNSIGNED PRIMARY KEY,
    `employee_name` VARCHAR(100) NOT NULL,
    `office_city` VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Fact_Employee_Revenue` (
    `employee_revenue_id` INT AUTO_INCREMENT PRIMARY KEY,
    `employee_number` INT UNSIGNED NOT NULL,
    `office_code` VARCHAR(10) NOT NULL,
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL,
    CONSTRAINT `fk_fact_employee_number` FOREIGN KEY (`employee_number`) REFERENCES `Dim_Employee_Revenue` (`employee_number`)
);


-- Which product line generates the most revenue?
CREATE TABLE IF NOT EXISTS `Dim_Product_Line_Revenue` (
    `product_line` VARCHAR(50) PRIMARY KEY,
    `product_line_description` VARCHAR(4000) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Fact_Product_Line_Revenue` (
    `product_line_revenue_id` INT AUTO_INCREMENT PRIMARY KEY,
    `product_line` VARCHAR(50) NOT NULL,
    `total_revenue` DECIMAL(10, 2) NOT NULL, 
    `total_orders` INT NOT NULL,
    CONSTRAINT `fk_fact_product_line` FOREIGN KEY (`product_line`) REFERENCES `Dim_Product_Line_Revenue` (`product_line`)
);
