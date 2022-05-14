Please follow follow the procedures below to run our project.
(The web page programs are in the "CarlorTheLife" folder)
(The sql scripts are in the "sql_script" folder)
(The data mining programs are in the "data_mining" folder)

*******Steps to build the database********
Step 1
Create a databse named with "CarRental3"

Step 2 (In the file "/CarlorTheLife/ColorTheLife/settings.py")
In line 104, change the password of mysql database to yours

Step 3 （cd to the folder "CarlorTheLife" and run these commands）
python3 manage.py makemigrations sys_RegLog
python3 manage.py makemigrations sys_Purchase
python3 manage.py makemigrations sys_Customer
python3 manage.py migrate

Step 4 （cd to the folder sql_script）
run db_init.sql
run fake_data_populate.sql

*******Run the Web********
After setting the database of the project, you can start to execute the program.You can execute the following command in your terminal:

python3 manage.py runserver 9090

(You should first intall the Django framework)
(And if you encounter an error saying that a package is not installed, please use pip or other methods to install it)
Then you need to go to a web server type the following web address:

http://127.0.0.1:9090/reglog/login/

Finally you can start to use the web !!! 
You should first register an account and then login to enjoy our website!