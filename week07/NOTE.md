#### 学习笔记

------

##### 类属性和对象属性

- python的对象和现实世界的对象

  python的对象：数字、字符串、元组、列表等

- 对象是一个数据以及相关行为的集合

- 古典类和新式类

  区别是python 2.2版本以前自定义类和基本数据类型分开，实现数据的基本功能很难做到统一，2.2版本以后类继承object类，与基本数据类型同源，实现基本功能变得流畅

- 类的两大成员：属性和方法

  - 属性分为类属性与对象属性
  - 类属性的特点是在内存中只保存一份，多个引用引用类属性时可以节省内存
  - 对象属性的特点是在每个对象都保存一份，在不同作用域或要存储多个数据时使用对象属性
  - self.name叫普通字段，实例化之后引用到对象
  - 类属性就是静态字段，不需要实例化
  - 使用__ dict __()方法可以查看类和对象的属性，返回的结果是字典。也可以使用dir()，返回的结果是列表
  - 如果是静态字段，使用实例__ dict __()方法是没法查看到的，如果查看到了，那么这个字段其实已经是普通字段了

  ![image-20200809193211792](C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200809193211792.png)

  - 查看对象的方法：type(a)、a.__ class __()、id(a)
  - c = Human和c = Human()是不同的，一个是引用类，一个是引用类的对象
  - 增加静态字段：Human.nature=eat。setattr(类，属性名，value值)该方法不能给内置类型增加方法和属性
  - 属性名前面一个下划线是人为约定私有属性，例如：_fly。属性名前面两个下划线是私有属性，不可更改，例如：__ fly
  - __ xxx __()魔术方法，会随着系统环境变化而变化
  - __ class __ .__ bases __ [0]. __ subclass __()

##### 类的方法

- 普通方法或实例方法，参数里要有self

- 语法糖，也叫装饰器，在原有的方法的上面加上一些特殊功能，用@符号标识，会使原有方法发生变化。

- 类方法@classmethod，参数里第一个为cls，表示该方法的类

- 静态方法@staticmethod，无参数，由类直接调用，不传入self和cls，所以不调用类属性和实例属性。通常用于方法与类有关联，但不希望引用类的属性和方法。一般用于做一些判断或类型转换。

  ![image-20200809200856719](C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200809200856719.png)

- classmethod可以给实例调用，实例先查找实例的__ dict __()是否有该方法，如果没有就去查找所在的类是否有该方法，当类中没有该方法时，会去查询父类中是否有该方法

- 类方法的使用场景：一种是当需要操作类或返回类时，或者构造函数__ new __()单一无法满足多种复杂情况时，引入类方法。另一种就是在父类中定义类方法，子类根据自己的变量名称发生变化时，可以引用父类的类方法。

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
  		print(Fruit.total)
  		print(id(cls.total))
  		print(id(Fruit.total))
  		
  # 第一种场景
  ms = Fruit.pre_name('ann-kind')
  ms.print_name()
  	# cls就是对象，当这个方法要操作类的时候，采用类方法
  # 第二种场景
  class Apple(Fruit):
  	pass
  class Orange(Fruit):
  	pass
  
  Apple.set(100)
  Orange.set(200)
  org = Oranger('s','ss')
  # org实例没有set方法,查询类方法，再查询父类方法
org.set(300)
  # cls=apple
  Apple.print_total()
  # cls=orange
  org.print_total()
  	
  ```
  
- @staticmethod一般用于额外逻辑的处理，这些逻辑与实例或类不相关。

##### 类的实例属性描述符

都可以对实例属性进行获取拦截

- __ getattribute __() 对所有属性访问都会调用到该方法

- __ getattr __() 适用于未定义的属性，当属性不在 dict()里的时候，getattr才会拦截

- 无论属性存在不存在，都会调用__ getattribute__()，这会对实例的性能有损耗

- 当__ getattr __ () 和 __ getattribute __ ()都存在时，执行调用的顺序是 getattribute > getattr > dict

  ```
  # 实例代码
  class Human:
  	def __init__(self,name):
  		self.name = name
  	def __getattr__(self,item):
  		print('__getattr__',item)
  		return 'Error,请求参数不正确'
  	def __getattribute__(self,item):
  		print('__getattribute__',item)
  		return super().__getattribute__(item)
  H2 = Human('ss')
  print(H2.name)
  print(H2.age)
  ```

##### 属性描述符

property 把方法封装成属性，使代码简洁，可读性、可维护性更强。更好的管理属性的访问，控制属性访问权限，提高数据安全性

- property本质不是函数，而是特殊的类
- 如果一个对象同时定义了__ get __ ()和 __ set __()方法，则成为数据描述符
- 如果只定义了其中一个，则成为非数据描述符

```
# 第一种写法
gender =  property(get_,set_,del_,'other property')
# 第二种写法
class Human(object):
	def __init__(self):
		self.__gender = None
	@property
	def gender(self):
		print(self._gender)
		
	@gender.setter
	def gender(self,value):
		self.__gender = value
	
	@gender.deleter
	def gender(self):
		del self._gender
