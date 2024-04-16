import matplotlib.pyplot as plt

# 数据
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
data_set_1 = [75, 68, 82, 85, 90, 78, 83]
data_set_2 = [70, 65, 75, 78, 85, 70, 73]

# 创建图形并设置标题
plt.bar(months, data_set_1, label='Data Set 1', color='green',alpha =0.4)
plt.bar(months, data_set_2, bottom=data_set_1, label='Data Set 2', color='gray',alpha = 0.4)

# 添加标签和标题
plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Analyze 2')

# 显示图例
plt.legend()

# 存储图片
plt.savefig('img/picture2.png')

# 显示图形
plt.show()