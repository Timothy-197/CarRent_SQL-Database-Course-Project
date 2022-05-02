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
-- TODO: car image - a separate table?
create table `car` (
    `car_id` int NOT NULL AUTO_INCREMENT,
    `description` varchar(100) NOT NULL,
    `brand` varchar(25) NOT NULL,       -- TODO: make it a foreign key?
    `color` varchar(15) NOT NULL,
    `capacity` decimal(3, 0) NOT NULL,
    `rate` float NOT NULL,
    `owner_id` int NOT NULL,

    primary key (`car_id`),
    foreign key (`owner_id`) references `owner`(`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create review table
create table `review` (
    `review_id` int NOT NULL AUTO_INCREMENT,
    `review` varchar(100) NOT NULL,
    `rate` decimal(1, 0) NOT NULL,
    `date` date NOT NULL,
    `customer_id` int NOT NULL,
    `car_id` int NOT NULL,

    primary key (`review_id`),
    foreign key (`customer_id`) references `customer`(`customer_id`),
    foreign key (`car_id`) references `car`(`car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create customer table
create table `customer` (
    `customer_id` int NOT NULL AUTO_INCREMENT,
    `customer_name` varchar(50) NOT NULL,
    `address` varchar(100) NOT NULL,
    `contact` varchar(11) NOT NULL,
    -- `profile_image` blob NOT NULL,
    -- `username` varchar(30) NOT NULL,
    `password` varchar(30) NOT NULL,    -- plaintext / ciphertext

    primary key (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create owner table
create table `owner` (
    `owner_id` int NOT NULL AUTO_INCREMENT,
    `owner_name` varchar(50) NOT NULL,
    `address` varchar(100) NOT NULL,
    `contact` varchar(11) NOT NULL,
    -- `profile_image` blob NOT NULL,
    -- `username` varchar(30) NOT NULL,
    `password` varchar(30) NOT NULL,

    primary key (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- create order table
-- correspond to `rental` table in ref
create table `order` (
    `order_id` int NOT NULL AUTO_INCREMENT,
    `order_date` date NOT NULL,
    -- `rental_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `begin_date` date NOT NULL,
    `return_date` date NOT NULL,
    `owner_id` int NOT NULL,
    `car_id` int NOT NULL,
    `customer_id` int NOT NULL,
    -- `rental_status` decimal(2, 0) NOT NULL,

    primary key (`order_id`),
    foreign key (`owner_id`) references `owner`(`owner_id`),
    foreign key (`car_id`) references `car`(`car_id`),
    foreign key (`customer_id`) references `customer`(`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;



-- tables for OLAP (for analysis purpose only, no need to be updated)
-- TODO...


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
