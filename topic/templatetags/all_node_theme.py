from  django  import  template

register=template.Library()


@register.simple_tag
def  all_node_theme(value):
    reservedict1 = {
        '生物知识': '1',
        '生物信息': '2',
        '生活交流': '3',
        '生信编程': '4',
        '计算机学习': '5',
        'django学习': '6',
        '论坛公告': '7',
    }

    node_id=reservedict1[value]
    return  node_id