from django.shortcuts import render,redirect,get_object_or_404
from  django.views.generic  import   View
from  django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from  user.models import User_Info
from  .models import Create_Topic
from  .forms import    PubTopic,Comment_Forms
from  operation.models import Topic_Comment


import  markdown




# Create your views here.



class  Index_View(View):
    '''
    查看所有主题标题
    '''
    def  get(self,request,page_id):
        topic_list=Create_Topic.objects.all().order_by('-pub_time')
        paginator=Paginator(topic_list,10)
        page_range=paginator.page_range
        page=request.GET.get(page_id)
        test=page_id
        #test=page
        try:
            topics=paginator.page(page_id)
            #test=topics
        except  PageNotAnInteger:
            topics=paginator.page(1)
            #test=topics
        except EmptyPage:
            topics=[]
                #paginator.page(paginator.num_pages)
        #处理侧边栏信息

        return  render(request,'topic/base.html',{'topics':topics,'page_id':(page_id+1)})




class  PubTopic_View(View):
    '''
    发布主题
    '''
    def  get(self,request,username):
        forms=PubTopic()
        return render(request, 'topic/create_topic.html',{'forms':forms})
    def  post(self,request,username):
        forms=PubTopic(request.POST)
        if  forms.is_valid():
            node=forms.cleaned_data["node"]
            title=forms.cleaned_data["title"]
            if  Create_Topic.objects.filter(title=title).exists():
                return  render(request,'topic/create_topic.html',{'forms':forms,'message':'该标题已经存在,请换一个标题'})
            content=forms.cleaned_data['content_raw']
            content=content.replace("<", " &lt;")
            content=content.replace(">", "&gt;")
            topic=Create_Topic()
            topic.user=User_Info.objects.get(username=username)
            topic.title=title
            topic.node=node
            topic.content=content
            topic.save()
            return  redirect(to='topic:index')
        else:
            return render(request,'topic/create_topic.html',{'forms':forms,'message':'输入的数据无法通过检查，请重新输入'})


class  Topic_Content_View(View):
    '''
    文章详细内容展示
    '''
    def  get(self,request,content_id):

        forms = Comment_Forms()
        topic_content=Create_Topic.objects.get(id=content_id)
        time=topic_content.pub_time
        title=topic_content.title
        name=topic_content.user.username
        node=topic_content.node
        content=markdown.markdown(
            topic_content.content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )

        comment=topic_content.topic_comment_set.all().order_by('-add_time')
        len_comment=len(comment)
        for  each_comment  in  comment:
            markdown_comment=markdown.markdown(
            each_comment.content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
            each_comment.content=markdown_comment


        return render(request, 'topic/topic_content.html',{'content_topic':topic_content,"time": time, "title": title, "name": name, "content": content, "node": node,'forms':forms,'comment':comment,'len_comment':len_comment})




'''
    def  post(self,request,content_id):

        topic=Create_Topic.objects.get(id=content_id)
        login_user=User_Info.objects.get(username=request.user.username)
        forms=Comment_Forms(request.POST)
        if  forms.is_valid():
            comment_content=forms.cleaned_data["content_raw"]
            comment=Topic_Comment()
            comment.user=login_user
            comment.topic=topic
            comment.content=comment_content
            comment.save()

            return  render(request,'topic/topic_content.html',{'comment':comment,'forms':forms,'content_id':content_id})

'''







def  default_index(request):
    return  redirect(to='page/1')


'''
redirect  
可传递的参数： 
一个模型对象：这个模型的get_absolute_url() 会被调用。 
一个视图名称，可带参数，该视图会被反向生成。 
一个绝对路径或相对路径，用作反向定位。
'''


class  Theme1_View(View):
    def  get(self,request,theme_id):
        reservedict={
            '1':'生物知识',
            '2':'生物信息',
            '3':'生活交流',
            '4':'生信编程',
            '5':'计算机学习',
            '6':'django学习',
            '7':'论坛公告'
        }
        node_id=reservedict[str(theme_id)]
        theme1=Create_Topic.objects.filter(node=node_id)
        return render(request,'topic_base.html',{'theme':theme1,'theme_id':theme_id})




