from django.conf.urls import url

from . import views

urlpatterns=[
    #查看本人的全部笔记
    url(r'^showall',views.showall),
    url(r'^new',views.new),#新建笔记
    url(r'^del/(\d+)',views.delete),#删除笔记
    url(r'^mod/(\d+)',views.modify),#修改笔记
]