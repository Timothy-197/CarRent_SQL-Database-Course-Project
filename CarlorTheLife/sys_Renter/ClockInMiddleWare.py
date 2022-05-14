from django.shortcuts import redirect
from django.urls import reverse
import re

# To make sure that only login user can see/use the ClockIn system and Reset_Passed system
class ClockInMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        path = request.path

        # 打卡界面
        if re.match(r'^/clockin',path) or re.match(r'^/reglog/reset_pwd',path):

            if request.user.id is None:
                return redirect("sys_RegLog:login")                




        response = self.get_response(request)

        return response