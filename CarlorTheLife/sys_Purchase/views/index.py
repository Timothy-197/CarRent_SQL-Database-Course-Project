from django.shortcuts import render,redirect
from sys_Purchase.models import  Car

from django.db.models import Q
from django.contrib import messages
from sys_RegLog.models import Customer

def index(request, showidx=1):
    '''
    car shop 首页
    '''
    sel_brand = None
    sel_color = None
    sel_category = None
    sel_fuel_type = None
    if request.method == 'POST':
        print("POST HERE!")
        sel_brand = request.POST.get('brand')
        print("Brand: ")
        print(sel_brand)
        sel_color = request.POST.get('color')
        sel_category = request.POST.get('category')
        sel_fuel_type = request.POST.get('fuel_type')
    

    CarList = Car.objects.filter(valid = 1, returned = 1)

    if sel_color != None and sel_color != "All":
        CarList = CarList.filter(color = sel_color)
    if sel_brand != None and sel_brand != "All":
        CarList = CarList.filter(brand = sel_brand)
    if sel_category != None and sel_category != "All":
        CarList = CarList.filter(category = sel_category)
    if sel_fuel_type != None and sel_fuel_type != "All":
        CarList = CarList.filter(fuel_type = sel_fuel_type)


    keywords = request.GET.get("table_search_shop", None)
    if keywords:
        CarList = CarList.filter(Q(description__contains=keywords) | Q(brand__contains=keywords) | Q(color__contains=keywords))

    #if no such car after search, return to the shop main page
    if len(CarList) == 0:
        messages.success(request, "No such car in shop")
        return redirect("sys_Purchase:index", showidx=1)
   

    if showidx < 1:
        showidx = 1
    elif showidx > len(CarList):
        showidx = len(CarList)
    showidx = showidx - 1    

    
    ShowCar = CarList[showidx]

    if sel_brand == None or sel_brand == "All":
        sel_brand = "Brand: All"
    if sel_color == None or sel_color == "All":
        sel_color = "Color: All"
    if sel_category == None or sel_category == "All":
        sel_category = "Category: All"
    if sel_fuel_type == None or sel_fuel_type == "All":
        sel_fuel_type = "Fuel_Type: All"    
    


    current_user = request.user
    current_user_id = current_user.id

    current_customer = Customer.objects.get(user_id = current_user_id)
    current_customer_id = current_customer.customer_id

    ShowCarFlag = None
    if ShowCar.rent_price < current_customer.balance:
        ShowCarFlag = 1
    else:
        ShowCarFlag = 0

    context = {'Carlist':CarList,'ShowCar':ShowCar, 'ShowCarFlag':ShowCarFlag,"current_customer":current_customer,"sel_brand": sel_brand, "sel_color":sel_color, "sel_category":sel_category,"sel_fuel_type":sel_fuel_type}
    return render(request, "sys_Purchase/shop/index.html", context)


