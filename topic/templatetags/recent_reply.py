from   django  import  template
from  topic.models import Create_Topic
register=template.Library()


@register.simple_tag
def  recent_reply(value):
    info=Create_Topic.objects.get(title=value)
    reply=info.topic_comment_set.all().order_by('-add_time')
    i="无"
    try:
        reply1=reply[0].user.username
        return  reply1
    except:
        return  i