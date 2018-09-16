from  django  import  template
from  topic.models import Create_Topic
from  user.models import User_Info


register=template.Library()


@register.simple_tag
def each_reply_num(username):
    info=User_Info.objects.get(username=username)
    reply=len(info.topic_comment_set.all())
    return  reply

