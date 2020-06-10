# -*- coding:utf-8 -*-
# author:asus
# datetime:2020/6/3 21:28
# software: PyCharm

import re
from gensim.models import Word2Vec
import jieba.analyse
import numpy as np


def chinese(text):
    # 去除文本中中文之外的字符
    regex_str = ".*?([\u4E00-\u9FA5]+).*?"
    chinese_sentence = re.findall(regex_str, text)
    all_sentence = ''.join(chinese_sentence)
    return all_sentence


def keyword_extract(text):
    """
    抽取出关键词与关键词相似词
    :param text: pdf解析文本
    :return:
    """
    # 运用jieba_tfidf找到关键词
    all_sentence = chinese(text)
    keywords = jieba.analyse.extract_tags(all_sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    keyword = keywords[0][0]

    # 将文本分词，并保存到list中，list无重复词
    seg = jieba.lcut(all_sentence)
    all_words = []
    for word in seg:
        if word not in all_words:
            all_words.append(word)

    # 计算文本除关键词之外的词与关键词的相似度
    all_words.remove(keyword)
    model = Word2Vec.load("wiki.model")
    similarities = []
    for word in all_words:
        if word in model:
            similarity = model.similarity(word, keyword)
            similarities.append(similarity)

    # 提取出相似度排名前五的词语，保存到keywords_list中
    similarities = np.array(similarities)
    index = np.argsort(-similarities)
    keywords_list = []
    for i in range(5):
        keywords_list.append(seg[index[i]])

    return keyword, keywords_list


if __name__ == "__main__":
    sentence = "新华社北京3月9日电  3月9日，中共中央政治局常委、国务院总理、中央应对新冠肺炎疫情工作领导小组组长李克强主持召开领导小组" \
               "会议。中共中央政治局常委、中央应对新冠肺炎疫情工作领导小组副组长王沪宁出席。会议指出，要认真贯彻习近平总书记重要讲话" \
               "精神，按照中央应对疫情工作领导小组部署，继续把各项防控工作抓紧抓实抓细，进一步防范疫情跨境传播，落实有序复工复产的措施，" \
               "激励真抓实干，力戒形式主义、官僚主义，统筹推进疫情防控和经济社会发展。会议指出，当前国内疫情防控形势持续向好，特别是" \
               "武汉疫情快速上升态势得到控制，来之不易，但形势依然复杂。要继续拓展向好势头，抓好分区分级精准防控，坚决防止疫情反弹。" \
               "同时，面对境外新冠肺炎疫情快速扩散带来的新挑战，要加强国际合作，做好出入境防疫工作，这有利于有序安全的国际人员流动。" \
               "要推动关口前移，加强出入境相关信息共享，协调推动对来华人员在离境国进行健康检测，做好航空器清洁消毒、机组防护、健康申报、" \
               "体温检测、飞行途中防控等，采取分区分级分类输入风险管控措施。严格实施出入境人员口岸卫生检疫和防控工作，在严控疫情输出的" \
               "同时，对卫生检疫部门判定的确诊病例、疑似病例、密切接触者等入境人员，按规定落实检测、转运、治疗、隔离、留观等措施，并" \
               "加强人文关怀。与有关国家教育部门建立协调机制，暂缓或减少留学人员等双向流动。做好对我国在境外公民疫情防控的指导帮扶工作。" \
               "北京等出入境人员较多的口岸，要依法实施缜密的出入境防疫管理。出，新冠肺炎疫情发生以来，全国上下众志成城，全力奋战，" \
               "形成了抗击疫情的强大合力。各级干部特别是领导干部要按照统筹推进疫情防控和经济社会发展要求，以更扎实的作风主动担当作为，" \
               "对真抓实干、攻坚克难、甘于奉献的要给予激励，力戒形式主义、官僚主义，防止敷衍应付、推诿扯皮等行为，确保党中央、国务院" \
               "决策部署落地见效。要坚持实事求是，准确发布各类防控信息，及时回应社会关切，杜绝瞒报谎报、弄虚作假。加强部门间沟通协调，" \
               "集中精力解决疫情防控、有序复工复产、群众基本生活保障中的实际问题，开会和发文都要讲求实效。加强数据共享，防止重复填报。" \
               "完善检查、督查方式，深入基层了解实情，避免简单将台账记录、报表填报等作为工作落实的评判标准。防止简单粗暴执法和极端化" \
               "做法，提高依法防控、依法治理能力。领导小组成员丁薛祥、黄坤明、蔡奇、王毅、肖捷、赵克志参加会议。"
    keyword, keywords = keyword_extract(sentence)
    print(keyword)
    print(keywords)
