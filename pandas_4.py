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
