select `car`.car_id, `car`.description, `car`.category, `car`.brand, `car`.color, `car`.capacity, `car`.fuel_type, `car`.image, `car`.rate, `car`.rent_price, `owner`.owner_id, `owner`.name, `owner`.gender, `owner`.address, `owner`.email
from `car`, `owner`
where valid = 1 and 
	`car`.owner_id = `owner`.owner_id and
    
    -- add car_id below to see exact car info
    `car`.car_id = 1;