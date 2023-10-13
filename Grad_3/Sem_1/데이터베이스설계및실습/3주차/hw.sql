SELECT `customerNumber`, `contactLastName` FROM `customers` UNION SELECT `employeeNumber`, `lastName` FROM `employees`; # 1

SELECT `status`, count(`status`) AS count FROM `orders` GROUP BY `orders`.`status` ORDER BY count DESC; # 2

SELECT `orderNumber`, sum(`quantityOrdered`) AS quantityOrdered, sum(`priceEach`) AS priceEach FROM `orderdetails` GROUP BY `orderNumber` HAVING quantityOrdered >= 1000 AND priceEach >= 600 ORDER BY quantityOrdered DESC; #3

SELECT DISTINCT `products`.`productName`, `priceEach` FROM `orderdetails` INNER JOIN `products` ON `products`.`productCode` = `orderdetails`.`productCode` WHERE `orderdetails`.`priceEach` IN (SELECT min(`orderdetails`.`priceEach`) FROM `orderdetails`); # 4

SELECT `orderdetails`.`orderNumber`, `orders`.`status`, sum(`orderdetails`.`quantityOrdered` * `orderdetails`.`priceEach`) AS `total price` FROM `orderdetails`, `orders`GROUP BY `orderdetails`.`orderNumber`; # 5

SELECT `customers`.`customerNumber`, `customers`.`customerName`, `orderNumber`, `orders`.`status` FROM `customers` LEFT JOIN `orders` ON `customers`.`customerNumber` = `orders`.`customerNumber`; # 6
# null값이 나온 이유? 해당 customer의 주문 정보가 없기 때문 = 해당 customer가 물건 주문을 하지 않았기 때문에 null값으로 나온다.

SELECT `customers`.`customerNumber`, `customers`.`customerName` FROM `customers` LEFT OUTER JOIN `orders` ON `customers`.`customerNumber` = `orders`.`customerNumber` WHERE `orders`.`customerNumber` IS NULL; # 7