# 用户goal管理
from re import U
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.core.paginator import Paginator
from numpy import byte
from pyrsistent import plist, v #用于信息分页
from django.db.models import Q
from pytz import UTC #用于“或”多条件搜索

from sys_ClockIn.forms import ImageForm
from sys_Purchase.models import Car
from sys_RegLog.models import Owner
from django.db import connection 


def index(request, pIndex=1,status_required = 0):

    current_user_id = request.user.id
    current_owner = Owner.objects.get(user_id = current_user_id)
    current_owner_id = current_owner.owner_id

    ###
    car_mod = Car.objects


    ######
    owner_car_list = car_mod.filter(owner_id = current_owner_id)
    owner_car_list = owner_car_list.filter(valid = 1)
    
    
    
    ## search 获取并判断搜索条件 ##
    mywhere=[]
    keywords = request.GET.get("table_search_nft", None)
    if keywords:
        owner_car_list = owner_car_list.filter(Q(description__contains=keywords) | Q(brand__contains=keywords)) ### 调整完model之后要改
        mywhere.append('table_search_nft='+keywords)


    page = Paginator(owner_car_list, 5)
    n_maxpages = page.num_pages

    pIndex = int(pIndex) # 当前页码
    # 判断当前页是否越界
    if pIndex > n_maxpages:
        pIndex = n_maxpages
    if pIndex < 1:
        pIndex = 1


    owner_car_list2 = page.page(pIndex) # 获取当前页数据
    plist = page.page_range # 获取当前页码列表信息

    returned_list = []
    for i in range(len(owner_car_list2)):
        print(owner_car_list2[i].returned)
        if owner_car_list2[i].returned == b'\x01':
            returned_list.append(1)
        else:
            returned_list.append(0)

    owner_car_merge_list = []
    for i in range(len(owner_car_list2)):
        tmp_dict = {"car":owner_car_list2[i], "returned":returned_list[i]}
        owner_car_merge_list.append(tmp_dict)

    context = {"owner_car_merge_list":owner_car_merge_list,"plist":plist, 'pIndex':pIndex, 'maxpages':n_maxpages, 'mywhere':mywhere}
    return render(request, "sys_ClockIn/goal/index2.html", context)

def add(request):

    if request.method == 'POST':
        description = request.POST.get('description')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        color = request.POST.get('color')
        fuel_type = request.POST.get('fuel_type')
        capacity = request.POST.get('capacity')
        rent_price = request.POST.get('rent_price')

        image = request.FILES['image']

        current_user_id = request.user.id
        current_owner = Owner.objects.get(user_id = current_user_id)
        current_owner_id = current_owner.owner_id

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Save!!!")
            image_entry = form.save()

        image = image_entry.image

        cursor = connection.cursor()
        sql = "insert into `car` (`description`, `category`, `brand`, `color`, `capacity`, `fuel_type`, `image`, `rent_price`, `owner_id`) values\
            ('This is a very nice car!', 'suv', 'Tesla', 'blue', '4', 'ELECTRIC', NULL, '90', '1');"
        sql = "insert into `car` (`description`, `category`, `brand`, `color`, `capacity`, `fuel_type`, `image`, `rent_price`, `owner_id`) values('" + description +"', '" + category + "', '" + brand +"', '" + color + "', " + capacity + ", '" + fuel_type + "', '" +str(image) + "', '" + str(rent_price) + "', '" + str(current_owner_id) + "');"
        print(sql)
        sql2 = "insert into `car` (`description`, `category`, `brand`, `color`, `capacity`, `fuel_type`, `image`, `rent_price`, `owner_id`) values('This is a very nice car!', 'suv', 'Tesla', 'blue', '4', 'ELECTRIC', NULL, '90', '1');"
        print(sql2)
        cursor.execute(sql)

    return render(request, "sys_ClockIn/goal/goal_add2.html")

def delete(request, car_id):
    delete_car_entry = Car.objects.get(car_id = car_id)
    #delete_car_entry.delete()
    print("Is Valid????")
    print(delete_car_entry.valid)
    delete_car_entry.valid = 0
    delete_car_entry.returned = 1
    delete_car_entry.save()
    return redirect('sys_ClockIn:goal_index',pIndex=1, status_required = 0)