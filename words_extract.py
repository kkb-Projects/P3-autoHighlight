"""
使用TF-IDF，进行关键词提取
"""
import jieba
# 结巴分词
def segment(file="pdf/output/1.txt"):
    word_list = []
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read().strip().replace('\n','').replace(' ', '')
    print(content)
    # 分词
    seg_list = jieba.cut(content, cut_all=True)
    result = ' '.join(seg_list) # result:str类型
    # print(type(result))
    word_list.append(result)
    print(word_list)
    return result


if __name__ == '__main__':
    segment()