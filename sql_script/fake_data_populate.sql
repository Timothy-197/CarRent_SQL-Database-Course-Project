SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

USE `CarRental3`;

-- -------------------------------------------------------- You should register a customer account to login

-- insert into `customer` (`name`, `gender`, `address`, `email`, `balance`, `password`) values
-- ('Gary CHEN', 'male', 'LGU Shaw', 'lgu@cuhk.edu.cn', '1000', 'abc123'),
-- ('Yiyan HU', 'male', 'LGU Shaw Building C', 'lgu@gmail.com', '2000', 'abcd1234'),
-- ('Hao ZHU', 'male', 'CUHK(SZ), Shenzhen, Guangdong Province', 'lgu@outlook.com', '1500', 'abcdefg');
-- 
-- -- --------------------------------------------------------

insert into `owner` (`name`,`user_id`, `gender`, `address`, `email`, `password`) values
('Qiaohui LIANG', 100,'female', 'CUHK(SZ), Longxiangdadao', 'lgu@hotmail.com', '12345678'),
('Hongmeng YANG',101, 'male', 'LGU at Guangdong Shenzhen', 'lgu@163.com', 'abcd9876');

-- --------------------------------------------------------

insert into `car` (`description`,`category`, `brand`, `color`, `capacity`, `fuel_type`, `image`, `rate`, `rent_price`, `owner_id`) values
('This is a very nice car!','suv', 'Tesla', 'red', '4', 'ELECTRIC', 'Car/TeslaS.jpeg', '4.5', '2000', '1'),
('A very pretty car!','truck', 'Ford', 'yellow', '2', 'GASOLINE', 'Car/FordT.jpeg', '4.8', '120', '2'),
('Good!','suv', 'Tesla', 'white', '6', 'ELECTRIC', 'Car/TeslaY.jpeg', '4.5', '150', '1'),
('Good!','suv', 'BMW', 'black', '5', 'GASOLINE', 'Car/Benz.webp', '4.5', '300', '1'),
('Good!','car', 'Cadillac', 'white', '5', 'GASOLINE', 'Car/caidi.jpeg', '4.5', '100', '1');

-- --------------------------------------------------------

insert into `review` (`review`, `rate`, `date`, `renter_trips_taken`, `customer_id`, `car_id`) values
('This car helps me a lot. Nice~', '4', '2022-05-01', '23', '1', '2'),
('Great experience, bro!', '5', '2022-05-03', '11', '3', '2');

-- --------------------------------------------------------

insert into `order` (`cost`, `order_date`, `begin_date`, `return_date`, `car_id`, `customer_id`) values
('200', '2022-04-12', '2022-04-13', '2022-04-16', '2', '100'),
('150', '2022-04-20', '2022-04-21', '2022-04-23', '2', '300');

-- --------------------------------------------------------

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
