from  django  import   forms


class  PubTopic(forms.Form):
    title=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"textinput textInput form-control"}))

    theme = (
        ('生物知识', '生物知识'),
        ('生物信息', '生物信息'),
        ('生活交流', '生活交流'),
        ('生信编程', '生信编程'),
        ('计算机学习', '计算机学习'),
        ('django学习', 'django学习'),
        #('comments', '论坛公告'),
    )

    node=forms.ChoiceField(choices=theme,widget=forms.Select(attrs={"class":"select form-control"}))

    content_raw=forms.CharField(widget=forms.Textarea(attrs={"class":"pagedownwidget form-control wmd-input","cols":"40","rows":"10"}))




class  Comment_Forms(forms.Form):
    content_raw = forms.CharField(widget=forms.Textarea(attrs={"class": "pagedownwidget form-control wmd-input", "cols": "40", "rows": "10"}))

