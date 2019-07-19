from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from . import models

def mylogin(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取表单的数据
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 验证用户名，密码是否正确
        try:
            user = models.User.objects.get(name=username,
                                           password=password)
            # 在当前连接的Session中记录当前用户的信息
            request.session['userinfo'] = {
                "username": user.name,
                'id': user.id
            }
            return HttpResponseRedirect('/')  # 回到首页
        except:
            return HttpResponse("登陆失败")



def mylogout(request):
    '退出登陆'
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/')  # 注销后跳转到主页



# def myregister(request):
#     if request.method == 'GET':
#         return render(request, 'userinfo/register.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         password2 = request.POST.get('password2', '')
#         if username == '':
#             username_error = "用户名不能为空"
#             return render(request, 'userinfo/register.html', locals())
#         if password == '':
#             return HttpResponse("密码不能为空")
#         if password != password2:
#             return HttpResponse('两次密码不一致!')
#         # 开始注册功能
#         try:
#             from . import models
#             user = models.User.objects.create(
#                 name=username,
#                 password=password
#             )
#             return HttpResponse("注册成功")
#         except:
#             return HttpResponse("注册失败")

