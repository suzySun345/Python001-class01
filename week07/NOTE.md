#### 学习笔记

------

##### 类属性和对象属性

- python的对象和现实世界的对象

  python的对象：数字、字符串、元组、列表等

- 对象是一个数据以及相关行为的集合

- 古典类和新式类

  区别是python2.2版本以前类和基本数据类型分开，实现数据的基本功能很难做到统一，2.2版本以后类继承object类，与基本数据类型同源，实现基本功能变得流畅

- 类的两大成员：属性和方法

  - 属性分为类属性与对象属性
  - 类属性的特点是在内存中只保存一份，多个引用引用类属性时可以节省内存
  - 对象属性的特点是在每个对象都保存一份，在不同作用域或要存储多个数据时使用对象属性
  - self.name叫普通字段，实例化之后引用到对象
  - 类属性就是静态字段，不需要实例化
  - 使用__ dict __()方法可以查看类和对象的属性，返回的结果是字典。也可以使用dir()，返回的结果是列表
  - 如果是静态字段，使用实例.__ dict __()方法是没法查看到的，如果查看到了，那么这个字段其实已经是普通字段了

  ![image-20200809193211792](C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200809193211792.png)

  - 查看对象的方法：type(a)、a.__ class __()、id(a)
  - c = Human和c = Human()是不同的，一个是引用类，一个是引用类的对象
  - 增加静态字段：Human.nature=eat。setattr(类，属性名，value值)该方法不能给内置类型增加方法和属性
  - 属性名前面一个下划线是人为约定私有属性，例如：_fly。属性名前面两个下划线是私有属性，不可更改，例如：__ fly
  - __ xxx __()魔术方法，会随着系统环境变化
  - __ class __ .__ bases __ [0]. __ subclass __()

- 类方法

  - 普通方法或实例方法，参数里要有self

  - 语法糖，也叫装饰器，在原有的方法的上面加上一些特殊功能，用@符号标识，会使原有方法发生变化。

  - 类方法@classmethod，参数里有cls，表示该方法的类

  - 静态方法@staticmethod，无参数，由类调用，通常用于方法与类有关联，但不希望引用类的属性和方法。

    ![image-20200809200856719](C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200809200856719.png)

  - classmethod可以给实例调用，实例先查找实例的__ dict __()方法，如果没有就去查找所在的类是否有该方法

  - 类方法，一种是当需要操作类或返回类时，或者构造函数__ new __()单一无法满足多种复杂情况时，引入类方法。另一种就是在父类中定义类方法，子类根据自己的变量名称发生变化时，可以引用父类的类方法。

    ```
    class Fruit(object):
    	total = 0
    	def __ init __(self,fname,lname):
    		self.fname = fname
    		self.lname = lname
    	def print_name(self):
    		print(self.fname)
    		print(self.lname)
    	# 输入参数不完全是fname,lname这种形式的，比如fname-lname
    	@classmethod
    	def pre_name(cls,name):
    		fname,lname = name.split('-')
    		return cls(fname,lname)
    	@classmethod
    	def set(cls,value):
    		cls.total = value
    	@classmethod
    	def print_total(cls):
    		print(cls.total)
    class Apple(Fruit):
    	pass
    class Orange(Fruit):
    	pass
    
    Apple.set(100)
    Orange.set(200)
    org = Oranger()
    org.set(300)
    Apple.print_total
    	
    ms = Fruit.pre_name('ann-kind')
    ms.print_name()
    	# cls就是对象，当这个方法要操作类的时候，采用类方法
    
    
    		
    ```

    