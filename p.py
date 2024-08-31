import pygal
from pygal.style import Style

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

# 创建一个柱状图对象
bar_chart = pygal.Bar(style=custom_style, show_legend=True)
bar_chart.title = 'Fruits and Vegetables Count'

# 获取所有唯一的 Subcategory 和 Category
subcategory_set = sorted(set(data['Subcategory']))
categories = sorted(set(data['Category']))
# 初始化数据结构
category_data = {cat: {sub: [] for sub in subcategory_set} for cat in categories}

# 填充数据到相应类别
for cat, sub, count in zip(data['Category'], data['Subcategory'], data['Count']):
    category_data[cat][sub].append(count)

for category in categories:
    data_series = []
    for sub in subcategory_set:
        counts = category_data[category].get(sub, [0])
        # 如果多个计数则添加到数据列表中
        data_series.extend(counts)
    print(data_series)
    bar_chart.add(category, data_series)

# 设置 X 轴标签
bar_chart.x_labels = data['Subcategory']

# 保存为 SVG 文件
bar_chart.render_to_file('fruits_and_vegetables_count.svg')

# 如果在 Jupyter Notebook 中运行，可以使用以下代码显示：
# from IPython.display import display, SVG
# display(SVG(bar_chart.render(disable_xml_declaration=True)))
