# -*- coding:utf-8 -*-
# author:asus
# datetime:2020/6/5 21:48
# software: PyCharm


from bs4 import BeautifulSoup
import pdfplumber
from words_extract import keyword_extract

pdf_name = "3.pdf"

with pdfplumber.open(pdf_name) as pdf:  # 解析pdf文本
    for page in pdf.pages:
        page_txt = page.extract_text()
        # 获取文本，直接得到字符串，包括了换行符【与PDF上的换行位置一致，而不是实际的“段落”】
        # print(page_txt)

keyword, keywords = keyword_extract(page_txt)   # 获取关键词
print("关键词获取成功")
# print(keyword)
# print(keywords)

# 打开html文件
soup = BeautifulSoup(open("3.html", encoding='utf-8'))
# 返回所有tag列表

tag_list = soup.find_all('body')  # 获取body标签内容

all_context = str(tag_list[0])  # body标签内容转为string，并进行关键词标亮<mark>替换
all_context = all_context.replace(keyword, "<mark>" + keyword + "</mark>")
for word in keywords:
    all_context = all_context.replace(word, "<mark>" + word + "</mark>")
# all_context = all_context.replace('\n', '')
# print(all_context)
sp = BeautifulSoup(all_context)  # string转为bs4.element.Tag

soup.find('body').replace_with(sp)  # 修改后内容替换原body内容
print("替换成功")
with open('3test_output.html', 'w', encoding='utf-8') as fp:
    # 输出到新html文件
    fp.write(str(soup))
    print("输出成功")
