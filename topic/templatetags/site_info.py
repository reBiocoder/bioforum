from  django  import template

from  user.models import User_Info
from  topic.models import Create_Topic
#对自定义标题进行注册
register=template.Library()


@register.simple_tag
def   site_info(vaule):
    all_people=len(User_Info.objects.all())
    return  all_people

