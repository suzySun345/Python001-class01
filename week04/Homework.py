import  pandas as pd
import numpy as np

def data_show():
    
    df =  pd.DataFrame(None, index=range(5), columns=['id','name','age','order_id'])
    df['id'] = ['0019','1010','1050','0080','1099']
    df['name'] = ['ss','ee','qq','hi','ui']
    df['age'] = [14, 13, 15, 12, 17]
    df['order_id'] = [100,134,122,175,120]
    df2 = pd.DataFrame(None, index=range(5), columns=['id','name','age','salary'])
    df['id'] = ['0203','1010','1022','0080','1099']
    df['name'] = ['tt','ee','ww','hi','ui']
    df['age'] = [16, 13, 16, 12, 17]
    df['salary'] = np.random.randint(2000,size=5)
    print(df)
    # 1.SELECT * FROM data;
    print(df)
    # 2. SELECT * FROM data LIMIT 10;
    print(df.head(10))
    # 3. SELECT id FROM data;
    print(df['id'])
    # 4. SELECT COUNT(id) FROM data;
    print(df['id'].count())
    # 5. SELECT * FROM data WHERE id<1000 AND age>30;
    # print(df[(df['id']>1000) & (df['age']>30)])
    # 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
    print(df.groupby('id').agg({'order_id':'nunique'}))
    # 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    print(pd.merge(df,df2,on='id',how = 'inner'))
    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    print(pd.concat([df,df2]))
    # 9. DELETE FROM table1 WHERE id=10;
    print(df.drop(index=df[df['id']==10].index))
    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    print(df.drop(['age'],axis=1))

if __name__ == '__main__':
    data_show()