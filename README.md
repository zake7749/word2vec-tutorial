# 使用 gensim 訓練中文詞向量

## [教學文件](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)

## 套件需求

* jieba
```
pip3 install jieba
```
* gensim
```
pip3 install -U gensim
```

## 訓練流程

1.取得[中文維基數據](https://dumps.wikimedia.org/zhwiki/20160820/zhwiki-20160820-pages-articles-multistream.xml.bz2)

2.使用`wiki_to_txt.py`從xml格式裡提取出文章

```
python3 wiki_to_txt.py zhwiki-20160820-pages-articles-multistream.xml.bz2
```
3.使用 opencc 統一將維基文本轉換為繁體中文
```
opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json
```
4.使用`jieba`對文本斷詞，並去除停用詞
```
python3 segment.py
```
5.使用`gensim`的word2vec模型，訓練語料庫
```
python3 train.py
```
6.測試模型
```
python3 demo.py
```
