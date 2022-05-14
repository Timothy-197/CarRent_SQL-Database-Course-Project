from django.contrib import admin

# from sys_ColorTile.models import User_NFT,User_ColorTile
# # Register your models here.
# @admin.register(User_NFT)
# class GoalAdmin(admin.ModelAdmin):
#     #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('id','username','nft_id', 'bought_time')

#     #设置哪些字段可以点击进入编辑界面
#     list_display_links = ('id','username',)

#     #list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 10

#     #ordering设置默认排序字段，负号表示降序排序
#     ordering = ('id',)  #-id降序

#     #list_editable 设置默认可编辑字段
#     #list_editable = []


# @admin.register(User_ColorTile)
# class GoalAdmin(admin.ModelAdmin):
#     #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('id','username','user_CT_red', 'user_CT_green', 'user_CT_blue')

#     #设置哪些字段可以点击进入编辑界面
#     list_display_links = ('id','username',)

#     #list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 10

#     #ordering设置默认排序字段，负号表示降序排序
#     ordering = ('id',)  #-id降序

#     #list_editable 设置默认可编辑字段
#     #list_editable = []