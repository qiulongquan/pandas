import pandas as pd

df = pd.read_csv("los_census.csv")
df.head()
# print(df)
print("="*60)
print(df.iloc[:3])
# 还可以选择特定的一行。
print(df.iloc[5])

print("="*60)
# df.iloc[] 的 [[行]，[列]] 里面可以同时接受行和列的位置，
# 如果你直接键入 df.iloc[1, 3, 5] 就会报错。
# 所以，很简单。如果你想要选择 1，3，5 行，可以这样做。
print(df.iloc[[1, 3, 5]])
# 如果想要显示1,3,5行，同时只显示0,1,2,3列的话,可以实现切片的功能
print(df.iloc[[1, 3, 5],[0,1,2,3]])

print("="*60)
import numpy as np  # 加载 numpy 模块
df = pd.DataFrame(np.random.randn(6,5),index=list('abcdef'),columns=list('ABCDE'))
# 选择 1，3 行和 C 后面的列：
print(df.loc[['a','c'], 'C':])
#           C         D         E
# # a  1.057609  0.687555 -1.587644
# # c -0.300336  0.459426  1.114225
