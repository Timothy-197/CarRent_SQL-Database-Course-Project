-- 这步用了join，因为要查owner信息
-- 如果有分页功能，可以在最后加上limit
--     参数为 limit <要跳过几个record> <列出几个record>
-- 这里不使用 select * 而是手动列出select列表

select `car`.car_id, `car`.description, `car`.category, `car`.brand, `car`.color, `car`.capacity, `car`.fuel_type, `car`.image, `car`.rate, `car`.rent_price, `owner`.owner_id, `owner`.name, `owner`.gender, `owner`.address, `owner`.email
from `car`, `owner`
where valid = 1 and 
	`car`.owner_id = `owner`.owner_id
    -- limit 1, 1
    ;
