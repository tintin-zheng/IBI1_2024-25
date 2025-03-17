#import the matplotlib library
import matplotlib.pyplot as plt

#creat two lists to store the data from UK and China
uk_countries = [57.11, 3.13, 1.91, 5.45]
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
#sort the data in the lists
sorted_uk_countries = sorted(uk_countries)
sorted_china_provinces = sorted(china_provinces)
#print the sorted lists
print(f"The sorted list of uk_countries is {sorted_uk_countries}.")
print(f"The sorted list of china_provinces is {sorted_china_provinces}.")

#creat two pie charts displaying the distribution of population sizes separately in	UK countries	
#and Zhejiang-neighbouring provinces

#creat the pie chart for the UK countries
#assign the figure number
plt.figure(1)
#set the labels for the pie chart
labels = ["England", "Wales", "Northern Ireland", "Scotland"]
#set the colors I LOVE for the pie chart
colors = ["#4DA4BA", "#85BBDA", "#1C60AC", "#5C7FAD"]
#creat the pie chart
plt.pie(uk_countries, labels = labels, colors = colors, autopct = "%1.2f%%" )
#add the title to the pie chart
plt.title("Population size distribution in UK countries")

#creat the pie chart for the Zhejiang-neighbouring provinces
#assign the figure number
plt.figure(2)
#set the labels for the pie chart
labels = ["Zhengjiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]
#set the colors I LOVE for the pie chart
colors = ["#AD1414", "#FFA12C", "#FFFE93", "#D3632C", "#683024"]
#creat the pie chart
plt.pie(china_provinces, labels = labels, colors = colors, autopct = "%1.2f%%" )
#add the title to the pie chart
plt.title("Population size distribution in Zhejiang-neighbouring provinces")
#show the pie chart
plt.show()

#try another plot to display the data
#use Florence Nightingale Rose Diagram to display the data
#creat the Florence Nightingale Rose Diagram fro the UK countries
import matplotlib.pyplot as plt
import numpy as np

# 示例数据：12 个月份的数值
categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
values = [10, 15, 7, 8, 12, 9, 6, 14, 11, 13, 5, 8]

# 设置极坐标参数
N = len(categories)
theta = np.linspace(0, 2 * np.pi, N, endpoint=False)  # 中心角度
width = 2 * np.pi / N  # 每个扇区的宽度

# 旋转角度，使 0 度位于顶部（南丁格尔图的典型样式）
theta -= np.pi / 2

# 创建极坐标子图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# 绘制玫瑰图：用颜色映射表示数值
bars = ax.bar(theta, values, width=width, align='center', alpha=0.7,
              color=plt.cm.viridis(values / np.max(values)))  # 使用 viridis 颜色映射

# 隐藏半径刻度
ax.set_yticklabels([])
ax.set_xticks(theta)  # 设置类别标签的位置
ax.set_xticklabels(categories)

# 调整极坐标方向：使 0 角度在顶部，并顺时针方向增加
ax.set_theta_offset(np.pi / 2)  # 初始偏移
ax.set_theta_direction(-1)       # 顺时针方向

# 添加标题
plt.title('Nightingale Rose Chart', pad=20)

plt.show()