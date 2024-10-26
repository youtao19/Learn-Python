import matplotlib.pyplot as plt
import numpy as np

# 定义爱心函数
def heart_function(x, y):
    return ((x**2 + y**2 - 1)**3 - x**2 * y**3)

# 创建坐标网格
x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)

# 创建网格矩阵
X, Y = np.meshgrid(x, y)

# 计算爱心形状
Z = heart_function(X, Y)

# 绘制爱心
plt.contour(X, Y, Z, [0], colors='red')

# 设置标题
plt.title("爱心")

# 隐藏坐标轴
plt.axis('off')

# 显示图形
plt.show()
