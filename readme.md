# [搜狗图片](http://pic.sogou.com/)爬虫 #

## 简介 ##

scrapy框架，存储到mongodb。

## 使用方法 ##

在settings.py中设置下列参数，然后运行爬虫。
```python
# 自定义变量
# 分类
CATEGORY = '美女'
# 标签
TAG = '全部'
# 开始页码(起始0)，每页15幅图片
START = 0
# 结束页码
END = 260
# mongodb
MONGO_URI = 'localhost'
MONGO_DATABASE = 'sogoupic'
```

## 简要分析 ##

搜狗图片主页：http://pic.sogou.com/

按F12打开web开发者工具 -> 进网络监视器，很容易发现采用Ajax，网址规律如下：

```
http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=美女&tag=女神&start=0&len=15
http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=美女&tag=女神&start=15&len=15
http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=美女&tag=女神&start=30&len=15
http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=美女&tag=女神&start=45&len=15
```

在response中，发现json数据，节选部分数据项保存。

e.g.
```json
{
    "title" : "清新萌妹子可爱迷人",
    "tags" : [ 
        "迷人", 
        "妹纸", 
        "可爱", 
        "小清新"
    ],
    "width" : 620,
    "height" : 930,
    "size" : 89441,
    "page_url" : "http://www.mm4493.com/meitu/46166_10.html",
    "ori_pic_url" : "http://www.mm4493.com/d/file/p/2016-01-04/2c4799934e8f33d80891cb7389e58e86.jpg",
    "pic_url" : "http://img03.sogoucdn.com/app/a/100520021/82e035a5ea76c4900afd54cf5c609eb3"
}
```
