from  django  import  forms

from  captcha.fields import CaptchaField


class  Login(forms.Form):
    username=forms.CharField(label='账号',required=True,max_length=150,widget=forms.TextInput(attrs={"class":"form-control","id":"id_login","placeholder":"请输入账号"}))
    password=forms.CharField(label='密码',required=True,min_length=5,widget=forms.PasswordInput(attrs={"class":"form-control","id":"id_password","name":"password","placeholder":"请输入密码"}))

class   Register(forms.Form):
    username=forms.CharField(required=True,max_length=150,min_length=2,widget=forms.TextInput(attrs={"class":"form-control", "id":"id_username" ,"type":"text","placeholder":"请输入账号"}))
    password=forms.CharField(initial='请输入您的密码',required=True,max_length=20,min_length=6,widget=forms.PasswordInput(attrs={"class":"form-control", "id":"id_password1","placeholder":"请输入密码"}))
    password1=forms.CharField(initial='请再次输入您的密码',required=True,max_length=20,min_length=6,widget=forms.PasswordInput(attrs={"class":"form-control", "id":"id_password1","placeholder":"请确定密码"}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"请输入邮箱"}))
    mobile=forms.CharField(label='移动电话',required=False,max_length=11,min_length=10,widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"请输入您的移动手机号码"}))
    captcha=CaptchaField(error_messages={'message':'验证码输入错误'})
