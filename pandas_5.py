# pandas百题测试 51-100

import pandas as pd
import numpy as np
# freq='D' freq='W' freq='M' freq='Y'  代表显示的级别  年 月 周 日
dti = pd.date_range(start='2018-01-01', end='2018-12-31', freq='D')
s = pd.Series(np.random.rand(len(dti)), index=dti)
print(s)
# 求出周三 weekday == 2时候的值的总和
print(s[s.index.weekday == 2].sum())
# 求出每个月对应的值的平均值
print(s.resample('M').mean())

# 以秒为单位取100个，从当前时间开始计算
s = pd.date_range('today', periods=100, freq='S')
print(s)
ts = pd.Series(np.random.randint(0, 500, len(s)), index=s)
print(ts)
ts1=ts.resample('Min').sum()
print(ts1)

s = pd.date_range('today', periods=1, freq='D')  # 获取当前时间
print(s)
# 设定当前时间为东京时间
ts_tko=s.tz_localize('Asia/Tokyo')
print(ts_tko)
# 显示上海的时间
print(ts_tko.tz_convert('Asia/Shanghai'))


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
# 查询age大于3的全部信息
print(df[df['age']>3])

print(df)

print(df[df.isnull().values==True])

# 行列索引切片
print(df.iloc[1:3,2:4])

# DataFrame 按关键字查询  在animal列里面值是dog和snake的对象
print(df[df['animal'].isin(['dog','snake'])])

# DataFrame 分组求和
print(df.groupby('animal').sum())

df = pd.DataFrame(np.random.random(size=(5, 6)), columns=list('abcdef'))
print(df)
print(df.sum().idxmax()) # idxmax(), idxmin() 为 Series 函数返回最大最小值的索引值

print('='*60)
# 算出每一行的平均值
print(df.mean(axis=1))
# axis=1 是行轴
# axis=0 是列轴
# 每一行的平均值和当前行的每个值进行减法操作，然后写入当前位置
print(df.sub(df.mean(axis=1),axis=0))

df = pd.DataFrame({'A': list('aaabbcaabcccbbc'),
                   'B': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
print(df)
# 根据A分组然后在根据B里面的值找到最大的3个值显示出来
print(df.groupby('A')['B'].nlargest(3))

# A
# a  1     345
#    7      52
#    0      12
# b  12     57
#    8      54
#    4      45
# c  10    235
#    14     87
#    9      23

# 根据A分组然后在根据B里面的值找到最大的3个值然后求和sum
print(df.groupby('A')['B'].nlargest(3).sum(level=0))

# A
# a    409
# b    156
# c    345


def square(x):  # 计算平方数
    return x ** 2
list_new=map(square, [1, 2, 3, 4, 5])
# map的返回值
# Python 2.x 返回列表。
# Python 3.x 返回迭代器。
for a in list_new:
    print(a,end=' ')
print("\n"+"="*50)
# 计算列表各个元素的平方
# [1, 4, 9, 16, 25]

# map的返回值
# Python 2.x 返回列表。
# Python 3.x 返回迭代器。
list_new=map(lambda x: x ** 2, [1, 2, 3, 4, 5])
for a in list_new:
    print(a,end=' ')
print("\n"+"="*50)
# 使用 lambda 匿名函数
# [1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
# map的返回值
# Python 2.x 返回列表。
# Python 3.x 返回迭代器。
list_new=map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
for a in list_new:
    print(a,end=' ')
print("\n"+"="*50)
# [3, 7, 11, 15, 19]


# 班级一部分同学的数学成绩表，如下图所示
# 但我们更加关心的是该同学是否及格，将该数学成绩按照是否>60来进行划分。
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Candy', 'Dany', 'Ella',
                            'Frank', 'Grace', 'Jenny'], 'grades': [58, 83, 79, 65, 93, 45, 61, 88]})


def choice(x):
    if x > 60:
        return 1
    else:
        return 0

df['grades'] = pd.Series(map(lambda x: choice(x), df['grades']))
print(df)


# 数据去重
# 一个列为A的 DataFrame 数据，如下图所示
# 尝试将 A 列中连续重复的数据清除。
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
new_df=df.loc[df['A'].shift() != df['A']]
# 通过arange生成等差数列，替换以前的index
new_df.index=[np.arange(0,7,1)]
print(new_df)

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# 5    6
# 6    7

from matplotlib import pyplot as plt
ts = pd.Series(np.random.randn(100), index=pd.date_range('today', periods=100))
ts = ts.cumsum()
fig = plt.figure() # 新建图形对象
fig.add_subplot()
plt.plot(ts,'r')
plt.show()


df = pd.DataFrame(np.random.randn(100, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
fig = plt.figure() # 新建图形对象
fig.add_subplot()
plt.plot(df,'r')
plt.show()



df = pd.DataFrame({"xs": [1, 5, 2, 8, 1], "ys": [4, 2, 1, 9, 6]})
df = df.cumsum()
df.plot.scatter("xs", "ys", color='red', marker="*")
fig = plt.figure() # 新建图形对象
fig.add_subplot()
plt.plot(df,'r')
plt.show()



df = pd.DataFrame({"revenue": [57, 68, 63, 71, 72, 90, 80, 62, 59, 51, 47, 52],
                   "advertising": [2.1, 1.9, 2.7, 3.0, 3.6, 3.2, 2.7, 2.4, 1.8, 1.6, 1.3, 1.9],
                   "month": range(12)
                   })

ax = df.plot.bar("month", "revenue", color="yellow")
df.plot("month", "advertising", secondary_y=True, ax=ax)
fig = plt.figure() # 新建图形对象
fig.add_subplot()
plt.plot(df,'r')
plt.show()