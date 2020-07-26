#### 学习笔记

------

##### 学习内容

1. pandas的数据构造，Series和DataFrame
2. DataFrame的数据操作，包括增、删、改、查
3. DataFrame的数据选择，比较运算、行、列
4. DataFrame的表连接

##### 具体要点

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

