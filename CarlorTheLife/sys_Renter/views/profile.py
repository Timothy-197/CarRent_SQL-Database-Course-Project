import random
from django.shortcuts import render

from sys_Purchase.models import  Car
from sys_Customer.models import  Order

from sys_RegLog.models import  Customer, Owner

def index(request, pIndex=1):
    '''
    UserProfile: index
    '''

    user_order_mod = Order.objects
    car_mod = Car.objects
    current_user_id = request.user.id
    user_car_list = []
    user_order_merge_list = []
    if request.user.profile.user_is_customer == 1:
        current_customer_owner = Customer.objects.get(user_id = current_user_id)
        user_order_list = user_order_mod.filter(customer_id = current_customer_owner.customer_id, returned = 0)
        user_car_list = []
        for i in range(len(user_order_list)):
            user_car_list.append(user_order_list[i].car)
        for j in range(len(user_order_list)):
            tmp_dict = {"order":user_order_list[j],"car":user_car_list[j]}
            user_order_merge_list.append(tmp_dict)
    else:
        current_customer_owner = Owner.objects.get(user_id = current_user_id)
        user_car_list = car_mod.filter(owner_id =current_customer_owner.owner_id)
        user_car_list = user_car_list.filter(valid = 1)


    context = {"customer": current_customer_owner,"user_order_merge_list": user_order_merge_list, "user_car_list":user_car_list}
    return render(request, "sys_Renter/profile/index.html", context)
