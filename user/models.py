from django.db import models

from  django.contrib.auth.models import AbstractUser



class  User_Info(AbstractUser):
    '''
    用户信息
    '''
    nick_name=models.CharField(max_length=20,verbose_name='昵称',default='')
    mobile=models.CharField(max_length=11,null=False,blank=False,verbose_name='电话号码')
    avatar=models.ImageField(upload_to='image/%Y/%m',default='image/github.png',verbose_name='用户头像',max_length=200)


    class  Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name
    def  __str__(self):
        return   self.username
