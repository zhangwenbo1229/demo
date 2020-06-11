#  搜索引擎的设计与实现

这是我在大学四年的一个纪念，因为疫情的影响，一直呆在家里，只好在毕业论文上多下工夫。这个项目是我在网络上东拼西凑出来的。项目的结构很简单，一个网络爬虫使用的是==Scrapy==框架；一个web界面使用的是网上很流行的==flask==框架；==MySQL==数据库负责存储数据。实现的效果是一个表情包搜索引擎，如图所示<img src="https://gitee.com/zhangwenbo1229/image/raw/master/img/20200611093654.png" style="zoom:80%;" />

非常感谢[春江慕客](https://www.bobobk.com/471.html)的博客为我提供了主体思路，在博客上的基础上我添加了一个一部分代码，实现了分页效果，为搜索结果页面底部添加了一个页面条，可以分页跳转，如图所示<img src="https://gitee.com/zhangwenbo1229/image/raw/master/img/20200611093648.png" style="zoom: 67%;" />

我的项目使用的IDE是Pycharm，环境是 Python3.8.2，mysql版本是5.7.26需要安装

```
pip install scrapy
pip install flask
pip install pymysql
```

3个字段，自增id，图片地址，图片描述。

```mysql
create dataabse bqb;
use bqb;
DROP TABLE IF EXISTS `bqb_scrapy`;
CREATE TABLE `bqb_scrapy` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`image_url` varchar(100) NOT NULL,
`image_des` varchar(100) NOT NULL,
PRIMARY KEY (`id`),
KEY `image_url` (`image_url`)
) ENGINE=InnoDB AUTO_INCREMENT=187800 DEFAULT CHARSET=utf8mb4;
```

爬虫运行需要在*项目根目录*运行`scrapy crawl dotula`

最后效果是
<img src="https://gitee.com/zhangwenbo1229/image/raw/master/img/20200611093629.png" alt="爬虫运行效果图" style="zoom:80%;" />

在数据库中可以查看到
<img src="https://gitee.com/zhangwenbo1229/image/raw/master/img/20200611093638.png" alt="数据库结果" style="zoom:80%;" />

在pycharm中运行flask，可以在本地的5000端口，看到搜索界面
<img src="https://gitee.com/zhangwenbo1229/image/raw/master/img/20200611093612.png" alt="搜索界面图" style="zoom:80%;" />

输入关键词，得到结果
<img src="https://gitee.com/zhangwenbo1229/image/raw/master/img/20200611093622.png" alt="搜索结果图" style="zoom:80%;" />