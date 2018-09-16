from  django  import template

register=template.Library()

from  topic.models import Create_Topic

@register.simple_tag
def theme_to_reply(value):

    info=Create_Topic.objects.get(title=value)
    reply=info.topic_comment_set.all()
    reply1=len(reply)
    return  reply1


