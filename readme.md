# EarthLiveSharp
项目来自[Earth Live Sharp ](https://github.com/bitdust/EarthLiveSharp)
图片均来自向[日葵-8號即時網頁](http://himawari8.nict.go.jp/)

这是我用python写的脚本文件(~~需要修改文件路径~~),ubuntu下测试正常,直接运行`python wallpaper.py`

每十分钟更新一次照片,并自动设置为壁纸.可加入开机启动项.

ubuntu直接添加文件就可以，可以参考[这里](http://jingyan.baidu.com/article/7c6fb428632c3980642c90ce.html),  mac可以参考[这里](http://stackoverflow.com/questions/6442364/running-script-upon-login-mac)

照片本身较小,可以在壁纸设置中选择居中并把背景颜色改为黑色,效果如下.

##### ~~该脚本直接从官网获取照片, 会对官网造成流量压力,不建议传播.~~ 

####更新

使用[Cloudinary](https://cloudinary.com) CDN, 减少官网压力.

服务端图片更新有延时,客户端按需延时等待图片更新.

无需修改脚本中文件路径,可直使用.多谢[LathamZ](https://github.com/LathamZ),mac版本也都是由[LathamZ](https://github.com/LathamZ)更新.

使用mac版本时，请确保安装了PIL(Pillow)库。没有请执行这条命令：`sudo pip install pillow`
## 效果
![screenshot1](https://github.com/xyangk/EarthLiveSharp/blob/master/demo/demo.png)
