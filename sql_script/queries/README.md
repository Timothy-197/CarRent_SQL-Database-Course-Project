**每个页面与对应的query**



* login_register (注册/登录)
  * 查询customer/owner密码 - 通过邮箱
  * 新增customer/owner



* customer_shop (商店页面)
  * 查询所有的car
  * 带filter查询car
  * insert new order
  * 更新customer balance（在下订单后扣钱）
  * 查询特定的car
  
* customer_order (用户订单页面)
  * 查询所有当前order
  * 用户归还car
  * （关键字搜索）
* customer_profile (用户信息)
  * 查询自己的profile - 通过email
  * 更新profile
* customer_home (用户homepage)
  * 用户历史订单数
  * ...



* owner_profile (商家信息)
  * 查询自己的profile - 通过email
  * 更新profile
* owner_car_manage (商家管理自己的车)
  * 查询自己的car
  * 删除已有的car
  * ~~(查询跟自己车有关的order)~~
* owner_add_car (上架新car页面)
  * 上架新的car