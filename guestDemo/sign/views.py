# -*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, "index.html")


# 登录
def login_action(request):
    if request.method == "POST":
        # 寻找名为 "username"和"password"的POST参数，而且如果参数没有提交，返回一个空的字符串。
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == '' or password == '':
            return render(request, "index.html", {"error": "username or password null!"})

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 验证登录
            response = HttpResponseRedirect('/event_manage/')  # 登录成功跳转发布会管理
            request.session['username'] = username  # 将 session 信息写到服务器
            return response
        else:
            return render(request, "index.html", {"error": "username or password error!"})
    # 防止直接通过浏览器访问 /login_action/ 地址。
    return render(request, "index.html")


# 登录成功后管理页面(# 发布会管理)
@login_required  # 限制该视图必须登录才能访问
def event_manage(request):
    # 从cookie中拿到user的value
    # username=request.COOKIES.get('user','')
    # 读取浏览器中的session
    event_list = Event.objects.all()
    username = request.session.get('username', '')
    # event_list['start_time'].strftime('YYYY-MM-DD HH:MM:SS')
    '''
    print event_list[1].start_time
    for i in (len(event_list)-1):
        event_list[i].start_time=event_list[i].start_time.strftime('YYYY-MM-DD HH:MM:SS')
    '''
    # print(len(event_list))
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


# 搜索框发布会名称查询
@login_required
def search_name(request):
    username = request.session.get('username', '')
    search_name = request.GET.get("name", "")
    search_name_bytes = search_name.encode(encoding="utf-8")
    # event_list = Event.objects.filter(name__contains=search_name_bytes)
    event_list = Event.filter(name__contains=search_name_bytes)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 跳转到嘉宾列表
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('username', '')
    return render(request, 'guest_manage.html', {'guests': guest_list, 'user': username})


# 嘉宾搜索功能
@login_required
def search_realname(request):
    username = request.session.get('username', '')
    search_realname = request.GET.get('realname', '')
    # search_realname_bytes=search_realname.encode(encoding='utf-8')
    guest_list = Guest.objects.filter(realname__contains=search_realname)
    return render(request, 'guest_manage.html', {'user': username, 'guests': guest_list})


# 嘉宾分页功能
@login_required
def guest_manage(request):
    username = request.session.get('username', '')
    guest_list = Guest.objects.all()
    # 创建每页2条数据的分页器
    paginator = Paginator(guest_list, 2)
    # 获取页面的page
    page = request.GET.get('page')
    try:
        # 获取第page页的数据
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {'user': username, 'guests': contacts})

# 签到页面
@login_required
def sign_index(request,eid):
    event=get_object_or_404(Event,id=eid)
    guest_list = Guest.objects.filter(event_id=eid)
    sign_list = Guest.objects.filter(sign="1", event_id=eid)
    guest_data = str(len(guest_list))
    sign_data = str(len(sign_list))
    return render(request,'sign_index.html',{'event':event,'sign':sign_data,'guest':guest_data})

# 签到动作
@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html',{'event': event, 'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html',{'event': event, 'hint': 'event id or phone error.'})
    result = Guest.objects.get(event_id=eid, phone=phone)
    if result.sign:
        return render(request, 'sign_index.html',{'event': event, 'hint': "user has sign in."})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!'})

# 退出功能
@login_required
def logout(request):
    # 退出登录
    auth.logout(request)
    response=HttpResponseRedirect('/index/')
    return response