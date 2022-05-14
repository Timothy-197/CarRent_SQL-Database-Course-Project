from django.urls import path

# from sys_Renter.views import index

from sys_Renter.views import goal

from sys_Renter.views import profile
'''
sys_Renter suburls
'''
urlpatterns=[
    #path('', index.index, name='index'), #用户首页
    path('goal/<int:pIndex>/<int:status_required>', goal.index, name="goal_index"), # 浏览
    path('goal/add', goal.add, name="goal_add"), # 添加表单
    path('goal/del/<int:car_id>', goal.delete, name="goal_del"), # 执行删除
    path('profile/', profile.index, name="profile_index")
]

app_name = "sys_Renter"