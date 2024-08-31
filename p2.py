import pygal
from pygal.style import Style
from collections import defaultdict

# 自定义颜色样式
custom_style = Style(
    colors=['#FF5733', '#33FF57'],  # 水果颜色：红色，蔬菜颜色：绿色
    label_font_size=14,
    major_label_font_size=18,
    title_font_size=20
)

# 数据
data = {
    'Category': ['水果', '水果', '蔬菜', '水果', '蔬菜', '水果'],
    'Subcategory': ['苹果', '香蕉', '生菜', '苹果', '生菜', '香蕉'],
    'Count': [10, 15, 25, 7, 5, 12]
}

bar_chart = pygal.Bar(style=custom_style)

# 设置图表的标题
bar_chart.title = 'Simple Bar Chart'

# 添加数据系列
bar_chart.add('COMMMM', data['Count'])

# 设置 X 轴标签
bar_chart.x_labels =data['Subcategory']
# 渲染图表到文件

bar_chart.render_to_file('simple_bar_chart.svg')
