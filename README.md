# dayAndNightAndroidCustomServerPy
dayAndNight-android私有资源服务

- 这个仓库是https://github.com/1030907690/dayAndNight-android 的私服资源代码示例
- 这是Python Django例子目前只有3个简单接口search、homeRecommend、videoDetail
## 运行
- python manage.py runserver 0.0.0.0:8083 #0.0.0.0让其它电脑可连接到开发服务器，8000为端口号。如果不指定，那么端口号默认为8000
- python manage.py runserver 0.0.0.0:8083 1>/root/app/logs/log.log 2>&1 &  #这是后台运行输出日志文件到/root/app/logs/weixin.log