# -*-coding: UTF-8 -*-

'''
视频对象
'''
#类定义
class VideoSearch:
    #定义基本属性
    name = ''
    photo = ''
    url = ''
    performer = ''
    #定义构造方法
    def __init__(self,name,photo,url,performer):
        self.name = name
        self.photo = photo
        self.url = url
        self.performer = performer
