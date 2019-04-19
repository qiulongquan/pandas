import pandas as pd

# 从csv读取数据然后写入json文件
# pd.read_table("los_census.txt") #读取 txt 文件
df_los_census=pd.read_csv("los_census.csv",sep=',',header=0) #读取 csv 文件
df_los_census.to_json('1.json')

# 当然，你也可以通过 to_excel("1.xlsx") 储存为 Excel 默认支持的 .xlsx 格式。
# 只是，需要注意在线环境会报错。这时候需要再补充安装 openpyxl 包就好了：
# sudo pip install openpyxl

print(df_los_census.head()) # 默认显示前 5 条
print("="*60)
print(df_los_census.head(7)) # 显示前 7 条
print("="*60)
print(df_los_census.tail()) # 默认显示前 5 条
print("="*60)
print(df_los_census.tail(7)) # 显示前 7 条

print("="*60)
# describe() 相当于对数据集进行概览，会输出该数据集的计数、最大值、最小值等。
print(df_los_census.describe())
print("="*60)
# 例如上面，针对一个 DataFrame 会对每一列的数据单独统计。
# idxmin() 和 idxmax() 会计算最小、最大值对应的索引标签。
print(df_los_census.idxmin())
print(df_los_census.idxmax())
print("="*60)
# count() 用于统计非空数据的数量。
print(df_los_census.count())
print("="*60)
# value_counts() 仅仅针对 Series，它会计算每一个值对应的数量统计。
import numpy as np

s = pd.Series(np.random.randint(0, 9, size=100)) # 生成一个 Series，并在 0-9 之间生成 100 个随机值。

print(s)
print('------分割线------')
print(s.value_counts())

print("="*60)
# 排序
# 既然是数据处理，就少不了排序这一常用的操作。在 Pandas 中，
# 排序拥有很多「姿势」，下面就一起来看一看。
# 1. 按索引排序
# 首先是按照索引排序，其方法为Series.sort_index()或者是DataFrame.sort_index()。
df = pd.DataFrame(data={'one': [1, 2, 3], 'two': [4, 5, 6], 'three': [7, 8, 9], 'four': [10, 11, 12]}, index=['a', 'c', 'b'])
print(df)
#    four  one  three  two
# a    10    1      7    4
# c    11    2      8    5
# b    12    3      9    6
# 对索引进行排序
print(df.sort_index())
#    four  one  three  two
# a    10    1      7    4
# b    12    3      9    6
# c    11    2      8    5
# 或者添加参数，进行倒序排列：
print(df.sort_index(ascending=False))