## 과제 1
#### 1. employees의 lastname, firstname, jobtitle의 정보를 검색
```mysql
SELECT `lastname`, `firstname`, `jobtitle` FROM `employees` LIMIT 10;
```
#### 2. customers중 country가 USA이면서 NYC라는 city에 살고 있으며 creditlimit이 200미만인 사람의 이름(customername)을 검색
```mysql
SELECT `customername` FROM `customers` WHERE `country` = "USA" and `city` = "NYC" and `creditlimit` < 200 LIMIT 10;
```
#### 3. buyprice가 50이하이거나 100이상인 products의 productcode, productname, buyprice를 검색
```mysql
SELECT `productcode`, `productname`, `buyprice` FROM `products` WHERE `buyprice` <= 50 or `buyprice` >= 100 LIMIT 10;
```
#### 4. lastname에 am이 들어가고 firstname이 er로 끝나느 employees의 employeenumber와 lastname, firstname을 검색
```mysql
SELECT `employeenumber`, `lastname`, `firstname` FROM `employees` WHERE `lastname` LIKE '%am%' and `firstname` LIKE '%er' LIMIT 10;
```
#### 5. customers의 lastname은 사전의 역순으로, 고객의 firstname은 사전순으로 정렬될 수 있도록 검색
```mysql
SELECT `contactlastname`, `contactfirstname` FROM `customers` ORDER BY `contactlastname` ASC, `contactfirstname` DESC LIMIT 10;
```
#### 6. buyprice가 가장 높은 products의 productname과 buyprice를 10위까지 추출
```mysql
SELECT `productname`, `buyprice` FROM `products` ORDER BY `buyprice` DESC LIMIT 10;
```
#### 7. priceeach가 가장 작은 products의 productname과 priceeach를 검색
```mysql
SELECT DISTINCT `products`.`productname`, `orderdetails`.`priceeach` FROM `products`, `orderdetails` WHERE `products`.`productcode` IN (SELECT `orderdetails`.`productcode` FROM `orderdetails` WHERE `priceeach` IN (SELECT MIN(`priceeach`) FROM `orderdetails`)) ORDER BY `priceeach` ASC LIMIT `;
```
#### 8. amount가 40000이상인 customers가 사는 city를 모두 나열
```mysql
SELECT DISTINCT `city` FROM `customers` WHERE `customernumber` IN (SELECT `customernumber` FROM `payments` WHERE `amount` >= 40000) LIMIT 10;
```
## 과제 2
#### 1. 고객테이블에서 고객번호, 고객 lastnmae정보를 얻은 결과와 직원 테이블에서 직원번호, 직원 lastname정보를 합치고 번호에 대하여 오름차순으로 정렬한 결과를 보이시오.
```mysql
SELECT `customerNumber`, `contactLastName` FROM `customers` UNION SELECT `employeeNumber`, `lastName` FROM `employees`;
```
#### 2. 주문의 상태와 그 상태를 갖는 주문의 수를 출력하여라 (상태를 갖는 주문의 수가 많은 순으로 출력)
```mysql
SELECT `status`, count(`status`) AS count FROM `orders` GROUP BY `orders`.`status` ORDER BY count DESC;
```
#### 3. 상세주문 테이블에서 주문번호별 총 주문수, 총 개당 가격을 추출하시오. (총 주문수는 1000건 이상이고, 총 개당 가격은 600이상인 ROW만 추출)
```mysql
SELECT `orderNumber`, sum(`quantityOrdered`) AS quantityOrdered, sum(`priceEach`) AS priceEach FROM `orderdetails` GROUP BY `orderNumber` HAVING quantityOrdered >= 1000 AND priceEach >= 600 ORDER BY quantityOrdered DESC; 
```
#### 4. INNER JOIN을 활용하여 priceEach가 가장 작은 물품의 이름과 priceEach를 검색하시오.
```mysql
SELECT DISTINCT `products`.`productName`, `priceEach` FROM `orderdetails` INNER JOIN `products` ON `products`.`productCode` = `orderdetails`.`productCode` WHERE `orderdetails`.`priceEach` IN (SELECT min(`orderdetails`.`priceEach`) FROM `orderdetails`); 
```
#### 5. 주문 테이블과 상세 주문 테이블로부터 주문번호 별로 주문번호, 상태, 총 주문금액을 검색하시오. (하나의 주문번호에는 여러 개의 상품 주문이 있기 때문에 총 주문금액은 quantityOrderd * priceEach들의 sum이 되어야함.)
```myslq
SELECT `orderdetails`.`orderNumber`, `orders`.`status`, sum(`orderdetails`.`quantityOrdered` * `orderdetails`.`priceEach`) AS `total price` FROM `orderdetails`, `orders`GROUP BY `orderdetails`.`orderNumber`; 
```
#### 6. 모든 고객의 주문 정보를 검색하시오.(추출해야할 정보는 고객번호, 고객이름, 주문번호, 상품 상태)
#### Q. SELECT c.customerNumber, c.customerName, orderNumber, o.status FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber;
#### Q의 결과에서 NULL값이 포함되었다면, 그 이유를 설명하시오.
#### null값이 나온 이유? 해당 customer의 주문 정보가 없기 때문이다.
```mysql
SELECT `customers`.`customerNumber`, `customers`.`customerName`, `orderNumber`, `orders`.`status` FROM `customers` LEFT JOIN `orders` ON `customers`.`customerNumber` = `orders`.`customerNumber`;
# null값이 나온 이유? 해당 customer의 주문 정보가 없기 때문 = 해당 customer가 물건 주문을 하지 않았기 때문에 null값으로 나온다.

