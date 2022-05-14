from django.urls import path

from sys_Customer import views
urlpatterns = [
    path('nft/<int:pIndex>/', views.index, name="nft_index"), # 浏览
    path('nft/return/<int:order_id>', views.return_car, name="return_car")

]

app_name = "sys_Customer"