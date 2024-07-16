from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    """
    处理注册请求并返回注册模板。

    此函数接收一个HTTP请求，将其渲染成注册的HTML响应。
    用于展示注册页面的内容。

    参数:
    - request: HttpRequest对象，包含客户端的请求信息。

    返回:
    - HttpResponse对象，包含渲染后的注册HTML内容。
    """
    #如果是GET 请求返回注册页面
    if request.method == 'GET':
        return render(request, 'register.html')
    #如果是POST 请求则进行注册操作
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 重定向到登录页面
        else:
            form = UserCreationForm()
            return render(request, 'register.html', {'form': form})