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
* [OpenCC](https://github.com/BYVoid/OpenCC) (可更換為任何繁簡轉換套件)

## 訓練流程

1.取得[中文維基數據](https://dumps.wikimedia.org/zhwiki/20160820/zhwiki-20160820-pages-articles.xml.bz2)，本次實驗是採用 2016/8/20 的資料。

*目前 8 月 20 號的備份已經被汰換掉囉，請前往[維基百科:資料庫下載](https://dumps.wikimedia.org/zhwiki/)按日期來挑選更新的訓練資料。( 請挑選以`pages-articles.xml.bz2`為結尾的檔案 )*

2.將下載後的維基數據置於與專案同個目錄，再使用`wiki_to_txt.py`從 xml 中提取出維基文章

```
python3 wiki_to_txt.py zhwiki-20160820-pages-articles.xml.bz2
```
*若您採用的不是 8 月 20 號的備份，請更換 `zhwiki-20160820-pages-articles.xml.bz2` 為您採用的備份的檔名。*

3.使用 OpenCC 將維基文章統一轉換為繁體中文
```
opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json
```
4.使用`jieba` 對文本斷詞，並去除停用詞
```
python3 segment.py
```
5.使用`gensim` 的 word2vec 模型進行訓練
```
python3 train.py
```
6.測試我們訓練出的模型
```
python3 demo.py
```
