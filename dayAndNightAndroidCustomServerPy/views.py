# -*- coding: utf-8 -*-
from django.http import HttpResponse



import json


from .bean.VideoSearch import *
import re

'''
返回的数据结构就是这样
'''


#搜索 2019年12月9日15:29:40
def search(request):
    keyWord = request.GET.get('keyWord', None);
    videoSearchArray = []
    videoSearch = VideoSearch("南方车站的聚会[TS]","http://cn2.3days.cc/1575873305179637.jpeg","http://wolongzy.net/detail/299773.html","胡歌,桂纶镁,廖凡,万茜,奇道,黄觉,曾美慧孜,张奕聪,陈永忠,李志鹏,刘畅,常嘉豪,常嘉壮,陈子杰,邱文洋,汤青松,付小仙")
    videoSearchArray.append(videoSearch)
    json_str = json.dumps(videoSearchArray, default=lambda obj:obj.__dict__, sort_keys = True, indent = 0, ensure_ascii = False)
    json_str = re.sub(r'\s', ' ', str(json_str))
    print(json_str)
    return HttpResponse(json_str);

#首页推荐 2019年12月9日15:29:43
def homeRecommend(request):
    videoSearchArray = []
    videoSearch = VideoSearch("南方车站的聚会[TS]","http://cn2.3days.cc/1575873305179637.jpeg","http://wolongzy.net/detail/299773.html","胡歌,桂纶镁,廖凡,万茜,奇道,黄觉,曾美慧孜,张奕聪,陈永忠,李志鹏,刘畅,常嘉豪,常嘉壮,陈子杰,邱文洋,汤青松,付小仙")
    videoSearchArray.append(videoSearch)
    json_str = json.dumps(videoSearchArray, default=lambda obj:obj.__dict__, sort_keys = True, indent = 0, ensure_ascii = False)
    json_str = re.sub(r'\s', ' ', str(json_str))
    print(json_str)
    return HttpResponse(json_str);

#视频详情
def videoDetail(request):
    url = request.GET.get("url",None)
    # videoGroupList 视频播放节点分组
    json_str = '{"videoGroupList":[{"group":"wlm3u8","videoList":[{"name":"第1集","url":"http://cn6.7639616.com/hls/20191209/201eddfd3d1335f819edb977417f6784/1575872830/index.m3u8"}]}],"url":"http://wolongzy.net/detail/299773.html","performer":"胡歌","imageUrl":"http://cn2.3days.cc/1575873305179637.jpeg","name":"南方车站的聚会[TS]","plot":"南方车站的聚会"}'
    return HttpResponse(json_str);


if __name__ == '__main__':
    print()
    json_str = '{"videoGroupList":[{"group":"m3u8","videoList":[{"name":"第1集","url":"http://xxxx.m3u8"}]}],"url":"http://wolongzy.net/detail/299773.html","performer":"胡歌","imageUrl":"http://cn2.3days.cc/1575873305179637.jpeg","name":"南方车站的聚会[TS]","plot":"南方车站的聚会"}'
    print(json_str)
