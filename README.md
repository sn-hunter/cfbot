# qq机器人的安装使用说明

## qq机器人的安装

1.去go-cqhttp官网下载qq机器人

[Tags · Mrs4s/go-cqhttp (github.com)](https://github.com/Mrs4s/go-cqhttp/tags)

2.找到想要的版本，点击进入后下载系统可以使用的安装包（此文件说明时使用的V1.2.0）

3.以window为例，运行`.exe`文件，一路确定，会出现.bat文件

4.运行.bat文件，选择`0 http`通信就可以

5.修改配置文件`config.yml`，内容如下 **请务必将qq号改为自己的**

链接：https://pan.baidu.com/s/1Oz96-GQnxc_eEU6BMo8nlg?pwd=ldcf 
提取码：ldcf

6.再次运行`.bat`文件，会生成`device.json`

7.修改`json`文件，修改这一部分为 2`"protocol":2`  （这是将协议改为手表，是最好实现的一种办法）

## python代码的下载与使用

1.将python代码下载之后，运行`main.py`文件

2.根据报错，安装python的相关库

3.正常运行后关闭即可

## 运行过程

1.首先运行go-cqhttp机器人，即运行`.bat`文件，等待二维码扫码登陆

2.运行`main.py`，即可正常使用

# 开发说明

如果想要开发自动发送图片的功能，可以参考`method.py`文件

```python
def sendGroupyq(uid):
    requests.get(
        url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(uid, '文件名.后缀'))
```

#### 图片文件放到机器人文件中的/data/images文件中