```
#### 7. 고객 중 주문을 하지 않은 고객의 고객번호와 고객이름을 추출하시오.
```mysql
SELECT `customers`.`customerNumber`, `customers`.`customerName` FROM `customers` LEFT OUTER JOIN `orders` ON `customers`.`customerNumber` = `orders`.`customerNumber` WHERE `orders`.`customerNumber` IS NULL; 
```
## 과제 3
#### 1. Employee Table에 employeeNumber는 1901번, lastName은 hong, firstName은 jin, extension은 x5000, email은 nike@google.com, officeCode는 10, reportsTo는 null, jobTitle은 Research인 사원의 정보를 입력하시오
```mysql
SET foreign_key_checks = 0;
INSERT INTO employees(employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES(1901, "hong", "jin", "x5000", "nike@google.com", 10, null, "Research"); #1
SET foreign_key_checks = 1;
SELECT * from `employees` where officeCode = 10;
```
#### 2. Jobtitle이 research인 직원이 속한 office의 city를 Cheonan-si으로 변경하시오
```mysql
INSERT INTO `offices` VALUES(10, "NYC", "", "", "", "", "", "", "");
UPDATE `offices` SET `city` = "Cheonan-si" where `officeCode` in (SELECT `officeCode` FROM `employees` where `jobTitle` = "Research");
SELECT * FROM `offices` where `officeCode` in (SELECT `officeCode` FROM `employees` WHERE `jobTitle` = "Research");
```
#### 3. 아래 데이터베이스 및 테이블을 구축하시오
###### ❑ empdb라는 이름의 database를 만드시오
###### ❑ Database 안에 merit이라는 테이블을 생성하시오(아래는 테이블 정보)
###### ◼ performance INT(11) NOT NULL
###### ◼ percentage FLOAT NOT NULL
###### ◼ PRIMARY KEY(performance)
###### ❑ Database 안에 employees라는 테이블을 만드시오
###### ◼ emp_id INT(11) NOT NULL AUTO_INCREMENT,
###### ◼ emp_name VARCHAR(255) NOT NULL,
###### ◼ performance INT(11) DEFAULT NULL,
###### ◼ salary FLOAT DEFAULT NULL,
###### ◼ PRIMARY KEY (emp_id) CONSTRAINT fk_performance FOREIGN KEY ###### (performance) REFERENCES 
###### merits(performance)
###### ❑ merit 테이블에 실적(performance)별 보너스 percentage를 입력하시오
###### ◼ 1 → 0, 2 → 0.01, 3 → 0.03, 4 → 0.05, 5 → 0.08
###### ❑ employees 테이블에 직원 데이터를 입력하시오
###### ◼ ('Mary Doe', 1, 50000),
###### ◼ ('Cindy Smith', 3, 65000),
###### ◼ ('Sue Greenspan', 4, 75000),
###### ◼ ('Grace Dell', 5, 125000),
###### ◼ ('Nancy Johnson', 3, 85000),
###### ◼ ('John Doe', 2, 45000),
###### ◼ ('Lily Bush', 3, 55000);
```mysql
DROP DATABASE `empdb`;
CREATE DATABASE IF NOT EXISTS `empdb`;
USE `empdb`;

CREATE TABLE IF NOT EXISTS `merit` (
  `performance` INT(11) NOT NULL,
  `percentage` FLOAT NOT NULL,
  PRIMARY KEY(`performance`)
);

CREATE TABLE IF NOT EXISTS `employees`(
  `emp_id` INT(11) NOT NULL AUTO_INCREMENT,
  `emp_name` VARCHAR(255) NOT NULL,
  `performance` INT(11) DEFAULT NULL,
  `salary` FLOAT DEFAULT NULL,
  PRIMARY KEY(`emp_id`),
  CONSTRAINT `fk_performance` FOREIGN KEY (`performance`) REFERENCES `merit`(`performance`)
);

INSERT INTO `merit` VALUES(1, 0);
INSERT INTO `merit` VALUES(2, 0.01);
INSERT INTO `merit` VALUES(3, 0.03);
INSERT INTO `merit` VALUES(4, 0.05);
INSERT INTO `merit` VALUES(5, 0.08);
SELECT * FROM `merit`;

INSERT INTO `employees` VALUES(1, "Mary Doe", 1, 50000);
INSERT INTO `employees` VALUES(2, "Cindy Smith", 3, 65000);
INSERT INTO `employees` VALUES(3, "Sue Greenspan", 4, 75000);
INSERT INTO `employees` VALUES(4, "Grace Dell", 5, 125000);
INSERT INTO `employees` VALUES(5, "Nancy Johnson", 3, 85000);
INSERT INTO `employees` VALUES(6, "John Doe", 2, 45000);
INSERT INTO `employees` VALUES(7, "Lily Busy", 3, 55000);
SELECT * FROM `employees`;
```
#### 4. 실적 별 월급은 실적이 올라갈 때 마다 월급=월급+월급*percentage로 오른다고 가정하고, 현재 employees 테이블에 들어가 있는 월급 데이터는 실적정보가 반영되어 있지 않다고 할 때 실적을 반영한 월급으로 갱신 시키시오
```mysql
UPDATE `employees` JOIN `merit` SET `employees`.`salary` = `employees`.`salary` + `employees`.`salary` * `merit`.`percentage` WHERE `merit`.`performance` = `employees`.`performance`;
SELECT * FROM `employees`;
```
#### 5. Employees와 offices Table에서 officeCode가 1인 Row들을 삭제하시오 (삭제 후 결과 화면 스크린 샷)
```mysql
USE `classicmodels`;
SET foreign_key_checks = 0;
DELETE FROM `employees` WHERE `officeCode` = 1;
DELETE FROM `offices` WHERE `officeCode` = 1;
SET foreign_key_checks = 1;
SELECT * FROM `employees`;
SELECT * FROM `offices`;
```
#### 6. 3번에서 입력시킨 사원을 삭제하시오.
```mysql
USE `empdb`;
DELETE FROM `employees`;
SELECT * FROM `employees`;
```
#### 7. room 테이블을 캡처하고, 2번 building을 삭제 한 후에 room 테이블을 캡처하시오
```mysql
CREATE TABLE buildings(
  `building_no` INT(11) NOT NULL AUTO_INCREMENT,
  `building_name` VARCHAR(255) NOT NULL,
  `address` VARCHAR(355) NOT NULL,
  PRIMARY KEY(`building_no`)
);

INSERT INTO buildings(building_name, address) VALUES("ACME Headquaters", "3950 North 1st Street CA 95134"), ("ACME Sales", "5000 North 1st Street CA 95134");

CREATE TABLE rooms(
  room_no INT(11) NOT NULL AUTO_INCREMENT,
  room_name VARCHAR(255) NOT NULL,
  building_no INT(11) NOT NULL,
  PRIMARY KEY (room_no),
  KEY building_no(building_no),
  CONSTRAINT rooms_ibfk_1 FOREIGN KEY(building_no) REFERENCES buildings (building_no) ON DELETE CASCADE
);

INSERT INTO rooms(room_name,building_no) VALUES("Amazon",1), ("War Room",1), ("Office of CEO",1), ("Marketing", 2), ("Showroom",2);

SELECT * FROM `rooms`;
DELETE FROM `buildings` WHERE `building_no` = 2;
SELECT * FROM `rooms`;
```
## 과제 4
#### 1. 가격이 3이상인 술을 파는 바의 이름을 검색하시오.
```radb
\project_{bar}(\select_{price >= 3} Serves);
```
```mysql
SELECT DISTINCT bar FROM Serves WHERE price >= 3;
```
#### 2. 'Dixie'를 판매하는 바의 이름과 가격을 검색하시오.
```radb
\project_{bar, price}(\select_{beer = 'Dixie'} Serves);
```
```mysql
SELECT bar, price FROM Serves WHERE beer = 'Dixie';
```
#### 3. 일주일에 2번 바를 이용하는 음주가 이름, 주소, 바 이름을 검색하시오.
```radb
\proejct_{drinker, address, bar}(\select_{times_a_week = 2} Frequents \join_{name = drinker} Drinker);
```
```mysql
SELECT drinker, address, bar FROM Frequants JOIN Dinker ON name = drinker AND times_a_week = 2;
```
#### 4. 'Budweiser'와 'Corona'를 좋아하는 음주가의 이름과 주소를 검색하시오.
###### or
```radb
\project_{name, address}(\select_{beer = 'Budweiser' or beer = 'Corona'} Likes \join_{drinker = name} Drinker);
```
```mysql
SELECT DISTINCT name, address FROM Likes JOIN Drinker ON drinker = name WHERE beer = 'Budweiser' or beer = 'Corona';
```
###### and
```radb
\project_{Likes.drinker, Drinker.address}((\project_{Likes.drinker, Drinker.address}(\select_{beer = 'Budweiser'} Likes \join_{Likes.drinker = Drinker.name} Dinker)) \intersect (\project_{Likes.drinker, Dinker.address}(\select_{beer = 'Corona'} Likes \join_{Likes.drinker = Drinker.name} Drinker)));
```
```mysql
SELECT Likes.drinker, Drinker.address FROM Likes JOIN Drinker ON Likes.drinker = Drinker.name WHERE beer = 'Budweiser' INTERSECT SELECT Likes.drinkser, Drinker.address FROM Likes JOIN Drinker ON Likes.drinker = Drinker.name WHERE beer = 'Corona';
```
#### 5. 'Ben'이 자주 가는 술집에서 'Ben'이 좋아하는 술을 얼마에 파는지 바의 이름, 술 이름, 가격을 검색하시오.
```radb
\project_{Frequents.bar, Likes.beer, Serves.price}((((\select_{drinker = 'Ben'} Frequents) \join_{Frequents.bar = Bar.name} Bar) \join_{Frequents.drinker = Likes.drinker} Likes) \join_{Frequents.bar = Serves.bar and Likes.beer = Serves.beer} Serves);
```
```mysql
SELECT Frequents.bar, Likes.beer, Serves.price FROM Frequents JOIN Bar ON Frequents.bar = Bar.name JOIN Likes ON Frequents.drinker = Likes.drinker JOIN Serves ON Frequents.bar = Serves.bar and Likes.beer = Serves.beer WHERE Frequents.drinker = 'Ben';
```