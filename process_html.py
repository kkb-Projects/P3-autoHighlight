from bs4 import BeautifulSoup

# 打开html文件
soup = BeautifulSoup(open("pdf/test1.html"))

print(type(soup))

# 返回所有tag列表
print(soup.find_all('a'))

# 返回一个标签名为"a"的Tag
print(soup.find("a"))
