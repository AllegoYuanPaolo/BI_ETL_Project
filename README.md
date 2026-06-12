# Business Intelligence ETL Project
- Contributors:
  - Allego, Yuan Paolo A. 
  - Nale, Luther Ian S.
# Table of Contents
- [Business Intelligence ETL Project](#business-intelligence-etl-project)
- [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Tech Stack](#tech-stack)
  - [Walkthrough](#walkthrough)
    - [MySQL](#mysql)
    - [Python Venv](#python-venv)
    - [Web Server use](#web-server-use)
      - [Run Both Servers](#run-both-servers)
      - [Run Backend Server](#run-backend-server)
      - [Run Frontend Server](#run-frontend-server)
    - [API use](#api-use)
  - [KPIs to Address](#kpis-to-address)
    - [1. Which city has the best market for sales?](#1-which-city-has-the-best-market-for-sales)
    - [2. Which product has the highest sales?](#2-which-product-has-the-highest-sales)
    - [3. Which office rpovides the best sales support?](#3-which-office-rpovides-the-best-sales-support)
    - [4. Which Sales Rep Generates the most revenue?](#4-which-sales-rep-generates-the-most-revenue)
    - [5. Which product line generates the most revenue?](#5-which-product-line-generates-the-most-revenue)
  - [Filters](#filters)
  - [API Enpoints](#api-enpoints)
    - [`/etl` Endpoints](#etl-endpoints)
      - [1. `GET /etl/refresh`](#1-get-etlrefresh)
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
- The backend codebase is comprised of Python:
  - FastAPI framework to create APIs and routes
  - Uvicorn to run the web server
  - SQAlchemy as the ORM framework
  - PyMySQL for the MySQL driver
- All of the `pip` dependencies are listed on [requirements.txt](requirements.txt) 

- The frontend codebase is comprised of:
  - HTML
  - CSS
  - JavaScript (vanilla)
> *Frontend dev, please update this if you're using libraries/dependencies.  Then remove this message afterwards*


## Walkthrough
### MySQL
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

### Python Venv
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
  - If it doesn't work, run this command to manually activate the venv:
    ```shell
    C:\path\to\project> ./.venv/Scripts/activate.bat
    ```

- Next, use the following command to install the dependencies:
    ```shell
    pip install -r requirements.text
    ```
    - `pip`, or Python's package manager, will recursively install all the listed `requirements.txt`

### Web Server use
#### Run Both Servers
- To run the both backend and frontend server, simply only type `run_servers` in the terminal from the project root.  This is start two new cmd windows that will run the backend server (`app/main.py`) and the frontend server (`frontend/run.py`) 
  - PORTS:
    - Backend: 5010
    - Frontend: 5090
#### Run Backend Server
- To run the backend server, follow this command:
    ```shell
    (.venv) C:\path\to\project>run_back
    ```

#### Run Frontend Server
- To run the frontend server, follow this command:
    ```shell
    (.venv) C:\path\to\project>run_front
    ```


### API use
- To use the API endpoint, the JavaScript endpoint function is already provided below along with a usage example:
    ```javascript
    
    /**
    * @param {string} key - The name of then enpoint to call
    * @returns {Array<Object>} An array of objects from a JSON response
    * @throws {Error} if the fetch fails, it throws the HTTP Error code
    */
    async function load(key) {
        const r = await fetch(EP[key]);
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
    }

    ```

## KPIs to Address
- These KPIs (Key Performance Indicators) all involve the revenues of various entities involved in the sample business database.  However, an additional metric has been added to provide more insight to the business; Average Order Value (`aov`)
  - This measures the average value of the revenue per order
    - Computed by: `total_revenue` / `total_orders`

All KPIs are answered from a single unified star schema:

**Fact table:** `fact_sales` — each row is an order-detail line with FK references to 5 dimensions.
**Dimension tables:** `dim_city`, `dim_office`, `dim_sales_rep`, `dim_product`, `dim_product_line`

```sql
CREATE TABLE `fact_sales` (
  `order_id`       varchar(15)     NOT NULL,
  `order_date`     date            NOT NULL,
  `city_id`        int             NOT NULL,
  `office_id`      int             NOT NULL,
  `sales_rep_id`   int             NOT NULL,
  `product_id`     int             NOT NULL,
  `product_line_id` int            NOT NULL,
  `revenue`        decimal(10,2)   NOT NULL,
  `quantity`       int             NOT NULL,
  PRIMARY KEY (`order_id`, `product_id`),
  CONSTRAINT `fk_fact_city`        FOREIGN KEY (`city_id`)        REFERENCES `dim_city`        (`city_id`),
  CONSTRAINT `fk_fact_office`      FOREIGN KEY (`office_id`)      REFERENCES `dim_office`      (`office_id`),
  CONSTRAINT `fk_fact_sales_rep`   FOREIGN KEY (`sales_rep_id`)   REFERENCES `dim_sales_rep`   (`sales_rep_id`),
  CONSTRAINT `fk_fact_product`     FOREIGN KEY (`product_id`)     REFERENCES `dim_product`     (`product_id`),
  CONSTRAINT `fk_fact_product_line` FOREIGN KEY (`product_line_id`) REFERENCES `dim_product_line` (`product_line_id`)
);
```

Each KPI below simply joins `fact_sales` with the relevant dimension table and aggregates.

### 1. Which city has the best market for sales?
- This question can be answered by computing the total sales and total orders (`total_revenue` and `total_orders`) for each city and then comparing them to find out which city has the highest sales.

**How it's queried:** `fact_sales` is joined with `dim_city` on `city_id`, grouped by `city_name`.

```sql
SELECT dc.city_name,
       SUM(fs.revenue) AS total_revenue,
       COUNT(fs.order_id) AS total_orders
FROM fact_sales fs
JOIN dim_city dc ON fs.city_id = dc.city_id
GROUP BY dc.city_name;
```



### 2. Which product has the highest sales?
- This question can be answered by computing the total sales and total orders (`total_revenue` and `total_orders`) for each product and then comparing them to find out which product has the highest sales.

**How it's queried:** `fact_sales` is joined with `dim_product` on `product_id`, grouped by `product_name`.

```sql
SELECT dp.product_name,
       SUM(fs.revenue) AS total_revenue,
       COUNT(fs.order_id) AS total_orders
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
GROUP BY dp.product_name;
```

### 3. Which office provides the best sales support?
- This question can be answered by computing the total sales and total orders (`total_revenue` and `total_orders`) for each office and then comparing them to find out which office provides the best sales support.

**How it's queried:** `fact_sales` is joined with `dim_office` on `office_id`, grouped by `office_city`.

```sql
SELECT off.office_city,
       SUM(fs.revenue) AS total_revenue,
       COUNT(fs.order_id) AS total_orders
FROM fact_sales fs
JOIN dim_office off ON fs.office_id = off.office_id
GROUP BY off.office_city;
```

### 4. Which Sales Rep Generates the most revenue?
- This question can be answered by computing the total sales (`total_revenue`) of for each sales representative and then comparing them to find out which employee has the most revenue
- Additionally, the total number of orders (`total_orders`) per employee, and their office location (`office_city`) will be taken into account

**How it's queried:** `fact_sales` is joined with `dim_sales_rep` on `sales_rep_id` and with `dim_office` on `office_id`, grouped by sales rep.

```sql
SELECT dsr.sales_rep_name,
       off.office_city,
       SUM(fs.revenue) AS total_revenue,
       COUNT(fs.order_id) AS total_orders
FROM fact_sales fs
JOIN dim_sales_rep dsr ON fs.sales_rep_id = dsr.sales_rep_id
JOIN dim_office off ON fs.office_id = off.office_id
GROUP BY dsr.sales_rep_id;
```

### 5. Which product line generates the most revenue?
- This question can be answered by computing the total sales (`total_revenue`) of for each product line and then comparing them to find out which product line generates the most revenue
- Additionally, the total number of orders (`total_orders`) per product line will be taken into account

**How it's queried:** `fact_sales` is joined with `dim_product_line` on `product_line_id`, grouped by `product_line`.

```sql
SELECT dpl.product_line,
       SUM(fs.revenue) AS total_revenue,
       COUNT(fs.order_id) AS total_orders
FROM fact_sales fs
JOIN dim_product_line dpl ON fs.product_line_id = dpl.product_line_id
GROUP BY dpl.product_line;
```

## Filters
All `/sales` endpoints accept query parameters to narrow results. Parameters are optional — omit them to get unfiltered data.

### Common parameters (available on all `/sales` endpoints)

| Parameter | Type | Description | Example |
|---|---|---|---|
| `start_date` | `date` (YYYY-MM-DD) | Include orders on or after this date | `?start_date=2026-01-01` |
| `end_date` | `date` (YYYY-MM-DD) | Include orders on or before this date | `?end_date=2026-06-30` |
| `year` | `int` | Filter to a specific calendar year | `?year=2025` |
| `quarter` | `int` (1–4) | Filter to a specific quarter | `?quarter=3` |
| `half` | `int` (1–2) | Filter to a half-year (1 = Jan–Jun, 2 = Jul–Dec) | `?half=2` |

### Endpoint-specific parameters

| Parameter | Available on |
|---|---|
| `city` | `/cities`, `/offices`, `/employee` |
| `office_city` | `/offices`, `/employee` |

### Filter applicability matrix

| Endpoint | `start_date` / `end_date` | `year` | `quarter` | `half` | `city` | `office_city` |
|---|---|---|---|---|---|---|
| `/cities` | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| `/offices` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `/products` | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| `/employee` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `/product_line` | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |

### Example calls

```shell
# City revenue for 2025 only
curl "http://localhost:5010/sales/cities?year=2025"

# Products sold in Q4
curl "http://localhost:5010/sales/products?quarter=4"

# Office revenue for H2 (Jul–Dec)
curl "http://localhost:5010/sales/offices?half=2"

# Employees in the Makati office
curl "http://localhost:5010/sales/employee?office_city=Makati"

# City revenue for a specific city with a date range
curl "http://localhost:5010/sales/cities?city=Manila&start_date=2025-06-01&end_date=2025-12-31"

# Product line revenue from Jan 1, 2026 onward
curl "http://localhost:5010/sales/product_line?start_date=2026-01-01"
```

## API Enpoints
- There are two categories of the endpoints:
  - `/etl`
  - `/sales`

### `/etl` Endpoints
#### 1. `GET /etl/refresh`
- This triggers the entire pipeline to Extract, Transform, and Load--essentially refresing the data
- Data to receive:
  - If no errors are encountered:
    ```json
    {
        "status": "OK"
    }
    ```
  - If an error is encountered:
    ```json
    {
        "status": "ERROR",
        "messaage": "error message"
    }
    ```


### `/sales` Endpoints
#### 1. `GET /sales/cities`
- Retrieves total revenue grouped by city
- **Available filters:** `start_date`, `end_date`, `year`, `quarter`, `half`, `city`
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
- Example: `GET /sales/cities?city=Manila&year=2025`

#### 2. `GET /sales/offices`
- Retrieves total revenue grouped by office location (city)
- **Available filters:** `start_date`, `end_date`, `year`, `quarter`, `half`, `city`, `office_city`
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
- Example: `GET /sales/offices?half=2`

#### 3. `GET /sales/products`
- Retrieves total revenue grouped by product
- **Available filters:** `start_date`, `end_date`, `year`, `quarter`, `half`
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
- Example: `GET /sales/products?quarter=4`

#### 4. `GET /sales/employee`
- Retrieves total revenue grouped by sales representative
- **Available filters:** `start_date`, `end_date`, `year`, `quarter`, `half`, `city`, `office_city`
- Data to receive:
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
- Example: `GET /sales/employee?office_city=Makati`

#### 5. `GET /sales/product_line`
- Retrieves total revenue grouped by product line
- **Available filters:** `start_date`, `end_date`, `year`, `quarter`, `half`
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
- Example: `GET /sales/product_line?start_date=2026-01-01`


## Auxiliary Information
### Model Creation
To create models easier, there is a tool that we can use to auto generate the model files. To use it, run the following command in the terminal:

```shell
sqlacodegen_v2 mysql+pymysql://root:password@localhost/database_name --outfile models.py
```
- This tool is in the `sqlacodegen_v2` package, so make sure to install it first using `pip` if you haven't already.
    ```shell
    pip install sqlacodegen-v2
    ```


