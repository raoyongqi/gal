from bs4 import BeautifulSoup

# 读取 p.svg 文件内容
with open('p.svg', 'r', encoding='utf-8') as file:
    p_svg_content = file.read()

# 读取 p2.svg 文件内容
with open('p2.svg', 'r', encoding='utf-8') as file:
    p2_svg_content = file.read()

# 解析 p.svg 文件
p_soup = BeautifulSoup(p_svg_content, 'xml')

# 解析 p2.svg 文件
p2_soup = BeautifulSoup(p2_svg_content, 'xml')

# 查找所有 <g> 标签中 class 属性为 "legends" 和 transform 属性为 "translate(10, 60)"
legends_groups = p_soup.find_all('g', class_='legends', transform='translate(10, 60)')

# 打印找到的 <g> 标签内容（可选）
for group in legends_groups:
    print("找到的 <g> 标签:")
    print(group.prettify())  # 使用 prettify() 方法使输出更易读

# 提取第一个找到的 <g> 标签（假设只替换第一个）
if legends_groups:
    new_legends_group_tag = legends_groups[0]
else:
    raise ValueError("未找到符合条件的 <g> 标签。")

# 查找旧的 <g> 标签（如果存在）在 p2.svg 中
old_legends_groups = p2_soup.find_all('g', class_='legends', transform='translate(10, 60)')

# 替换所有找到的旧 <g> 标签
for old_legends_group in old_legends_groups:
    old_legends_group.replace_with(new_legends_group_tag)

# 保存更新后的 p2.svg 文件
with open('updated_p2.svg', 'w', encoding='utf-8') as file:
    file.write(str(p2_soup))

print("更新后的 p2.svg 文件已保存。")
