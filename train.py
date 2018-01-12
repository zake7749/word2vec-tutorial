# -*- coding: utf-8 -*-

import logging

from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("wiki_seg.txt")
    model = word2vec.Word2Vec(sentences, size=250)

    #保存模型，供日後使用
    model.save("word2vec.model")

    #模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")

if __name__ == "__main__":
    main()
