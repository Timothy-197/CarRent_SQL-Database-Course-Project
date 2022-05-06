UPDATE `customer`
SET `name` = "New Name", `gender` = 'female', `address` = 'new address', `email` = "new-email@demo.com", `balance` = 1200, `password` = "123456"
WHERE `customer_id` = 1;


-- 我认为后端可以这样调用
-- %s 表示挖坑的地方
-- UPDATE `customer`
-- SET %s
-- WHERE `customer_id` = %s;