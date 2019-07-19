from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect

from user.models import User
from . import models
def showall(request):
    if hasattr(request, 'session') and 'userinfo' in request.session:
        # 此时用户已登陆
        # 拿到用户id
        user_id = request.session['userinfo']['id']
        # 根据当前登陆用户找到当前用户
        user = User.objects.get(id=user_id)
        # 根据当前用户筛选出当前用户的笔记
        notes = models.Note.objects.filter(author=user)
        return render(request, 'note/showall.html', locals())
    else:
        raise Http404

def new(request):
    if hasattr(request, 'session') and 'userinfo' in request.session:
        # 此时用户已登陆
        # 拿到用户id
        user_id = request.session['userinfo']['id']
        # 根据当前登陆用户找到当前用户
        user = User.objects.get(id=user_id)
        # 根据当前用户筛选出当前用户的笔记
        anote = models.Note(author=user)
        import random
        anote.title = "自定义标题%d" % random.randrange(10000)
        anote.content = '这是随便写的内容'
        anote.save()
        return HttpResponse("OK")
    else:
        raise Http404

def delete(request, id):
    if hasattr(request, 'session') and 'userinfo' in request.session:
        # 此时用户已登陆
        # 拿到用户id
        user_id = request.session['userinfo']['id']
        # 根据当前登陆用户找到当前用户
        user = User.objects.get(id=user_id)
        try:
            anote = models.Note.objects.get(author=user, id=id)
            anote.delete()
            return HttpResponseRedirect('/note/showall')
        except:
            return HttpResponse("删除失败")
    else:
        raise Http404

def modify(request, id):
    pass
