import pandas as pd
import numpy as np

# 字典 -> Series
# 数据值是 10, 20, 30，索引为 a, b, c 。我们可以直接通过 index= 参数来设置新的索引。
# pandas 会自动匹配人为设定的索引值和字典转换过来的索引值。而当索引无对应值时，会显示为 NaN 缺失值。
d = {'a' : 10, 'b' : 20, 'c' : 30}
s=pd.Series(d)
print(s)
print("="*60)
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)

print("="*60)
# ndarray -> Series
# ndarray 是著名数值计算包 numpy 中的多维数组。我们也可以将 ndarray 直接转换为 Series。
data = np.random.randn(5) # 一维随机数
index = ['a', 'b', 'c', 'd', 'e'] # 指定索引
s = pd.Series(data, index)
print(s)
# 上面的两个例子中，我们都指定了 index 的值。而当我们非人为指定索引值时，
# Pandas 会默认从 0 开始设置索引值。
s = pd.Series(data)
print(s)

print("="*60)
# 用来创建 Dataframe,它们分别是：
# from_csv()
# from_dict()
# from_items()
# from_records()
d = [('A', [1, 2, 3]), ('B', [4, 5, 6])]
c = ['one', 'two', 'three']
df = pd.DataFrame.from_items(d, orient='index', columns=c)
print(df)
print(df['one'])
print("删掉one列\n",df.pop('one'))
print("显示剩下的列\n",df)
# 添加列的方法未 df.insert(添加列位置索引序号, '添加列名', 数值)，例如：
df.insert(1, 'four', [10, 20])
print(df)