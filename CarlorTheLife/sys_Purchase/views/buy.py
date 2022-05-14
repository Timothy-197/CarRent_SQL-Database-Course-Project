from django.shortcuts import redirect
from sys_Purchase.models import  Car
from sys_ColorTile.models import  Order
from sys_RegLog.models import Customer

from datetime import datetime,timedelta

def rent(request, car_id):
    current_user = request.user
    current_user_id = current_user.id
    current_customer = Customer.objects.get(user_id = current_user_id)

    selected_car = Car.objects.get(car_id = car_id)
    cost = selected_car.rent_price
    order_date = datetime.now()
    begin_date = order_date + timedelta(days=1)
    return_date = begin_date + timedelta(days = 30)
    car_id = car_id
    customer_id = current_customer.customer_id

    current_customer.balance = float(current_customer.balance) - cost
    current_customer.save()

    # insert into `order` (`cost`, `order_date`, `begin_date`, `return_date`, `car_id`, `customer_id`) values
    # ('200', '2022-04-12', '2022-04-13', '2022-04-16', '2', '1');
    Order.objects.create(cost = cost, order_date = order_date, begin_date = begin_date, return_date = return_date, car_id = car_id, customer_id = customer_id, returned = 0)

    car = Car.objects.get(car_id = car_id)
    car.returned = 0
    car.valid = 1
    car.save()

    return redirect("sys_Purchase:index",showidx=1)


