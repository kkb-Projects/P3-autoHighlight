import tensorflow as tf
import matplotlib.pyplot as plt
import csv
import numpy as np
import os
import words_extract

from sklearn.feature_extraction.text import TfidfVectorizer


# 开始一个图session
sess = tf.Session()

# 定义批处理大小和特征向量长度
batch_size = 200
max_feature = 1000

corpus = [
            'This is the first document.',
            'This document is the second document.',
            'And this is the third one.',
            'Is this the first document?',
            ]
# 计算文本的tf-idf值
# tfidf = TfidfVectorizer(input=words_extract.segment(),
#                         max_features=max_feature)
# sparse_tfidf_texts = tfidf.fit_transform()
tfidf = TfidfVectorizer()
test_X = tfidf.fit_transform(corpus)
print(test_X.todense())
print(tfidf.get_feature_names())
print(test_X)

