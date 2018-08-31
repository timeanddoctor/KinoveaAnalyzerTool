
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[1]:
#有几行数据或者需要取多少个片段：
rows = int(input("请输入采集数目"))
#######################################################################
#读取数据，导出数据为表格后，通过复制成并列的数据，然后转换成txt文档。
#如果为txt文档


#方案1：c=np.loadtxt('ag0613.csv', delimiter=',',skiprows=(1), usecols=(0,), unpack=True)
#for n in range(markers*2):
#    x[n],y[n] = np.loadtxt("pnas.txt",skiprows=(1),delimiter="	",usecols=([n],[(n+1)]),unpack=True)
#    n += 2


#方案2：这里用到多少数据
x, y, xa, ya, xb, yb, xc, yc = np.loadtxt("pnas.txt", skiprows=(1), delimiter="	", usecols=(0,1,2,3,4,5,6,7), unpack=True)
#

#方案3：测试用
#x = [1,3,5]
#x1 = [7,9,11]
#x2 = [13,15,17]
#x3 = [19,21,23]
#y = [2,4,6]
#y1 = [8,10,12]
#y2=[14,16,18]
#y3=[20,22,24]
#########################################################################

#for i in range(markers):
#   x=[x[i],x1[i],x2[i],x3[i]] ######如果有多少个数据这里是需要修改数据个数
#   y=[y[i],y1[i],y2[i],y3[i]]
#   plt.plot(x,y)
#   plt.show()

# 线 plt.plot(x, y, linewidth = '1', label = "test", color=' coral ', linestyle=':', marker='|')
plt.xlabel('Time')
plt.ylabel('Gain')
 
xcc = xc[:rows]
ycc = yc[:rows]
plt.plot(xcc,ycc,linewidth = "2",color='b',marker=">")

#画图循环
for i in range(rows):
    xx = [x[i],xa[i],xb[i],xc[i]]
    yy = [y[i],ya[i],yb[i],yc[i]]
    plt.plot(xx,yy,linewidth = "3",color='r',marker='o')
    plt.axis("equal")


plt.show()

