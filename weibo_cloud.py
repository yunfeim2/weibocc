# coding: utf-8

import json

import jieba.analyse
import matplotlib as mpl
# from scipy.misc import imread
import imageio
from wordcloud import WordCloud

# mpl.use('TkAgg')
import matplotlib.pyplot as plt


def keywords(mblogs):
    text = []
    for blog in mblogs:
        keyword = jieba.analyse.extract_tags(blog['text'])
        text.extend(keyword)
    return text


def gen_img(texts, img_file):
    data = ' '.join(text for text in texts)
    image_coloring = imageio.imread(img_file)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='STXINWEI.TTF',
        stopwords=['微博','视频','现在','不是','全文','白天','觉得',"链接","公司",'美股','TSLA','网页','汽车','比亚迪']
    )
    wc.generate(data)

    # plt.figure()
    # plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    wc.to_file(img_file.split('.')[0] + '_wc_比亚迪.png')


if __name__ == '__main__':
    keyword = '比亚迪'
    mblogs = json.loads(open('result_{}.json'.format(keyword), 'r', encoding='utf-8').read())
    print('微博总数：', len(mblogs))

    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))

    print("总词数：", len(words))

    gen_img(words, 'edge.png')
