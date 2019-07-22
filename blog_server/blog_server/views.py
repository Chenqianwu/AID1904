from django.http import JsonResponse


def test_api(request):
    #JsonResponse 1,将返回内容序列化成json
    #2,response中添加 content-type: application/json
    return JsonResponse({'code':200})