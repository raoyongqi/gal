from bs4 import BeautifulSoup

# 读取 p.svg 文件内容
with open('p.svg', 'r', encoding='utf-8') as file:
    p_svg_content = file.read()

# 解析 p.svg 文件
p_soup = BeautifulSoup(p_svg_content, 'xml')

# 查找 <g> 标签
legends_groups = p_soup.find_all('g', class_='legends', transform='translate(10, 60)')

# 提取第一个找到的 <g> 标签（假设只替换第一个）
if legends_groups:
    new_legends_group_tag = legends_groups[0]
else:
    raise ValueError("未找到符合条件的 <g> 标签。")

# 提取 <script> 标签内容
p_script_tag = p_soup.find('script', type='text/javascript')
p_script_content = str(p_script_tag) if p_script_tag else None

if not p_script_content:
    raise ValueError("p.svg 文件中没有找到 <script> 标签。")

# 读取 p2.svg 文件内容
with open('p2.svg', 'r', encoding='utf-8') as file:
    p2_svg_content = file.read()

# 解析 p2.svg 文件
p2_soup = BeautifulSoup(p2_svg_content, 'xml')

# 查找和替换旧的 <g> 标签
old_legends_groups = p2_soup.find_all('g', class_='legends', transform='translate(10, 60)')
for old_legends_group in old_legends_groups:
    old_legends_group.replace_with(new_legends_group_tag)

# 查找旧的 <script> 标签并替换内容
p2_script_tag = p2_soup.find('script', type='text/javascript')
if p2_script_tag:
    p2_script_tag.replace_with(BeautifulSoup(p_script_content, 'xml'))

# 保存更新后的 p2.svg 文件
with open('updated_p2.svg', 'w', encoding='utf-8') as file:
    file.write(str(p2_soup))

print("更新后的 p2.svg 文件已保存。")
