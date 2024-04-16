import matplotlib.pyplot as plt

# 数据
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
data_set_one = [75, 68, 82, 85, 90, 78, 83, 80]
data_set_two = [70, 65, 75, 78, 85, 70, 73, 75]

# 创建图形并设置标题
plt.plot(months, data_set_one, label='Data Set One', color='lightgreen', linewidth=2)
plt.fill_between(months, data_set_one, color='lightgreen', alpha=0.4)

plt.plot(months, data_set_two, label='Data Set Two', color='darkgreen', linewidth=2)
plt.fill_between(months, data_set_two, color='darkgreen', alpha=0.5)

# 添加标签和标题
plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Analyze 1')

# 显示图例
plt.legend()

# 设置x轴刻度旋转
plt.xticks(rotation=45)

# 存储图片
plt.savefig('img/picture1.png')

# 显示图形
plt.show()