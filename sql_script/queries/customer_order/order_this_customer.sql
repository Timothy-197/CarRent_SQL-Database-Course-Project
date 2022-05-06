-- select `order`.*, `car`.*
select `order`.order_id, `order`.cost, `order`.order_date, `order`.begin_date, `order`.return_date, `order`.returned, `car`.category, `car`.brand, `car`.color, `car`.capacity, `car`.fuel_type, `car`.image
from `order`, `car`
where `order`.car_id = `car`.car_id
	and `order`.customer_id = 1;