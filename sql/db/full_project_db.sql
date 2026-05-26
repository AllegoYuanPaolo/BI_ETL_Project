-- MySQL dump 10.13  Distrib 9.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: orderTracking
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `orderTracking`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `orderTracking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `orderTracking`;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customerNumber` varchar(15) NOT NULL,
  `customerName` varchar(50) NOT NULL,
  `contactLastName` varchar(50) DEFAULT NULL,
  `contactFirstName` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `addressLine1` varchar(50) DEFAULT NULL,
  `addressLine2` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `postalCode` varchar(15) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `salesRepEmployeeNumber` int unsigned DEFAULT NULL,
  `creditLimit` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`customerNumber`),
  KEY `fk_employee` (`salesRepEmployeeNumber`),
  CONSTRAINT `fk_employee` FOREIGN KEY (`salesRepEmployeeNumber`) REFERENCES `employees` (`employeeNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('CUST001','Ryuujin Diecasts','Allego','Yuna','0918-898-4045','165 Shaw Blvd., Brgy. Bel-Air','Suite 692','Davao City','Davao del Sur','8000','Philippines',1076,5369.96),('CUST002','Santos\'s Toy Kingdom','Nale','Ian','0918-364-3193','997 EDSA, Brgy. Bagong Pag-asa','Suite 673','Paranaque','Metro Manila','1700','Philippines',1088,6014.38),('CUST003','Metro Auto-Miniatures','Espedido','Miguel ','0945-165-9025','377 Katipunan Ave., Brgy. Poblacion','Suite 274','Manila','Metro Manila','1000','Philippines',1002,7581.99),('CUST004','Villanueva\'s Retail Solutions','Salvador','Johan','0966-358-7418','889 Bonifacio St., Brgy. San Jose',NULL,'Iloilo City','Iloilo','5000','Philippines',1612,18585.30),('CUST005','Poe\'s Toy Emporium','Garcia','Dante','0922-453-6440','930 Quezon Ave., Brgy. Loyola Heights',NULL,'Manila','Metro Manila','1000','Philippines',1088,145373.00),('CUST006','Iloilo Diecast Hub','Ramos','Cory','0917-853-0212','518 Katipunan Ave., Brgy. Ugong',NULL,'Davao City','Davao del Sur','8000','Philippines',1002,100786.00),('CUST007','Cebu Miniature World','Sotto','Gloria','0956-803-0350','542 Quezon Ave., Brgy. Ugong',NULL,'Cagayan de Oro','Misamis Oriental','9000','Philippines',1286,174135.00),('CUST008','Baguio Collectibles','Lapid','Elena','0966-533-1598','207 Shaw Blvd., Brgy. Bel-Air',NULL,'Makati','Metro Manila','1200','Philippines',1621,79483.00),('CUST009','Ejercito\'s Collectibles','Dela Cruz','Maria','0920-202-8144','786 Rizal St., Brgy. San Jose',NULL,'Cebu City','Cebu','6000','Philippines',1625,136214.00),('CUST010','Marcos\'s Hobby Shop','Garcia','Teresa','0977-672-1330','231 Rizal St., Brgy. Ugong',NULL,'Pasig','Metro Manila','1600','Philippines',1621,186199.00),('CUST011','Pearl Hobbies & More','Marcos','Gloria','0977-349-0575','326 Rizal St., Brgy. San Jose',NULL,'Baguio','Benguet','2600','Philippines',1504,80777.00),('CUST012','Makati Trading Post','Ejercito','Ramon','0956-197-5461','65 Rizal St., Brgy. Ugong',NULL,'Baguio','Benguet','2600','Philippines',1501,146166.00),('CUST013','Castro\'s Diecast Hub','Poe','Gloria','0918-312-2430','98 Ayala Ave., Brgy. Loyola Heights',NULL,'Iloilo City','Iloilo','5000','Philippines',1002,115474.00),('CUST014','Castro\'s Wholesale Center','Ejercito','Cory','0945-573-9964','980 Rizal St., Brgy. Ugong',NULL,'Pasig','Metro Manila','1600','Philippines',1102,168132.00),('CUST015','Reyes\'s Toy Emporium','Flores','Teresa','0918-396-4615','153 Luna St., Brgy. Bagong Pag-asa',NULL,'Pasig','Metro Manila','1600','Philippines',1625,142800.00),('CUST016','Flores\'s Trading Post','Poe','Jose','0922-447-7975','501 EDSA, Brgy. Loyola Heights',NULL,'Davao City','Davao del Sur','8000','Philippines',1102,156365.00),('CUST017','Grand Collectibles','Reyes','Salvador','0956-550-4506','776 EDSA, Brgy. Bel-Air',NULL,'Iloilo City','Iloilo','5000','Philippines',1501,110865.00),('CUST018','Metro Hobbies & More','Lapid','Teresa','0922-405-8100','472 España Blvd., Brgy. Ugong',NULL,'Iloilo City','Iloilo','5000','Philippines',1102,176922.00),('CUST019','Baguio General Merchandise','Reyes','Liza','0918-604-9212','532 Katipunan Ave., Brgy. Bel-Air',NULL,'Davao City','Davao del Sur','8000','Philippines',1165,131910.00),('CUST020','Cavite Hobbies & More','Sotto','Teresa','0918-156-7678','568 Mabini St., Brgy. San Jose',NULL,'Makati','Metro Manila','1200','Philippines',1401,72893.00),('CUST021','Cavite Hobbies & More','Duterte','Liza','0917-443-8306','467 EDSA, Brgy. Ugong',NULL,'Taguig','Metro Manila','1630','Philippines',1337,122006.00),('CUST022','Robredo\'s Toy Kingdom','Aquino','Benigno','0922-942-2007','710 Shaw Blvd., Brgy. Loyola Heights',NULL,'Cagayan de Oro','Misamis Oriental','9000','Philippines',1056,173210.00),('CUST023','Global Retail Solutions','Bautista','Imelda','0966-390-8169','296 Quezon Ave., Brgy. Bagong Pag-asa',NULL,'Cebu City','Cebu','6000','Philippines',1323,78812.00),('CUST024','Makati Miniature World','Go','Isabel','0966-381-7390','931 EDSA, Brgy. Loyola Heights',NULL,'Davao City','Davao del Sur','8000','Philippines',1002,136311.00);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employeeNumber` int unsigned NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `extension` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `officeCode` varchar(10) NOT NULL,
  `reportsTo` int unsigned DEFAULT NULL,
  `jobTitle` varchar(50) NOT NULL,
  PRIMARY KEY (`employeeNumber`),
  KEY `reportsTo` (`reportsTo`),
  KEY `officeCode` (`officeCode`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`reportsTo`) REFERENCES `employees` (`employeeNumber`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`officeCode`) REFERENCES `offices` (`officeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1002,'Murphy','Diane','x5800','dmurphy@classicmodelcars.com','1',NULL,'President'),(1056,'Patterson','Mary','x4611','mpatter@classicmodelcars.com','1',1002,'VP Sales'),(1076,'Firrelli','Jeff','x9273','jfirrelli@classicmodelcars.com','1',1002,'VP Marketing'),(1088,'Patterson','William','x4871','wpatterson@classicmodelcars.com','6',1056,'Sales Manager (APAC)'),(1102,'Bondur','Gerard','x5408','gbondur@classicmodelcars.com','4',1056,'Sale Manager (EMEA)'),(1143,'Bow','Anthony','x5428','abow@classicmodelcars.com','1',1056,'Sales Manager (NA)'),(1165,'Jennings','Leslie','x3291','ljennings@classicmodelcars.com','1',1143,'Sales Rep'),(1166,'Thompson','Leslie','x4065','lthompson@classicmodelcars.com','1',1143,'Sales Rep'),(1188,'Firrelli','Julie','x2173','jfirrelli@classicmodelcars.com','2',1143,'Sales Rep'),(1216,'Patterson','Steve','x4334','spatterson@classicmodelcars.com','2',1143,'Sales Rep'),(1286,'Tseng','Foon Yue','x2248','ftseng@classicmodelcars.com','3',1143,'Sales Rep'),(1323,'Vanauf','George','x4102','gvanauf@classicmodelcars.com','3',1143,'Sales Rep'),(1337,'Bondur','Loui','x6493','lbondur@classicmodelcars.com','4',1102,'Sales Rep'),(1370,'Hernandez','Gerard','x2028','ghernande@classicmodelcars.com','4',1102,'Sales Rep'),(1401,'Castillo','Pamela','x2759','pcastillo@classicmodelcars.com','4',1102,'Sales Rep'),(1501,'Bott','Larry','x2311','lbott@classicmodelcars.com','7',1102,'Sales Rep'),(1504,'Jones','Barry','x102','bjones@classicmodelcars.com','7',1102,'Sales Rep'),(1611,'Fixter','Andy','x101','afixter@classicmodelcars.com','6',1088,'Sales Rep'),(1612,'Marsh','Peter','x102','pmarsh@classicmodelcars.com','6',1088,'Sales Rep'),(1619,'King','Tom','x103','tking@classicmodelcars.com','6',1088,'Sales Rep'),(1621,'Nishi','Mami','x101','mnishi@classicmodelcars.com','5',1056,'Sales Rep'),(1625,'Kato','Yoshimi','x102','ykato@classicmodelcars.com','5',1621,'Sales Rep'),(1702,'Gerard','Martin','x2312','mgerard@classicmodelcars.com','4',1102,'Sales Rep');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offices`
--

DROP TABLE IF EXISTS `offices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offices` (
  `officeCode` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `addressLine1` varchar(50) NOT NULL,
  `addressLine2` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `country` varchar(50) NOT NULL,
  `postalCode` varchar(15) NOT NULL,
  `territory` varchar(10) NOT NULL,
  PRIMARY KEY (`officeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offices`
--

LOCK TABLES `offices` WRITE;
/*!40000 ALTER TABLE `offices` DISABLE KEYS */;
INSERT INTO `offices` VALUES ('1','Makati','+63 2 8888 0001','Ayala Avenue',NULL,NULL,'Philippines','1226','Luzon'),('2','Quezon City','+63 2 8920 0002','Diliman',NULL,NULL,'Philippines','1101','Luzon'),('3','Cebu City','+63 32 231 0003','Cebu Business Park',NULL,NULL,'Philippines','6000','Visayas'),('4','Davao City','+63 82 221 0004','J.P. Laurel Avenue',NULL,NULL,'Philippines','8000','Mindanao'),('5','Pasig','+63 2 8631 0005','Ortigas Center',NULL,NULL,'Philippines','1605','Luzon'),('6','Taguig','+63 2 8555 0006','Bonifacio Global City',NULL,NULL,'Philippines','1634','Luzon'),('7','Baguio','+63 74 442 0007','Session Road',NULL,NULL,'Philippines','2600','Luzon');
/*!40000 ALTER TABLE `offices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderdetails`
--

DROP TABLE IF EXISTS `orderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderdetails` (
  `orderNumber` varchar(15) NOT NULL,
  `productCode` varchar(15) NOT NULL,
  `quantityOrdered` int unsigned NOT NULL,
  `priceEach` decimal(10,2) NOT NULL,
  `orderLineNumber` smallint NOT NULL,
  PRIMARY KEY (`orderNumber`,`productCode`),
  KEY `productCode` (`productCode`),
  CONSTRAINT `orderdetails_ibfk_1` FOREIGN KEY (`orderNumber`) REFERENCES `orders` (`orderNumber`),
  CONSTRAINT `orderdetails_ibfk_2` FOREIGN KEY (`productCode`) REFERENCES `products` (`productCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderdetails`
--

LOCK TABLES `orderdetails` WRITE;
/*!40000 ALTER TABLE `orderdetails` DISABLE KEYS */;
INSERT INTO `orderdetails` VALUES ('ORD001','HW001',5,129.00,1),('ORD001','MBX001',2,149.00,2),('ORD001','TMC001',1,329.00,3),('ORD002','HW002',3,299.00,1),('ORD002','MBX002',4,399.00,2),('ORD002','TMC002',2,449.00,3),('ORD003','HW003',1,599.00,1),('ORD003','MBX003',2,749.00,2),('ORD003','TMC003',5,699.00,3),('ORD004','HW001',5,129.00,2),('ORD004','MBX001',2,149.00,3),('ORD004','MJT001',10,179.00,1),('ORD005','HW002',2,299.00,2),('ORD005','MBX002',4,399.00,3),('ORD005','MJT002',3,249.00,1),('ORD006','HW003',1,599.00,2),('ORD006','MBX003',2,749.00,3),('ORD006','MJT003',1,799.00,1),('ORD007','HW001',3,129.00,3),('ORD007','MJT001',6,179.00,2),('ORD007','TMC001',4,329.00,1),('ORD008','HW002',5,299.00,3),('ORD008','MJT002',3,249.00,2),('ORD008','TMC002',2,449.00,1),('ORD009','HW003',2,599.00,3),('ORD009','MJT003',1,799.00,2),('ORD009','TMC003',1,699.00,1),('ORD010','MBX001',8,149.00,1),('ORD010','MJT001',4,179.00,3),('ORD010','TMC001',2,329.00,2),('ORD011','MBX002',5,399.00,1),('ORD011','MJT002',2,249.00,3),('ORD011','TMC002',1,449.00,2),('ORD012','MBX003',3,749.00,1),('ORD012','MJT003',1,799.00,3),('ORD012','TMC003',4,699.00,2),('ORD013','HW001',2,129.00,1),('ORD013','MBX002',3,399.00,2),('ORD013','TMC003',1,699.00,3),('ORD014','HW002',4,299.00,1),('ORD014','MBX003',1,749.00,2),('ORD014','MJT001',5,179.00,3),('ORD015','HW002',17,244.57,2),('ORD015','MJT001',2,180.86,3),('ORD015','TMC002',33,469.05,1),('ORD015','TMC003',1,742.44,4),('ORD016','MBX001',40,131.89,1),('ORD017','HW003',25,483.54,1),('ORD017','MBX003',47,808.39,2),('ORD017','MJT002',24,259.10,3),('ORD018','HW004',15,260.97,3),('ORD018','MJT001',28,146.09,1),('ORD018','TMC001',11,341.46,2),('ORD019','MJT001',8,185.03,1),('ORD020','MBX002',24,352.89,2),('ORD020','MJT003',37,642.20,1),('ORD021','HW002',19,288.31,3),('ORD021','HW004',29,283.38,2),('ORD021','TMC001',35,294.62,1),('ORD022','MBX001',7,120.52,3),('ORD022','MBX002',38,416.68,1),('ORD022','TMC002',15,466.60,2),('ORD023','HW004',25,266.08,1),('ORD024','HW001',39,131.47,1),('ORD024','HW004',5,258.21,2),('ORD025','HW001',37,116.77,1),('ORD025','HW003',50,633.89,5),('ORD025','MBX001',8,151.46,2),('ORD025','TMC001',35,346.16,4),('ORD025','TMC002',37,405.16,3),('ORD026','HW002',39,251.03,3),('ORD026','HW003',24,485.09,1),('ORD026','MBX003',36,599.59,2),('ORD027','HW001',31,120.17,2),('ORD027','MBX002',16,335.63,5),('ORD027','MBX003',17,663.02,4),('ORD027','MJT002',40,257.84,1),('ORD027','TMC002',14,366.78,3),('ORD028','HW001',38,118.15,1),('ORD028','MBX002',25,349.39,4),('ORD028','MJT002',6,260.47,3),('ORD028','TMC001',18,276.80,2),('ORD029','HW003',6,516.22,1),('ORD029','MBX001',14,135.13,2),('ORD030','HW001',3,139.87,1),('ORD030','MBX002',49,337.77,5),('ORD030','MJT003',14,727.54,2),('ORD030','TMC001',12,302.27,4),('ORD030','TMC003',1,738.26,3),('ORD031','HW004',35,308.67,2),('ORD031','MBX003',11,744.81,3),('ORD031','MJT002',13,261.02,1),('ORD031','TMC002',36,364.94,4),('ORD032','HW001',13,127.02,3),('ORD032','HW002',2,317.30,2),('ORD032','MBX002',50,347.88,1),('ORD033','MJT001',27,186.36,1),('ORD033','MJT003',14,668.76,4),('ORD033','TMC002',5,415.54,2),('ORD033','TMC003',13,662.28,3),('ORD034','HW002',10,269.46,4),('ORD034','HW004',11,251.34,3),('ORD034','MBX003',2,612.35,1),('ORD034','MJT001',11,155.70,2),('ORD035','HW001',5,105.15,3),('ORD035','HW002',49,270.87,4),('ORD035','HW003',42,658.71,5),('ORD035','HW004',47,298.58,1),('ORD035','MJT001',46,182.36,2),('ORD036','MBX001',23,122.99,1),('ORD036','MJT001',33,194.18,2),('ORD037','HW001',39,128.46,1),('ORD037','MJT001',26,155.30,2),('ORD038','HW004',20,243.42,3),('ORD038','MBX002',25,321.03,2),('ORD038','MJT001',48,153.94,4),('ORD038','TMC002',34,401.69,1),('ORD039','TMC003',13,610.36,1),('ORD040','HW003',40,614.75,3),('ORD040','MBX002',14,384.19,1),('ORD040','MJT001',28,146.06,2),('ORD040','MJT002',6,250.72,5),('ORD040','MJT003',48,826.41,4),('ORD041','HW002',10,305.81,2),('ORD041','MBX001',33,157.81,1),('ORD041','MBX002',42,378.91,3),('ORD041','MBX003',9,652.30,4),('ORD042','HW002',9,316.01,5),('ORD042','MJT001',17,194.63,4),('ORD042','MJT002',4,258.92,1),('ORD042','MJT003',13,818.39,3),('ORD042','TMC001',2,299.53,2),('ORD043','HW001',29,112.04,1),('ORD043','HW003',49,615.89,5),('ORD043','MBX001',48,149.53,4),('ORD043','MBX002',20,329.09,3),('ORD043','TMC002',37,469.19,2),('ORD044','MBX001',7,134.35,4),('ORD044','MJT002',26,224.03,3),('ORD044','TMC002',41,485.85,1),('ORD044','TMC003',18,602.39,2),('ORD045','MBX001',15,149.60,1),('ORD046','HW002',15,256.33,3),('ORD046','MBX001',42,150.73,5),('ORD046','MJT002',15,226.05,2),('ORD046','MJT003',40,693.14,1),('ORD046','TMC001',44,342.50,4),('ORD047','MBX001',32,124.87,2),('ORD047','TMC001',50,283.19,1),('ORD048','HW002',40,266.27,4),('ORD048','MBX002',20,345.20,3),('ORD048','MBX003',18,785.15,1),('ORD048','MJT003',19,858.15,2),('ORD049','TMC002',6,402.75,1),('ORD050','HW003',20,635.44,1),('ORD050','MBX002',24,352.31,3),('ORD050','TMC001',4,329.77,4),('ORD050','TMC003',50,618.42,2),('ORD051','TMC003',48,748.05,1),('ORD052','HW001',25,108.78,2),('ORD052','MBX001',46,131.52,3),('ORD052','MJT003',11,778.40,1),('ORD052','TMC003',27,606.46,4),('ORD053','HW003',35,510.39,1),('ORD053','HW004',23,296.16,2),('ORD054','TMC001',16,340.39,1);
/*!40000 ALTER TABLE `orderdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orderNumber` varchar(15) NOT NULL,
  `orderDate` date DEFAULT NULL,
  `requiredDate` date DEFAULT NULL,
  `shippedDate` date DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  `comments` text,
  `customerNumber` varchar(15) NOT NULL,
  `total_Price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`orderNumber`),
  KEY `customerNumber` (`customerNumber`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customerNumber`) REFERENCES `customers` (`customerNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('ORD001','2026-01-29','2026-02-07',NULL,'Cancelled',NULL,'CUST001',1272.00),('ORD002','2026-04-25','2026-05-08',NULL,'In Process',NULL,'CUST002',3391.00),('ORD003','2025-12-13','2025-12-26','2025-12-16','Resolved',NULL,'CUST003',5592.00),('ORD004','2026-02-09','2026-02-19','2026-02-15','Shipped','Particularly finally early same campaign course word better.','CUST004',2733.00),('ORD005','2025-06-12','2025-06-21',NULL,'Cancelled',NULL,'CUST001',2941.00),('ORD006','2025-05-05','2025-05-17','2025-05-11','Resolved',NULL,'CUST002',2896.00),('ORD007','2025-12-29','2026-01-08','2025-12-31','Shipped',NULL,'CUST003',2777.00),('ORD008','2026-02-18','2026-02-28',NULL,'On Hold',NULL,'CUST004',3140.00),('ORD009','2026-04-21','2026-04-30',NULL,'On Hold',NULL,'CUST001',2696.00),('ORD010','2025-05-29','2025-06-06','2025-06-04','Shipped',NULL,'CUST002',2566.00),('ORD011','2026-02-08','2026-02-21',NULL,'In Process',NULL,'CUST003',2942.00),('ORD012','2025-09-16','2025-09-28',NULL,'In Process',NULL,'CUST004',5842.00),('ORD013','2025-09-29','2025-10-11',NULL,'In Process','Look me but right win.','CUST001',2154.00),('ORD014','2026-02-22','2026-03-08','2026-02-23','Resolved',NULL,'CUST002',2840.00),('ORD015','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST013',20740.28),('ORD016','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST009',5275.62),('ORD017','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST008',56301.26),('ORD018','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST002',11761.29),('ORD019','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST007',1480.25),('ORD020','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST006',32230.68),('ORD021','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST003',24007.55),('ORD022','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST009',23676.63),('ORD023','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST007',6652.11),('ORD024','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST008',6418.58),('ORD025','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST003',64333.36),('ORD026','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST002',43017.15),('ORD027','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST002',35815.52),('ORD028','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST022',19769.58),('ORD029','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST006',4989.13),('ORD030','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST024',31521.58),('ORD031','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST021',35527.72),('ORD032','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST024',19680.00),('ORD033','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST001',25081.68),('ORD034','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST002',8396.72),('ORD035','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST006',63886.18),('ORD036','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST016',9236.79),('ORD037','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST010',9047.83),('ORD038','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST005',33940.57),('ORD039','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST015',7934.63),('ORD040','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST015',75229.99),('ORD041','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST021',30050.60),('ORD042','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST016',18426.56),('ORD043','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST005',64547.34),('ORD044','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST017',37528.13),('ORD045','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST002',2244.07),('ORD046','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST011',56361.81),('ORD047','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST013',18155.24),('ORD048','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST016',47992.53),('ORD049','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST015',2416.51),('ORD050','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST004',53404.14),('ORD051','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST005',35906.40),('ORD052','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST013',33706.14),('ORD053','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST023',24675.38),('ORD054','2026-05-22','2026-05-29',NULL,'Shipped',NULL,'CUST020',5446.20);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `customerNumber` varchar(15) NOT NULL,
  `checkNumber` varchar(50) NOT NULL,
  `paymentDate` date NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`customerNumber`,`checkNumber`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`customerNumber`) REFERENCES `customers` (`customerNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES ('CUST001','HQ336336','2024-10-19',6066.00),('CUST001','JM292331','2024-11-05',2572.00),('CUST002','HQ55022','2025-01-30',2160.00),('CUST002','OM314933','2024-12-18',1627.00),('CUST003','GG314553','2025-02-15',3500.00),('CUST004','MA765512','2025-03-10',1200.00);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productlines`
--

DROP TABLE IF EXISTS `productlines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productlines` (
  `productLine` varchar(50) NOT NULL,
  `textDescription` varchar(4000) DEFAULT NULL,
  `htmlDescription` mediumtext,
  `image` mediumblob,
  PRIMARY KEY (`productLine`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productlines`
--

LOCK TABLES `productlines` WRITE;
/*!40000 ALTER TABLE `productlines` DISABLE KEYS */;
INSERT INTO `productlines` VALUES ('Hot Wheels','A product line of die-cast toy cars, known for their speed and collectible nature',NULL,NULL),('Majorette','A product line of die-cast toy cars, known for their vibrant colors and wide range of models',NULL,NULL),('Matchbox','A product line of die-cast toy cars, known for their detailed designs and variety of models',NULL,NULL),('Tomica','A product line of die-cast toy cars, known for their high-quality craftsmanship and realistic designs',NULL,NULL);
/*!40000 ALTER TABLE `productlines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `productCode` varchar(15) NOT NULL,
  `productName` varchar(70) NOT NULL,
  `productLine` varchar(50) NOT NULL,
  `productScale` varchar(10) DEFAULT NULL,
  `productVendor` varchar(50) DEFAULT NULL,
  `productDescription` text,
  `quantityInStock` int unsigned DEFAULT NULL,
  `buyPrice` decimal(10,2) DEFAULT NULL,
  `MSRP` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`productCode`),
  KEY `productLine` (`productLine`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`productLine`) REFERENCES `productlines` (`productLine`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('HW001','Hot Wheels Basic Cars','Hot Wheels','~1:64','Mattel','An affordable diecast meant to ride the orange track!',234,90.48,129.00),('HW002','Hot Wheels Silver Series','Hot Wheels','~1:64','Mattel','For collectors who are getting more serious with a metal base and full details',462,214.49,299.00),('HW003','Hot Wheels Gold Series','Hot Wheels','~1:64','Mattel','A premium collectible series, metal base, rubber tires and full details!',120,474.47,599.00),('HW004','Hot Wheels Neon Speeders','Hot Wheels','~1:64','Mattel','Light them under a bluelight and watch them glow!',248,213.41,299.00),('MBX001','Matchbox Basic Cars','Matchbox','~1:64','Mattel','An affordable diecast bringing your favorite traffic to your room!',104,114.83,149.00),('MBX002','Matchbox Moving Parts','Matchbox','~1:64','Mattel','A series with moving parts such as opening hoods, doors, trunks!',151,275.20,399.00),('MBX003','Matchbox Collectors','Matchbox','~1:64','Mattel','For collectors who prefer premium details',256,598.76,749.00),('MJT001','Majorette Basic Cars','Majorette','~1:64','Majorette','Basic Majorette car model',352,142.75,179.00),('MJT002','Majorette Premium Cars','Majorette','~1:64','Majorette','Detailed cars with themed series',158,151.48,249.00),('MJT003','Majorette Collection Series','Majorette','~1:64','Majorette','Collector\'s items that are true-to-scale',456,509.21,799.00),('TMC001','Tomica Basic Cars','Tomica','~1:64','Tomy Company','Basic diecast model with suspension',267,243.99,329.00),('TMC002','Tomica Premium','Tomica','~1:64','Tomy Company','Premium Tomica car with premium details',448,341.68,449.00),('TMC003','Tomica Premium Unlimited','Tomica','~1:64','Tomy Company','Premium Tomica car models from various licensed cars',396,426.34,699.00);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `orderstatistics`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `orderstatistics` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `orderstatistics`;

--
-- Table structure for table `dim_employee_revenue`
--

DROP TABLE IF EXISTS `dim_employee_revenue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_employee_revenue` (
  `employee_number` int unsigned NOT NULL,
  `employee_name` varchar(100) NOT NULL,
  `office_city` varchar(50) NOT NULL,
  PRIMARY KEY (`employee_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_employee_revenue`
--

LOCK TABLES `dim_employee_revenue` WRITE;
/*!40000 ALTER TABLE `dim_employee_revenue` DISABLE KEYS */;
INSERT INTO `dim_employee_revenue` VALUES (1002,'Diane Murphy','Makati'),(1056,'Mary Patterson','Makati'),(1076,'Jeff Firrelli','Makati'),(1088,'William Patterson','Taguig'),(1102,'Gerard Bondur','Davao City'),(1286,'Foon Yue Tseng','Cebu City'),(1323,'George Vanauf','Cebu City'),(1337,'Loui Bondur','Davao City'),(1401,'Pamela Castillo','Davao City'),(1501,'Larry Bott','Baguio'),(1504,'Barry Jones','Baguio'),(1612,'Peter Marsh','Taguig'),(1621,'Mami Nishi','Pasig'),(1625,'Yoshimi Kato','Pasig');
/*!40000 ALTER TABLE `dim_employee_revenue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_office_sales`
--

DROP TABLE IF EXISTS `dim_office_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_office_sales` (
  `office_code` varchar(10) NOT NULL,
  `office_city` varchar(50) NOT NULL,
  PRIMARY KEY (`office_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_office_sales`
--

LOCK TABLES `dim_office_sales` WRITE;
/*!40000 ALTER TABLE `dim_office_sales` DISABLE KEYS */;
INSERT INTO `dim_office_sales` VALUES ('1','Makati'),('3','Cebu City'),('4','Davao City'),('5','Pasig'),('6','Taguig'),('7','Baguio');
/*!40000 ALTER TABLE `dim_office_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_product_line_revenue`
--

DROP TABLE IF EXISTS `dim_product_line_revenue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_product_line_revenue` (
  `product_line` varchar(50) NOT NULL,
  `product_line_description` varchar(4000) NOT NULL,
  PRIMARY KEY (`product_line`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_product_line_revenue`
--

LOCK TABLES `dim_product_line_revenue` WRITE;
/*!40000 ALTER TABLE `dim_product_line_revenue` DISABLE KEYS */;
INSERT INTO `dim_product_line_revenue` VALUES ('Hot Wheels','A product line of die-cast toy cars, known for their speed and collectible nature'),('Majorette','A product line of die-cast toy cars, known for their vibrant colors and wide range of models'),('Matchbox','A product line of die-cast toy cars, known for their detailed designs and variety of models'),('Tomica','A product line of die-cast toy cars, known for their high-quality craftsmanship and realistic designs');
/*!40000 ALTER TABLE `dim_product_line_revenue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_product_sales`
--

DROP TABLE IF EXISTS `dim_product_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_product_sales` (
  `product_code` varchar(15) NOT NULL,
  `product_name` varchar(70) NOT NULL,
  PRIMARY KEY (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_product_sales`
--

LOCK TABLES `dim_product_sales` WRITE;
/*!40000 ALTER TABLE `dim_product_sales` DISABLE KEYS */;
INSERT INTO `dim_product_sales` VALUES ('HW001','Hot Wheels Basic Cars'),('HW002','Hot Wheels Silver Series'),('HW003','Hot Wheels Gold Series'),('HW004','Hot Wheels Neon Speeders'),('MBX001','Matchbox Basic Cars'),('MBX002','Matchbox Moving Parts'),('MBX003','Matchbox Collectors'),('MJT001','Majorette Basic Cars'),('MJT002','Majorette Premium Cars'),('MJT003','Majorette Collection Series'),('TMC001','Tomica Basic Cars'),('TMC002','Tomica Premium'),('TMC003','Tomica Premium Unlimited');
/*!40000 ALTER TABLE `dim_product_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dim_sales`
--

DROP TABLE IF EXISTS `dim_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_sales` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `customer_city` varchar(50) NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_sales`
--

LOCK TABLES `dim_sales` WRITE;
/*!40000 ALTER TABLE `dim_sales` DISABLE KEYS */;
INSERT INTO `dim_sales` VALUES (1,'Davao City'),(2,'Manila'),(3,'Iloilo City'),(4,'Paranaque'),(5,'Pasig'),(6,'Makati'),(7,'Taguig'),(8,'Baguio'),(9,'Cebu City'),(10,'Cagayan de Oro');
/*!40000 ALTER TABLE `dim_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fact_employee_revenue`
--

DROP TABLE IF EXISTS `fact_employee_revenue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fact_employee_revenue` (
  `employee_revenue_id` int NOT NULL AUTO_INCREMENT,
  `employee_number` int unsigned NOT NULL,
  `office_code` varchar(10) NOT NULL,
  `total_revenue` decimal(10,2) NOT NULL,
  `total_orders` int NOT NULL,
  PRIMARY KEY (`employee_revenue_id`),
  KEY `fk_fact_employee_number` (`employee_number`),
  CONSTRAINT `fk_fact_employee_number` FOREIGN KEY (`employee_number`) REFERENCES `dim_employee_revenue` (`employee_number`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fact_employee_revenue`
--

LOCK TABLES `fact_employee_revenue` WRITE;
/*!40000 ALTER TABLE `fact_employee_revenue` DISABLE KEYS */;
INSERT INTO `fact_employee_revenue` VALUES (1,1076,'1',34144.68,5),(2,1056,'1',19769.58,1),(3,1002,'1',324561.14,13),(4,1323,'3',24675.38,1),(5,1286,'3',8132.36,2),(6,1401,'4',5446.20,1),(7,1337,'4',65578.32,2),(8,1102,'4',75655.88,3),(9,1625,'5',114533.38,5),(10,1621,'5',71767.67,3),(11,1612,'6',65119.14,4),(12,1088,'6',247322.06,12),(13,1504,'7',56361.81,1),(14,1501,'7',37528.13,1);
/*!40000 ALTER TABLE `fact_employee_revenue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fact_office_sales`
--

DROP TABLE IF EXISTS `fact_office_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fact_office_sales` (
  `office_sales_id` int NOT NULL AUTO_INCREMENT,
  `office_code` varchar(10) NOT NULL,
  `total_revenue` decimal(10,2) NOT NULL,
  `total_orders` int NOT NULL,
  PRIMARY KEY (`office_sales_id`),
  KEY `fk_fact_office_code` (`office_code`),
  CONSTRAINT `fk_fact_office_code` FOREIGN KEY (`office_code`) REFERENCES `dim_office_sales` (`office_code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fact_office_sales`
--

LOCK TABLES `fact_office_sales` WRITE;
/*!40000 ALTER TABLE `fact_office_sales` DISABLE KEYS */;
INSERT INTO `fact_office_sales` VALUES (1,'1',378475.40,19),(2,'6',312441.20,16),(3,'5',186301.05,8),(4,'4',146680.40,6),(5,'7',93889.94,2),(6,'3',32807.74,3);
/*!40000 ALTER TABLE `fact_office_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fact_product_line_revenue`
--

DROP TABLE IF EXISTS `fact_product_line_revenue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fact_product_line_revenue` (
  `product_line_revenue_id` int NOT NULL AUTO_INCREMENT,
  `product_line` varchar(50) NOT NULL,
  `total_revenue` decimal(10,2) NOT NULL,
  `total_orders` int NOT NULL,
  PRIMARY KEY (`product_line_revenue_id`),
  KEY `fk_fact_product_line` (`product_line`),
  CONSTRAINT `fk_fact_product_line` FOREIGN KEY (`product_line`) REFERENCES `dim_product_line_revenue` (`product_line`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fact_product_line_revenue`
--

LOCK TABLES `fact_product_line_revenue` WRITE;
/*!40000 ALTER TABLE `fact_product_line_revenue` DISABLE KEYS */;
INSERT INTO `fact_product_line_revenue` VALUES (1,'Hot Wheels',327067.04,1003),(2,'Tomica',306866.61,679),(3,'Matchbox',282046.10,838),(4,'Majorette',234615.52,640);
/*!40000 ALTER TABLE `fact_product_line_revenue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fact_product_sales`
--

DROP TABLE IF EXISTS `fact_product_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fact_product_sales` (
  `product_sales_id` int NOT NULL AUTO_INCREMENT,
  `product_code` varchar(15) NOT NULL,
  `total_revenue` decimal(10,2) NOT NULL,
  `total_orders` int NOT NULL,
  PRIMARY KEY (`product_sales_id`),
  KEY `fk_fact_product_code` (`product_code`),
  CONSTRAINT `fk_fact_product_code` FOREIGN KEY (`product_code`) REFERENCES `dim_product_sales` (`product_code`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fact_product_sales`
--

LOCK TABLES `fact_product_sales` WRITE;
/*!40000 ALTER TABLE `fact_product_sales` DISABLE KEYS */;
INSERT INTO `fact_product_sales` VALUES (1,'HW003',176705.00,295),(2,'MJT003',159001.00,199),(3,'MBX002',144837.00,363),(4,'TMC003',127218.00,182),(5,'TMC002',118087.00,263),(6,'MBX003',110852.00,148),(7,'TMC001',76986.00,234),(8,'HW002',66976.00,224),(9,'HW004',62790.00,210),(10,'MJT001',53521.00,299),(11,'MBX001',48723.00,327),(12,'MJT002',35358.00,142),(13,'HW001',35346.00,274);
/*!40000 ALTER TABLE `fact_product_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fact_sales`
--

DROP TABLE IF EXISTS `fact_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fact_sales` (
  `sales_id` int NOT NULL AUTO_INCREMENT,
  `location_id` int NOT NULL,
  `total_revenue` decimal(10,2) NOT NULL,
  `total_orders` int NOT NULL,
  PRIMARY KEY (`sales_id`),
  KEY `fk_fact_sales_location` (`location_id`),
  CONSTRAINT `fk_fact_sales_location` FOREIGN KEY (`location_id`) REFERENCES `dim_sales` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fact_sales`
--

LOCK TABLES `fact_sales` WRITE;
/*!40000 ALTER TABLE `fact_sales` DISABLE KEYS */;
INSERT INTO `fact_sales` VALUES (1,1,262108.13,13),(2,2,234046.22,8),(3,3,175248.93,8),(4,4,112927.75,9),(5,5,94628.96,4),(6,6,68166.04,3),(7,7,65578.32,2),(8,8,56361.81,1),(9,9,53627.63,3),(10,10,27901.94,3);
/*!40000 ALTER TABLE `fact_sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-26  2:14:23
