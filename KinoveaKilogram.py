
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[1]:
#有几个数据：
markers = 3
#######################################################################
#读取数据，导出数据为表格后，通过复制成并列的数据，然后转换成txt文档。
#如果为txt文档


#方案1：
#for n in range(markers*2):
#    x[n],y[n] = np.readtxt("file.txt",delimiter=",",usecols=([n],[n+1]),unpack=true)
#	 n = n+2
#

#方案2：x,y,x1,y1,x2,y2,x3,y3 = np.readtxt("file.txt",delimiter=",",usecols=(1,2,3,4,5,6,7,8),unpack=true)
#

#方案3：
x = [1,3,5]
x1 = [7,9,11]
x2 = [13,15,17]
x3 = [19,21,23]
y = [2,4,6]
y1 = [8,10,12]
y2=[14,16,18]
y3=[20,22,24]
#########################################################################

#for i in range(markers):
#   x=[x[i],x1[i],x2[i],x3[i]] ######如果有多少个数据这里是需要修改数据个数
#   y=[y[i],y1[i],y2[i],y3[i]]
#   plt.plot(x,y)
#   plt.show()
 


#画图循环
for i in range(markers):
    x=[x[i],x1[i],x2[i],x3[i]]
    y=[y[i],y1[i],y2[i],y3[i]]
    plt.plot(x,y)
plt.show()

