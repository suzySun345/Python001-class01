#### 学习笔记

------

##### 学习内容

1. 使用第三方库requests访问目标网站发送请求并获取响应数据
2. 使用第三方库beautiful soup对Html进行parser，find_all抽取数据
3. 使用第三方库lxml对Html进行parser，xpath抽取数据
4. 使用第三方库pandas将数据进行文件保存
5. 使用for循环来进行翻页操作
6. Http协议、Html标签、浏览器发送的Http请求
7. Scrapy爬虫框架的结构解析，engine、piplines、items的具体功能
8. Selector中的xpath的定位方法

##### 学习思考

1. requests不能进行Html的parser吗？如果能，要怎样做？还有Html.parser是什么？
2. beautiful soup里的find元素方法的底层逻辑是？和lxml的xpath区别是什么，底层逻辑是否相同？
3. 为什么python自带的urllib2的响应数据需要decode？而requests不需要？urllib2的响应结果是HttpResponse对象，只能用read()读取内容，二进制编码必须要decode，而Requests的响应结果是Response对象，text返回的是str格式，不需要decode
4. xpath里的text()，若该元素没有文本内容会如何。貌似没有影响，仍需验证。
5. 推导式就是for循环的简写方式
6. 使用return在返回结果的同时会结束循环，yield不会
7. Null\None\空的区别
8. scrapy里request函数里的meta用来做什么的？
9. f''字符串里可以用表达式，表达式用{}括起来
10. 如果parser()里返回items列表，piplines该怎么提取，process_item()接收的是item对象
11. scrapy的setting里的user-agent设置不生效，在spider里custom_settings设置user-agent也不生效，必须要在Request.get()里设置headers

##### 学习总结

1. 学完后，我对爬虫的初步概念是，对目标网站或数据来源通过发送网络请求获取数据，然后抽取需要的数据并格式化。这个过程应该是分为三个环节：①访问目标数据源②从响应数据里过滤出自己需要的数据③格式化输出。然后依据这三个环节将方法对号入座，分别为Requests、beautiful soup或lxml、pandas

2. 对scrapy框架的逻辑的理解，访问目标Url使用 start_requests()，抽取数据使用parser()和item，格式化输出使用piplines。具体的内部机制仍需整理。

   