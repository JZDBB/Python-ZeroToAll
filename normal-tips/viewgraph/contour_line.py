import numpy as np
import matplotlib.pyplot as plt

z_list = []
for y in range(3):
    for x in range(3):
        z = x**2+y
        z_list.append(z)    #获得z的数据
z = z_list
x = np.linspace(0,2,3)
y = np.linspace(0,2,3)
[X,Y] = np.meshgrid(x,y)   #生成X,Y画布，X,Y都是3*3
#因为z是一维，所以要变成3*3
z = np.mat(z)
z = np.array(z)
z.shape = (3,3)
#画图（建议一定要查看X,Y,z是不是一一对应了）
plt.figure(figsize=(10,6))
plt.contourf(x,y,z)
plt.contour(x,y,z)
plt.show()
