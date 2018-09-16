from  django  import  template

from  user.models import User_Info

from  topic.models import Create_Topic


register=template.Library()


@register.simple_tag
def each_people_num(username):
    info=User_Info.objects.get(username=username)
    all_theme=info.create_topic_set.all()
    all_theme1=len(all_theme)
    return  all_theme1




