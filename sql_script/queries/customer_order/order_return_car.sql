update `order`
set `order`.returned = 1     -- set to 1 to indicate True, i.e. customer has returned the car
where `order`.order_id = 1;  -- add parameter here, something like: "where `order`.order_id = %s"