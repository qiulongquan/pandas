# pandas百题测试 1-50

import pandas as pd
import numpy as np
print(pd.__version__)

arr=[1,2,3,4,5]
a=pd.Series(arr)
print(a)

a=np.random.randn(5)
index=['a','b','c','d','e']
a=pd.Series(a,index=index)
print(a)

a={'a':1,'b':2,'c':3}
b=pd.Series(a)
print(b)
b.index=['A','B','C']
print(b)

bb=b.append(pd.Series([11,22,33]))
print(bb)

bb=bb.drop('A')
print(bb)

bb['B']=1234
print(bb)

print(bb[:3])

print(bb.median())

print(bb.sum())

print(bb.max())

print(bb.min())

# DataFrame
import datetime
start=(datetime.datetime.now()).strftime("%Y-%m-%d")
# 通过定义pd.date_range时间序列，开始时间start，数量是periods的6次。
dates=pd.date_range(start=start,periods=6)
num_arr=np.random.randn(6,4)
columns=['A','B','C','D']
aa=pd.DataFrame(num_arr,index=dates,columns=columns)
print(aa)


# DataFrame生成数据的时候是竖着一列数据，不是传统的横着一排数据
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
        }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
aa=pd.DataFrame(data,index=labels)
# 更换某一个列的列名，注意要把inplace设定为True
aa.rename(columns={'age':'AGE'},inplace=True)
print(aa)

print("="*50)
print(aa.dtypes)


print(aa.head(5))

print(aa.tail(3))

print(aa.index)

print(aa.columns)

print(aa.values)

print(aa.describe())

print("="*50)
# DataFrame 转置操作
print(aa)
print(aa.T)

print(aa.sort_index)

# 通过‘AGE’字段进行排序 默认是升序排序
print(aa.sort_values(by='AGE'))

print(aa[1:3])

print(aa['AGE'])

print(aa['AGE'].name)

print(aa['AGE'].values)

print(aa[['AGE','priority']])

print(aa[['AGE','priority']])

print(aa.iloc[1:3])

# 位置切片查询
print(aa.iloc[1:3,1:3])

bb=aa.copy()
print(bb)

# 判断 DataFrame 元素是否为空
# bb.isnull()  # 如果为空则返回为 True
print(bb.isnull())

# 添加列数据  先生成需要加入的列，然后指定index 最后加入到DataFrame对象中
num = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index=aa.index)
aa['No.'] = num  # 添加以 'No.' 为列名的新数据列
print(aa)

# 根据 DataFrame 的下标值进行更改。
aa.iat[1,0]=22
print(aa)

# 根据 DataFrame 的标签对数据进行修改
aa.loc['c','animal']='snake_qlq'
print(aa)

# 针对某一列'AGE'的数值进行求平均值
print(aa['AGE'].mean())

print(aa.mean())

# 对 DataFrame 中任意列做求和操作
print(aa['visits'].sum())


# 将字符串转化为小写字母
string = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca',
                    np.nan, 'CABA', 'dog', 'cat'])
print(string)
print(string.str.lower())

print(string.str.upper())

# 任何存在 NaN 的行都将被删除  整行删除
cc=aa.copy()
print(cc)
print(cc.dropna(how='any'))

# DataFrame 文件操作
# 47. CSV 文件写入
cc.to_csv('data_frame.csv')
print("write completed")

# 48. CSV 文件读取
df_new=pd.read_csv('data_frame.csv')
print(df_new)

# Excel 写入操作
aa.to_excel('df_new.xlsx',sheet_name='sheet1')
print("excel write completed")

# Excel 读取操作
df_new=pd.read_excel('df_new.xlsx','sheet1')
print(df_new)