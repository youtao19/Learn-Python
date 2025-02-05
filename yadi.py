# for i in range(1,521):
#     print("%d雅迪is pig\t" % i,end="")
#     if i % 10 == 0:
#         print("\n")
import numpy as np
import matplotlib.pyplot as plt 

# 生成心形曲线
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# 创建图形
plt.figure(figsize=(6, 6))

# 显示文字
plt.text(0, 0, '爱雅迪公主', fontsize=24, color='red', ha='center', va='center')

# 去除坐标轴
plt.axis('off')

# 显示图形
plt.show()
