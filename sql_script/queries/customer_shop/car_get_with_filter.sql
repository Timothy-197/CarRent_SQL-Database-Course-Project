select `car`.car_id, `car`.description, `car`.category, `car`.brand, `car`.color, `car`.capacity, `car`.fuel_type, `car`.image, `car`.rate, `car`.rent_price, `owner`.owner_id, `owner`.name, `owner`.gender, `owner`.address, `owner`.email
from `car`, `owner`
where valid = 1 and 
	`car`.owner_id = `owner`.owner_id and
    
    -- add filter below
    -- `car`.category = "suv"
    -- `car`.brand = "Ford"
    -- `car`.color = "red"
    -- `car`.capacity = 4
    -- `car`.fuel_type = "ELECTRIC"
    -- `car`.rate > 4.6
    `car`.rent_price < 100
    ;