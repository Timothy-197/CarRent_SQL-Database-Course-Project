SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `CarRental` ;
CREATE SCHEMA IF NOT EXISTS `CarRental` DEFAULT CHARACTER SET UTF8MB4 ;
USE `CarRental` ;

-- ------------------------------------------------------------------
-- the following codes define the tables in this Car Rental System
-- (ref: https://www.inettutor.com/source-code/car-rental-system-database-design/)
-- ------------------------------------------------------------------

-- create car table
create table `car` (
    `car_id` int NOT NULL AUTO_INCREMENT,
    `description` varchar(400) NOT NULL,
    `category` varchar(25) NOT NULL,    -- TODO: make it a foreign key?
    `brand` varchar(25) NOT NULL,       -- TODO: make it a foreign key?
    `color` varchar(15) NOT NULL,
    `capacity` decimal(3, 0) NOT NULL,
    `fuel_type` varchar(25) NOT NULL,
    `image` varchar(200),              -- `image` blob NOT NULL,
    `rate` float DEFAULT 5,
    `rent_price` float NOT NULL,
    `valid` bit NOT NULL DEFAULT 1,     -- 1: valid; 0: invalid (when owner "delete: a car, the car becomes invalid)
    `owner_id` int NOT NULL,

    primary key (`car_id`),
    foreign key (`owner_id`) references `owner`(`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create review table
create table `review` (
    `review_id` int NOT NULL AUTO_INCREMENT,
    `review` varchar(500) NOT NULL,
    `rate` decimal(1, 0) NOT NULL,
    `date` date NOT NULL,
    `renter_trips_taken` decimal(4, 0) NOT NULL,
    `customer_id` int NOT NULL,
    `car_id` int NOT NULL,

    primary key (`review_id`),
    foreign key (`customer_id`) references `customer`(`customer_id`),
    foreign key (`car_id`) references `car`(`car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create customer table
create table `customer` (
    `customer_id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `gender` varchar(10) NOT NULL,
    -- `age` decimal(3, 0) NOT NULL,
    `address` varchar(200) NOT NULL,
    `email` varchar(100) NOT NULL,
    `balance` decimal(8, 0) NOT NULL,
    -- `profile_image` blob NOT NULL,
    -- `username` varchar(30) NOT NULL,
    `password` varchar(30) NOT NULL,    -- plaintext / ciphertext

    primary key (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create owner table
create table `owner` (
    `owner_id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `gender` varchar(10) NOT NULL,
    -- `age` decimal(3, 0) NOT NULL,
    `address` varchar(100) NOT NULL,
    `email` varchar(100) NOT NULL,
    -- `profile_image` blob NOT NULL,
    -- `username` varchar(30) NOT NULL,
    `password` varchar(30) NOT NULL,

    primary key (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create order table
-- correspond to `rental` table in ref
create table `order` (
    `order_id` int NOT NULL AUTO_INCREMENT,
    `cost` float NOT NULL,
    `order_date` date NOT NULL,
    -- `rental_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `begin_date` date NOT NULL,
    `return_date` date NOT NULL,
    `returned` bit NOT NULL DEFAULT 0,
    -- `owner_id` int NOT NULL,
    `car_id` int NOT NULL,
    `customer_id` int NOT NULL,
    -- `rental_status` decimal(2, 0) NOT NULL,

    primary key (`order_id`),
    -- foreign key (`owner_id`) references `owner`(`owner_id`),
    foreign key (`car_id`) references `car`(`car_id`),
    foreign key (`customer_id`) references `customer`(`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- ------------------------------------------------------------------
-- tables for OLAP
-- (for analysis purpose only, no need to be updated)
-- ------------------------------------------------------------------

-- create car_rental_demand table
create table `car_rental_demand` (
    `date` date NOT NULL,
    `hour` decimal(2, 0) NOT NULL,
    `demand` decimal(5, 0) NOT NULL,

    primary key (`date`, `hour`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
