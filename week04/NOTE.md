#### 学习笔记

------

##### 相关文档

1. pandas 中文文档：
   https://www.pypandas.cn/

2. sklearn安装参考文档：
   https://pypi.org/project/sklearn-pandas/1.5.0/

3. sklearn学习文档：

   http://www.scikitlearn.com.cn/

4. Numpy 学习文档：
   https://numpy.org/doc/

5. matplotlib 学习文档：
   https://matplotlib.org/contents.html

##### Pandas简介

Pandas是一个强大的分析结构化数据的工具集；

它的使用基础是Numpy（提供高性能的矩阵运算）；

用于数据挖掘和数据分析，同时也提供数据清洗功能。

- DataFrame

  DataFrame是Pandas中的一个表格型的数据结构，含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔型等)，DataFrame即有行索引也有列索引，可以被看做是由Series组成的字典。

  - DataFrame的数据操作，包括增、删、改、查
  - DataFrame的数据选择，比较运算、行、列
  - DataFrame的表连接

- Series

  它是一种类似于一维数组的对象，是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成。仅由一组数据也可产生简单的Series对象

##### SKlearn的鸢尾花数据集

由Fisher在1936年整理，包含4个特征（Sepal.Length（花萼长度）、Sepal.Width（花萼宽度）、Petal.Length（花瓣长度）、Petal.Width（花瓣宽度）），特征值都为正浮点数，单位为厘米。目标值为鸢尾花的分类（Iris Setosa（山鸢尾）、Iris Versicolour（杂色鸢尾），Iris Virginica（维吉尼亚鸢尾））。

iris.data 包含了四个特征值，例如[5.1, 3.5, 1.4, 0.2]
iris.target为目标值
iris.feature_names，iris.target_names为特征名称

```
from sklearn import datasets
from sklearn.model_selection import train_test_split

#鸢尾花数据集
iris = datasets.load_iris()
x, y = iris.data, iris.target
print(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

#load_boston Boston房价
#load_digits 手写体分类
```

##### pandas安装和简单示例

```python
# 安装pandas
pip install pandas
# 导入pandas
import pandas as pd
# 数学计算
import numpy as np
# 可视化
import matplotlib as plt
df = pd.DataFrame(['p','q','r','s'])
print(df)
```

##### python动态拼接文件路径

我们可以通过__ file __ 属性查找该模块（或包）文件所在的具体存储位置

```
import my_package
print(my_package.__file__)
```

- os.path.realpath(__ file __)是获取当前文件的绝对路径

- os.path.dirname()去掉路径的文件名

- os.path.join()是连接两个或更多的路径名组件

  1.如果各组件名首字母不包含’/’，则函数会自动加上

  2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃

  3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾

  注意：从倒数第一个，以‘/’开头的参数开始拼接，之前的参数全部丢弃。参考下面的所有可能拼接情况

```python
import os

print os.path.join('111','222','333')  #111/222/333
print os.path.join('/111','222','333') #/111/222/333
print os.path.join('/111','/222','333') #/222/333

print os.path.join('/111','/222','/333') #/333

print os.path.join('111','222','/333') #/333
print os.path.join('111','/222','/333') #/333
print os.path.join('/111','/222','/333') #/333

print os.path.join('111/','222','333') #111/222/333
print os.path.join('111/','222/','333') #111/222/333
print os.path.join('111/','222/','333/') #111/222/333/

print os.path.join('111','222','333/') #111/222/333/
print os.path.join('111','222/','333/') #111/222/333/
print os.path.join('111/','222/','333/') #111/222/333/

print os.path.join('111','222','./333') #111/222/./333
```

```python
# 课程代码示例
# os.path.realpath(__file__)获取绝对路径
# os.path.dirname去掉脚本文件名
print(os.path.realpath(__file__))
pwd = os.path.dirname(os.path.realpath(__file__))
print(pwd)
# 连接path组件
book = os.path.join(pwd,'book_utf8.csv')
print(book)
```

**DataFrame**

DataFrame是一种表格型数据结构，它含有一组有序的列，每列可以是不同的值。DataFrame既有行索引，也有列索引。

```kotlin
data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame = pd.DataFrame(data)
```

DataFrame的行索引是index，列索引是columns，我们可以在创建DataFrame时指定索引的值：

```tsx
frame2 = pd.DataFrame(data,index=['one','two','three','four','five'],columns=['year','state','pop','debt'])
```

使用嵌套字典也可以创建DataFrame，此时外层字典的键作为列，内层键则作为索引:

```bash
pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = pd.DataFrame(pop)
```

**读取文件**
 读取文件生成DataFrame最常用的是read_csv,read_table方法。该方法中几个重要的参数如下所示：

| 参数           |                             描述                             |
| :------------- | :----------------------------------------------------------: |
| header         | 默认第一行为columns，如果指定header=None，则表明没有索引行，第一行就是数据 |
| index_col      | 默认作为索引的为第一列，可以设为index_col为-1，表明没有索引列 |
| nrows          |                        表明读取的行数                        |
| sep或delimiter |    分隔符，read_csv默认是逗号，而read_table默认是制表符\t    |
| encoding       |                           编码格式                           |

