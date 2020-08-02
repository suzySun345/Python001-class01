#### 学习笔记

------

### 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190823191349351.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1dhbmdUYW9UYW9f,size_16,color_FFFFFF,t_70)

**web框架的流程**

1.首先浏览器给Web服务器发送HTTP请求。

2.服务器接收到请求后解析请求，然后发送给Web后端框架。

3.后端框架接收到请求后进行处理（如封装js、数据库交互、业务处理等操作)。

4.处理结束后把HTTP的响应对象返回给服务器。

5.服务器把接收到的HTTP响应对象报文最后返回给浏览器。

6.最终浏览器得到想要的页面。

**MVT模式**

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019082319143163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1dhbmdUYW9UYW9f,size_16,color_FFFFFF,t_70)

**Django建立项目操作**

- **安装Django**

  pip install Django==2.2(最稳定的版本)

- **新建Django项目**

  \>>django-admin startproject MyDjango

  \>>python manage.py startapp index

- **启动Django应用程序**

  \>>python manage.py runserver

- **打开127.0.0.1:8000**

- **修改端口号**

  \>>python manage.py runserver 0.0.0.0:80