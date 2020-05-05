学习链接：https://www.bilibili.com/video/BV124411A7Ep/?p=4&t=987

##爬虫思路
1.确定抓取数据
2.创建scrpy 爬虫
3.使用response 对象，可以执行‘xpath’和‘css’语法来提取数据
4.提取的数据，是一个selector或者是selectorList对象。想要提取其中的字符串，需要执行getall 或者 get方法
5.数据解析回来，要传到pipline处理，返回的是str类型
6.item：建议在‘items.py’中定义好模型
7.pipeline：这是专门用来保存数据的，其中有三个方法是经常用到的。
    open_spider(self,spider)    :当爬虫被打开时执行
    process_item(self,item,spider)  :当爬虫有item传过来时被调用
    close_spider(self,spider)   :当爬虫关闭时调用
    要激活pipline，在setting.py中 设置 ITEM_PIPELINES