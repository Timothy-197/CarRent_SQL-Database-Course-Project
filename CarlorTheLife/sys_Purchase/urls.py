from django.urls import path

from sys_Purchase.views import index, buy

'''
Purchase suburls
'''
urlpatterns=[
    path('<int:showidx>/', index.index, name='index'),
    path('rent/<int:car_id>', buy.rent, name = "rent")

]

app_name = "sys_Purchase"