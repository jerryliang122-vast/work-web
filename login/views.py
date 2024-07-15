from django.shortcuts import render

# Create your views here.

def index(request):
    """
    处理主页请求并返回主页模板。

    此函数接收一个HTTP请求，将其渲染成主页的HTML响应。
    它是网站的入口点，用于展示主页的内容。

    参数:
    - request: HttpRequest对象，包含客户端的请求信息。

    返回:
    - HttpResponse对象，包含渲染后的主页HTML内容。
    """
    return render(request, 'index.html')