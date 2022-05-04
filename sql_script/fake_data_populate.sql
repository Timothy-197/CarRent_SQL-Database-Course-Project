SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

USE `CarRental`;

-- --------------------------------------------------------

insert into `customer` (`name`, `gender`, `age`, `address`, `contact`, `balance`, `password`) values
('Gary CHEN', 'male', '21', 'LGU Shaw', 'lgu@cuhk.edu.cn', '1000', 'abc123'),
('Yiyan HU', 'male', '20', 'LGU Shaw Building C', 'lgu@gmail.com', '2000', 'abcd1234'),
('Hao ZHU', 'male', '22', 'CUHK(SZ), Shenzhen, Guangdong Province', 'lgu@outlook.com', '1500', 'abcdefg');

-- --------------------------------------------------------

insert into `owner` (`name`, `address`, `contact`, `password`) values
('Qiaohui LIANG', 'CUHK(SZ), Longxiangdadao', 'lgu@hotmail.com', '12345678'),
('Hongmeng YANG', 'LGU at Guangdong Shenzhen', 'lgu@163.com', 'abcd9876');

-- --------------------------------------------------------

insert into `car` (`description`, `category`, `brand`, `color`, `capacity`, `fuel_type`, `image`, `rate`, `rent_price`, `owner_id`) values
('This is a very nice car!', 'suv', 'Tesla', 'blue', '4', 'ELECTRIC', NULL, '4.5', '90', '1'),
('A very pretty car!', 'truck', 'Ford', 'red', '2', 'GASOLINE', NULL, '4.8', '120', '2');

-- --------------------------------------------------------

insert into `review` (`review`, `rate`, `date`, `renter_trips_taken`, `customer_id`, `car_id`) values
('This car helps me a lot. Nice~', '4', '2022-05-01', '23', '1', '2'),
('Great experience, bro!', '5', '2022-05-03', '11', '3', '2');

-- --------------------------------------------------------

insert into `order` (`cost`, `order_date`, `begin_date`, `return_date`, `car_id`, `customer_id`) values
('200', '2022-04-12', '2022-04-13', '2022-04-16', '2', '1'),
('150', '2022-04-20', '2022-04-21', '2022-04-23', '2', '3');

-- --------------------------------------------------------

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
