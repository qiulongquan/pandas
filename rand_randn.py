import numpy as np
import numpy

print("="*60)
# 生成[0,1)之间的浮点数
x=numpy.random.random(size=5)
print(x)

print("="*60)
# 返回随机整数，范围区间为[low,high），包含low，不包含high
# 参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，
# 默认的数据类型是np.int  .high没有填写时，默认生成随机数的范围是[0，low)
x=numpy.random.randint(1,10,size=5)
print(x)

print("="*60)
# np.random.seed()的作用：使得随机数据可预测。
# 当我们设置相同的seed，每次生成的随机数相同。
# 如果不设置seed，则每次会生成不同的随机数
np.random.seed(1000)
x=np.random.random(size=5)
print(x)

print("="*60)
# numpy.random.randn(d0,d1,…,dn)
# randn函数返回一个或一组样本，具有标准正态分布。
# dn表格每个维度
# 返回值为指定维度的array
x=numpy.random.randn(2,3)
print(x)

print("="*60)
# numpy.random.randn()与rand()的区别
# numpy中有一些常用的用来产生随机数的函数，randn()和rand()就属于这其中。
# numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。
# numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。
arr1 = np.random.randn(2,4)
print(arr1)
print("="*60)
arr2 = np.random.rand(2,4)
print(arr2)