from  django  import  template

from  topic.models import Create_Topic

register=template.Library()



@register.simple_tag
def  all_theme(value):
    all_theme = len(Create_Topic.objects.all())
    return  all_theme
