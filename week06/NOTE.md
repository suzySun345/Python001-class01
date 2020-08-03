#### 学习笔记

------

![img](https://img-blog.csdn.net/20151116170654881)

##### web框架的流程

------



1.通过浏览器给Web服务器发送一个站点请求也就是HTTP请求。

2.服务器接收到请求后解析请求：

- Django查找配置文件mysite/mysite/settings.py，查看ROOT_URLCONF为多少，如图所示：
  ![这里写图片描述](https://img-blog.csdn.net/20150724150136919)
  这里为’mysite.urls’，表示URLconf为mysite/urls.py这个文件
- 查看mysite/urls.py，依次匹配每个url模式，直到找到第一个匹配的模式停下，这个找不到，还回去项目设置里的APP里去匹配
- 若匹配不成功或者中途出现异常，则返回http 404信息错误视图
- 若匹配成功，如path(‘^hello/$’, ‘blog.views.hello’, name=’hello’)就导入调用相关视图，即blog/views.py里的hello方法，该方法接收HttpRequest参数，返回HttpResponse对象。urlpatterns函数有三个参数，一个正则表达式、一个视图字符串/函数以及一个可选的参数name，name必须保持唯一。

3.后端框架接收到请求后进行处理（如封装js、数据库交互、业务处理等操作)。

4.处理结束后把HTTP的响应对象返回给服务器。

5.服务器把接收到的HTTP响应对象报文最后返回给浏览器。

6.最终浏览器得到想要的页面。



##### MVT模式的流程

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019082319143163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1dhbmdUYW9UYW9f,size_16,color_FFFFFF,t_70)



##### Django建立项目操作

------



- 安装Django

  ```
  pip install Django==2.2(最稳定的版本)
  ```

- 新建Django项目

  ```
  >>django-admin startproject MyDjango
  >>python manage.py startapp index
  ```

- 启动Django应用程序

  ```
  >>python manage.py runserver
  ```

- 打开127.0.0.1:8000

- 可以自己设置端口号

  ```
  >>python manage.py runserver 0.0.0.0:8003
  ```



##### Django的知识点学习：

------

当 Django 项目有多个 app 的时候，把所有视图函数都放到项目文件夹的 urls.py 来管理将会是一件比较烦杂的事情，我们可以在各自 app 的文件夹中创建 urls.py  文件来管理该 app 下的 url 和 视图函数的映射关系。

<img src="C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200803081729979.png" alt="image-20200803081729979" style="zoom: 67%;" />

**include使用方法**

用法：如果需要在当前urls中调用其他urls时比较好用

作用：用于urlpatterns中剔除掉path前面匹配到的部分，将剩下的部分交给include中的urls处理。

include函数的三种使用方式：

- include(module, namespace=None）
- include(pattern_list) #最常用
- include((pattern_list, app_namespace), namesapce=None)

module -- 表示一种模型文件

namespace -- 表示实例命名空间

pattern_list -- 必须是一个可迭代的path() 或者 re_path() 清单

app_namesapce -- app命名空间

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls'))
```

**Django url匹配方式**

- 带变量的url，通常有：str,int,uuid,slug,path

  ```
  from django.urls import path,include
  path('<int:year>', views.myyear) # 传入的参数赋值给变量year，如果变量值不是纯数字，默认返回404
  ```

- 正则表达式匹配

  需要导入re_path，re_path的作用与include的功能一样，特定的匹配

  ```
  from django.urls import re_path
  re_path('(?P<year>[0-9]{4}).html',views.myyear,name = 'urlyear')
  ```

- 自定义匹配规则

  导入register_convert，建立converter.py文件并在文件里自定义converter类，自定义的规则必须包含三部分，一是过滤规则，二是to_python()函数，三是to_url()函数

  urls.py文件

  ```
  from django.urls import path,re_path,register_converter
  from . import converter
  register_converter(converter.myconverter,'type_name')
  urlpatterns = [
  path('<type_name:value>','views.value')
  ] 
  ```

  converter.py

  ```
  class myconverter:
  	regex = '[0-9]+'
  	def to_python(self,value):
  		return int(value)
  	def to_url(self,value):
  		return str(value)
  ```

  

**render的作用**

render方法可接收三个参数，一是request参数，二是待渲染的html模板文件,三是保存具体数据的字典参数。

它的作用就是将数据填充进模板文件，最后把结果返回给浏览器，将response再做了一层封装

```
render(request,'xxx.html')
```

<img src="C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200803131246137.png" alt="image-20200803131246137" style="zoom: 67%;" />

返回错误码使用标准的Response

**Django快捷函数**

- render() 将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个HttpResponse对象

  将模板与view视图做绑定

  ```
  def myyear(request,year):
      return render(request,'yearview.html')
  ```

- redirect() 将一个HttpResponseRedirect返回到传递的参数的适当URL，一般用于用户名登录后的跳转

  ```
  def year(request,year):
      return redirect('/2020.html')
  ```

- get_object_or_404() 在给定的模型管理器上调用get()，但它会引发Http404而不是DoesNotExists异常

