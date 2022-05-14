*******建立数据库步骤********
第一步
新建一个数据库，名字为CarRental3

第二步 （在ColorTheLife文件夹下）
python3 manage.py makemigrations sys_RegLog
python3 manage.py makemigrations sys_Purchase
python3 manage.py makemigrations sys_ColorTile
python3 manage.py migrate

第三步 （在sql_script文件夹下）
跑 db_init.sql

After setting the database of the project, you can start to execute the program.You can execute the following command in your terminal:

python3 manage.py runserver 9090

Then you need to go to a web server type the following web address:

http://127.0.0.1:9090/reglog/

Finally you can start to use the web !!!

*****前端文件位置（都在templates里）：******

(1)关于注册登录的还是在 sys_RegLog

(2) base.html 在sys_ClockIn

(3) 商家已经上架车的信息：sys_ClockIn/goal/index2.html
    商家upload car: sys_ClockIn/goal/goal_add2.html

(4) 用户订单信息： sys_ColorTile/nft/index.html
    租车商城： sys_Purchase/shop/index.html

(5) 单独的那个profile页面： sys_ClockIn/profile/index.html
    更新profie: sys_RegLog/profile2.html