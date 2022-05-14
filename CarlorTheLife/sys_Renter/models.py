from django.db import models
from datetime import datetime,timedelta

from yaml import MappingStartEvent
from django.utils import timezone
import pytz

# #用户信息模型
# class Goal(models.Model):
#     username = models.CharField('username', max_length=50) # username
#     goalname = models.CharField('goalname', max_length=50,default = "") #goalname
#     description = models.CharField(max_length=50) # description
#     #password_hash = models.CharField(max_length=100) # 删掉
#     #password_salt = models.CharField(max_length=50)  # 删掉
#     status = models.IntegerField(default=1) 
#     create_at = models.DateTimeField(default=datetime.now)
#     update_at = models.DateTimeField(default=datetime.now)
#     dead_line = models.DateTimeField(default=(datetime.now()-timedelta(days=1)))
#     #finish_at

#     '''
#     def toDict(self):
#         #return {'id':self.id,'username':self.username,'name':self.name,'password':self.password,'address':self.address,'phone':self.phone,'email':self.email,'state':self.state,'addtime':self.addtime}
#         #没改！
#         return 0
#     '''

#     class Meta:
#         db_table = "user_goal"  # 更改表名 # 改成goal
#         verbose_name = 'Users\' Goal'  
#         verbose_name_plural = 'User_Goal Management'


# # Goals that finished
# class Goal_Finished(models.Model):
#     username = models.CharField(max_length=50) #username
#     goalname = models.CharField('goalname', max_length=50,default = "") #goalname
#     description = models.CharField(max_length=50) # description
#     #password_hash = models.CharField(max_length=100) # 删掉
#     #password_salt = models.CharField(max_length=50)  # 删掉
#     finish_at = models.DateTimeField(default=datetime.now)
#     status = models.IntegerField(default=4)

#     '''
#     def toDict(self):
#         #return {'id':self.id,'username':self.username,'name':self.name,'password':self.password,'address':self.address,'phone':self.phone,'email':self.email,'state':self.state,'addtime':self.addtime}
#         #没改！
#         return 0
#     '''

#     class Meta:
#         db_table = "user_goal_finished"  # 更改表名 # 改成goal
#         verbose_name = 'Finished Goal'  
#         verbose_name_plural = 'Goal_Finished Management'
