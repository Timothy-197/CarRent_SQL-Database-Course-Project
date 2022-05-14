# 用户goal管理
from re import U
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.core.paginator import Paginator
from pyrsistent import plist #用于信息分页
from django.db.models import Q
from pytz import UTC #用于“或”多条件搜索
# Create your views here.
from sys_Customer.models import  Order
from sys_Purchase.models import Car
from sys_RegLog.models import Customer

from datetime import datetime,timedelta


def index(request, pIndex=1):

    sel_time = None
    sel_returned = None
    if request.method == 'POST':
        print("POSTPSOT")
        sel_time = request.POST.get('order_time')
        sel_returned = request.POST.get('returned')



    current_user = request.user
    current_user_id = current_user.id

    current_customer = Customer.objects.get(user_id = current_user_id)
    current_customer_id = current_customer.customer_id


    ###
    user_order_mod = Order.objects

    user_order_list_0 = user_order_mod.filter(customer_id = current_customer_id)

    if sel_returned != None and sel_returned != "All":
        if sel_returned == "yes":
            user_order_list_0 = user_order_list_0.filter(returned = 1)
        elif sel_returned == "no":
            user_order_list_0 = user_order_list_0.filter(returned = 0)


    user_order_list = []

    if sel_time != None and sel_time != "All":
        current_time = datetime.date(datetime.now())
        if (sel_time == "week"):
            time_back = timedelta(days = 1)
        elif (sel_time == "month"):
            time_back = timedelta(days = 30)        
        elif (sel_time == "year"):
            time_back = timedelta(days = 365)
        for user_order_entry in user_order_list_0:
            if user_order_entry.order_date >= (current_time - time_back):
                user_order_list.append(user_order_entry)
    else:
        user_order_list = user_order_list_0

        
    user_car_list = []
    for i in range(len(user_order_list)):
        user_car_list.append(user_order_list[i].car)
    
    
    
    ## search 获取并判断搜索条件 ##
    mywhere=[]
    keywords = request.GET.get("table_search_nft", None)
    if keywords:
        user_order_list = user_order_list.filter(Q(order_id__contains=keywords) | Q(order_date__contains=keywords)) ### 调整完model之后要改
        mywhere.append('table_search_nft='+keywords)


    page = Paginator(user_order_list, 5)
    n_maxpages = page.num_pages

    pIndex = int(pIndex) # 当前页码
    # 判断当前页是否越界
    if pIndex > n_maxpages:
        pIndex = n_maxpages
    if pIndex < 1:
        pIndex = 1



    user_order_list2 = page.page(pIndex) # 获取当前页数据
    plist = page.page_range # 获取当前页码列表信息


    user_car_list2 = []
    for i in range(len(user_order_list2)):
        user_car_list2.append(user_order_list2[i].car)

    returned_list = []
    for i in range(len(user_order_list2)):
        if user_order_list2[i].returned == b'\x01':
            returned_list.append(1)
        else:
            returned_list.append(0)

    cross_ddl_list = []
    current_time = datetime.date(datetime.now())
    for i in range(len(user_order_list2)):
        return_time = user_order_list2[i].return_date
        if current_time > return_time:
            cross_ddl_list.append(1)
        else:
            cross_ddl_list.append(0)
    


    order_merge_list = []
    for i in range(len(user_order_list2)):
        tmp_dict = {"order": user_order_list2[i], "car": user_car_list2[i], "returned":returned_list[i], "cross_ddl":cross_ddl_list[i]}
        order_merge_list.append(tmp_dict)

    if sel_returned == None or sel_returned == "All":
        sel_returned = "Returned: All"
    if sel_time == None or sel_time== "All":
        sel_time = "Order Time: All"
    
    if sel_time == "week":
        sel_time = "Within a Week"
    elif sel_time == "month":
        sel_time = "Within a Month"
    elif sel_time == "year":
        sel_time = "Within a Year"

    if sel_returned == "yes":
        sel_returned = "Yes"
    if sel_returned == "no":
        sel_returned = "No"    

    context = {"order_merge_list":order_merge_list,"plist":plist, 'pIndex':pIndex, 'maxpages':n_maxpages, 'mywhere':mywhere, "sel_time":sel_time,"sel_returned":sel_returned}
    return render(request, "sys_Customer/nft/index.html",context)



def return_car(request, order_id):
    returned_order = Order.objects.get(order_id = order_id)
    returned_order.returned = 1
    returned_order.save()

    car_id = returned_order.car_id
    car = Car.objects.get(car_id = car_id)
    car.returned = 1
    car.valid = 1
    car.save()
    return redirect("sys_Customer:nft_index",pIndex=1)
