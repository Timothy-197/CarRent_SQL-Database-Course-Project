-- ref: https://www.mysqltutorial.org/import-csv-file-mysql-table/

USE `CarRental` ;

LOAD DATA INFILE 'E:\repo_Chen-Gary\CSC3170_CarRent_SQL\sql_script\OLAP\Car_Rental_Demand\train_E1GspfA.csv' 
INTO TABLE `car_rental_demand` 
FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- BULK INSERT `car_rental_demand`
-- FROM 'E:\repo_Chen-Gary\CSC3170_CarRent_SQL\sql_script\OLAP\Car_Rental_Demand\train_E1GspfA.csv'
-- WITH (
-- 	FORMAT = 'CSV',
--     FIRSTROW = 2,
--     FIELDTERMINATOR = ',',
-- );
