# MusicDownloader

MusicDownloader 是基于python的一个音乐下载项目。

其主要功能有：

* 批量下载网易云音乐歌单
* 通过关键字搜索，搜索并下载特定的音乐

## 使用说明

1. 登陆自己的[网易云音乐账号](https://music.163.com/#/my/)。
2. 在当前界面进入开发者工具，进入**网络**选项卡，并重新加载界面。
3. 使用搜索工具，随意搜索你歌单中的一个关键字，定位到一个名字以`detail?csrf_token`开头的文件。
4. 选中该文件，在右侧`Headers`选项卡中拉到页末，找到`Form Data`，将其中的`params`与`encSecKey`复制到我们项目的`config.py`中。
5. 将`config.py`中的`FileSaveDir`改为你自己在本地想要保存的路径。
6. 运行`main.py`文件即可。