h = Human()
h.gender2 = 'F'
del h.gender2
		
```

```
# property的python实现
class Property(object):
	def __init__(self,fget=None, fset=None, fdel=None, doc=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		if doc is None and fget is not None:
			doc = fget.__doc__
			self.__doc__ = doc
	def __get__(self, obj, objtype=None):
    	if obj is None:
    	
```

##### 新式类

当前类或者父类继承了object类，那么该类是新式类，否则是经典类

- object和type都属于type类，一切皆对象的缘由
- type类由type元类自身创建的。object类时由元类type创建
- object的父类为空，没有继承任何类
- type的父类为object类
- 创建的并不代表就是父类

##### 类的继承

- 单一继承

  python继承父类的实例属性需要使用super().__ init __()，python的父类默认是Object类

- 多重继承

  python支持多重继承，自然语言

- 菱形继承

  

- 继承机制MRO

- MRO的C3算法

##### 设计原则

- Single Responsibility Principle 单一职责原则

  应该有且只有一个原因引起类的改变，即一个类只负责一个职责。

  让类C负责两个不同的职责：职责P1，P2。当由于职责P1需求发生改变而需要修改类C时，有可能会导致原本运行正常的职责P2功能发生故障，这违背原则

- Open Closed Principle 开闭原则

  一个软件实体，如类、模块和函数应该对扩展开放，对修改关闭

- 里氏替换原则（Liskov Substitution Principle）

  所有引用基类的地方必须能透明地使用其子类的对象，子类完整地覆盖父类，使用对象调用时不需要区分子类和父类

- 接口隔离原则（Interface Segregation Principle）

  1、客户端不应该依赖它不需要的接口。
  2、类间的依赖关系应该建立在最小的接口上。

- 依赖倒置原则（Dependence Inversion Principle）

  1、上层模块不应该依赖底层模块，它们都应该依赖于抽象。
  2、抽象不应该依赖于细节，细节应该依赖于抽象。

- 迪米特法则（Law of Demeter）

  如果两个软件实体无须直接通信，那么就不应当发生直接的相互调用，可以通过第三方转发该调用。其目的是降低类之间的耦合度，提高模块的相对独立性。

##### 设计模式

- 单例模式

  单例模式（Singleton Pattern）最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。

  这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。

  - 1、单例类只能有一个实例。
  - 2、单例类必须自己创建自己的唯一实例。
  - 3、单例类必须给所有其他对象提供这一实例。

- 工厂模式

  https://baijiahao.baidu.com/s?id=1642981552691391423&wfr=spider&for=pc

  https://www.cnblogs.com/yssjun/p/11102162.html

  该模式用于封装和管理对象的创建，是一种创建型模式

  - 简单工厂模式

    根据类的标识，通过工厂对象就可以得到具体类的实例对象了。在工厂对象里面，类对象的实例化如下：

  - 工厂方法模式

    定义了一个创建对象的抽象方法，由子类决定要实例化的类，将对象的创建，抽取出来了

  - 抽象工厂模式

##### 元类

创建类的类，就是类的模板，用来控制如何创建类的，正如类是创建对象的模板一样。

元类的实例为类，类的实例是对象

创建方法：

1. class

   用来创建复杂一点的类

   元类必须继承自type

   ```
   # 元类必须继承自type
   class Delvalue(type):
       # 元类必须实现new方法
       def __new__(cls,name,bases,attrs):
           attrs['pop_value'] = pop_value
           return type.__new__(cls,name,bases,attrs)
   
   class DelDicValue(dict,metaclass=Delvalue):
       pass
   
   d = DelDicValue()
   d['a'] = 'A'
   d['b'] = 'B'
   d['c'] = 'C'
   d.pop_value('C')
   print(d)
   ```

2. type

   ```
   def hi():
   	print('Hi, welcome to meta class')
   # type的三个参数(类名，父类名，类的成员)
   Foo = type('Foo',(),{'say_hi':hi})
   # 这是一个类，没有实例化
   foo = Foo
   foo.say_hi()
   ```

##### 抽象基类(Abstract base class)

用来确保派生类实现了基类中的特定方法，被@abstractmethod装饰的方法必须在子类实现，否则会报错

- 避免继承错误，使类层次易于理解和维护
- 无法实例化基类
- 如果忘记在其中一个子类中实现接口方法，要尽早报错

```
from abc import ABCMeta,abstractmethod
class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
c = Concrete()
报错：TypeError: Can't instantiate abstract class Concrete with abstract methods bar
```

##### Mixin模式

在程序运行过程中，重新定义类的继承，即动态继承。

- 可以在不修改源代码的基础上，对已有类进行扩展
- 进行组件的划分