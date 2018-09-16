from django.shortcuts import render,redirect
from  django.http  import  HttpResponse
from  django.views.generic import  View  #继承通用类视图
from  django.contrib.auth  import  authenticate,login,logout
from  django.contrib.auth.hashers import make_password  #对数据库进行加密
import  markdown


from  topic.models import Create_Topic
from  operation.models import Topic_Comment
from  .models import User_Info
from  .forms import Login,Register
# Create your views here.

class  Login_View(View):
    nav_base = 'nav_base.html'
    def   get(self,request):
        forms=Login()
        return  render(request,'user/login.html',{'login':forms})


    def  post(self,request):
        forms=Login(request.POST)
        if  forms.is_valid():
            user_name=forms.cleaned_data['username']
            pass_word=forms.cleaned_data["password"]
            user=authenticate(username=user_name,password=pass_word)
            if   user  is  not  None:
                login(request,user)
                return  redirect(to='topic:index')

            else:
                forms=Login()
                return  render(request,'user/login.html',{'login':forms,'messsge':'您输入的用户名或者密码验证有误'})

        else:
            forms=Login()
            return render(request,'user/login.html',{'login':forms,'message':'您输入的信息不全'})



def  logout_view(request):
    logout(request)
    return  redirect(to='topic:index')


"""
注册用户相关操作
"""

class  Register_Voew(View):
    def  get(self,request):
        forms=Register()
        return render(request,'user/register.html',{'forms':forms})
    def  post(self,request):
        forms=Register(request.POST)
        if  forms.is_valid():
            username=forms.cleaned_data["username"]
            if  User_Info.objects.filter(username=username):
                return  render(request,'user/register.html',{'message':'该用户名已经被注册过了!','forms':forms})
            else:
                password=forms.cleaned_data["password1"]
                password1=forms.cleaned_data["password"]
                if  password!=password1:
                    return  render(request,'user/register.html',{'message':'您两次输入的密码不相同','forms':forms})
                else:
                    mobile=forms.cleaned_data["mobile"]
                    email=forms.cleaned_data["email"]
                    user=User_Info()
                    user.username=username
                    user.password=make_password(password)
                    user.mobile=mobile
                    user.email=email
                    user.save()
                    return  redirect(to='user:login')
        else:
            return  render(request,'user/register.html',{'message':'您的信息不符合要求，可能是验证码有误，请您核对信息','forms':forms})


class  Info_Profile(View):
    '''
    个人主题数量
    '''
    def  get(self,request,username1):
        userinfo=User_Info.objects.get(username=username1)
        reservedict1={
             '生物知识':'1',
             '生物信息':'2',
           '生活交流':'3',
             '生信编程':'4',
            '计算机学习':'5',
             'django学习':'6',
            '论坛公告':'7'

        }
        reservedict = {
            '1': '生物知识',
            '2': '生物信息',
            '3': '生活交流',
            '4': '生信编程',
            '5': '计算机学习',
            '6': 'django学习',
            '7': '论坛公告'
        }
        user_theme=userinfo.create_topic_set.all()
        user_reply=userinfo.topic_comment_set.all()
        return  render(request,'topic/info_profile.html',{'userinfo':userinfo,'user_theme':user_theme,'user_reply':user_reply})



class  Info_Reply(View):
    def  get(self,request,username1):
        userinfo = User_Info.objects.get(username=username1)
        user_reply = userinfo.topic_comment_set.all()
        for  each_user_reply  in  user_reply:
            reply=each_user_reply.content
            markdown_comment = markdown.markdown(
                reply,
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
            each_user_reply.content=markdown_comment


        return  render(request,'topic/info_reply.html',{'userinfo':userinfo,'all_user_reply':user_reply})





