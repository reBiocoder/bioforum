# bioforum
django2.0搭建的一个论坛。（django2.0 forum）
*******

**在学习django2.0的过程中，最大的一个问题就是学了之后没有任何能够实践的项目，能让自己来练练手，github上的大多数项目都是基于django1.1-django1.9之间的，这是学习django2.0的过程中，一个最痛苦的一件事。**

**本论坛基于django2.0，使用类视图的继承模式，基于django2.0内部的登录模块和一些内置的优秀功能，开发的一个论坛demo。**


*****
论坛的前端模板使用的是niji论坛的简约模板，niji也是GitHub上的一个开源项目。 但是他是作为一个app可以附加到其他功能上的，可以直接使用pip安装，但是很多配置并不容易设置好，而且是基于django1.×的版本。  所以我并未参照它的后端逻辑，仅仅前端使用了niji论坛的模板。niji论坛使用的是bootstrap的响应式框架，有时间可以自己看看。
# 使用方式：
1.在manage.py中，修改数据库，改为你自己的数据库信息；
2.在host中添加你自己的站点信息，
3.```pip  install  -r   requirement.txt```

4.python  manage.py  makemigrations
5.python  manage.py  migrate
6.pythton  manage.py  runserver
7.服务器的配置，我使用的是django2.0+python3+apache2.4+ubuntu，我的博客有相关文章：
[django2.0在服务器上的配置1](https://zhuanlan.zhihu.com/p/43016468)，
[django2.0在apache上的配置2](https://www.lovexu.xyz/2018/08/22/NO20/)

************
# 欢迎star，fork！
