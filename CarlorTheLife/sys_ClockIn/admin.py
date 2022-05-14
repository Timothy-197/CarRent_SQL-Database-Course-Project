from django.contrib import admin

# from sys_ClockIn.models import Goal, Goal_Finished
# Register your models here.

# @admin.register(Goal)
# class GoalAdmin(admin.ModelAdmin):
#     #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('id','username','description', 'status', 'create_at')

#     #设置哪些字段可以点击进入编辑界面
#     list_display_links = ('id','username',)

#     #list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 10

#     #ordering设置默认排序字段，负号表示降序排序
#     ordering = ('id',)  #-id降序

#     #list_editable 设置默认可编辑字段
#     #list_editable = []

# @admin.register(Goal_Finished)
# class FinishedGoalAdmin(admin.ModelAdmin):
#     #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('id','username','description', 'status', 'finish_at')

#     #设置哪些字段可以点击进入编辑界面
#     list_display_links = ('id','username',)

#     #list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 10

#     #ordering设置默认排序字段，负号表示降序排序
#     ordering = ('id',)  #-id降序

#     #list_editable 设置默认可编辑字段
#     #list_editable = ['username']