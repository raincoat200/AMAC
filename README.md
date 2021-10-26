
# 鸡金从业人员培训 浏览器点播脚本[辅助][原创]

各位鸡友好!
每到年底就遇到各类远程鬼畜培训,比如SAC和AMAC或者公司内部的培训任务.
本文脚本针对AMAC培训,可以实现

 1. **解除点播遇到的鼠标监听事件限制,支持页面最小化后台.**
 2. **每小节自动倒计时切换播.**
 

## 程序运行环境

废话不多说,直接看图文,大神请跳过脚本运行环境部署篇：
 1. **PYTHON 3** 
 [官方链接](https://www.python.org/downloads/release/python-3100/)  
 [传送门](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe) 
 [傻白甜安装教程](https://blog.csdn.net/qq_45502336/article/details/109531599)
 
 	**MARK重点步骤 1: 添加PATH环境变量**
![在这里插入图片描述](https://img-blog.csdnimg.cn/1b332aa9ee5d4671b9c4cedca560fb8d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_20,color_FFFFFF,t_70,g_se,x_16)	**MARK重点步骤 2:pip版本的更新**

```powershell
python -m pip install --upgrade pip
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/5fde6ef59ea049068fb9f5f952b75e7f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_20,color_FFFFFF,t_70,g_se,x_16)	**MARK重点步骤 3:爬虫库SELENIUM安装**

```python
pip install selenium
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/ab9ed890e8c2489c9abb8bab64fe42b2.png)



 3. FireFox 最新版 [传送门](https://download-ssl.firefox.com.cn/releases-sha2/stub/official/zh-CN/Firefox-latest.exe)；
 默认设置无脑安装即可
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/3de60d01fff74b5a82991035be6227b9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_17,color_FFFFFF,t_70,g_se,x_16)

 4. FireFox 对应geckodriver [国内镜像](http://npm.taobao.org/mirrors/geckodriver/)  93.0版本 [传送门](http://npm.taobao.org/mirrors/geckodriver/v0.30.0/geckodriver-v0.30.0-win32.zip)
[傻白甜安装教程](https://blog.csdn.net/hy_696/article/details/80114065)；
建议直接丢在C:\Windows 路径下

----

## PYTHON 主程序代码

```python
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
from time import sleep

def elem_play(var):
    var.click()
    sleep(3)
    browser.find_element_by_id("replaybtn").click()
    if browser.find_element_by_id("replaybtn").get_attribute("style").find("display: block")!=-1:
        browser.find_element_by_id("replaybtn").click()
    sleep(3)
    # time
    video = browser.find_element_by_class_name("CCH5playerContainer")
    ActionChains(browser).move_to_element(video).perform()
    time_text = browser.find_element_by_class_name("ccH5TimeTotal").text
    timenum = int(time_text.split(":")[0]) * 60 + int(time_text.split(":")[1])
    print(var.text, time_text, timenum, '秒')
    sleep(timenum + 3)
    try:
        browser.find_element_by_id("class_float").find_element_by_class_name("btn-close").click()
    except:
        pass

def go():
    # CURRENT ITEMS
    try:
        item = browser.find_element_by_xpath("//a[@class='article-li active cur']")
        elem_play(item)
    except:
        pass
    elems = browser.find_elements_by_class_name("art-wrap-li")
    for i in elems:
        i.text
    for i in elems:
        ActionChains(browser).move_to_element(i).perform()
        i.click()
        sleep(3)
        # LISTS
        item = i.find_element_by_xpath("//a[@class='article-li active']")
        elem_play(item)

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('https://peixun.amac.org.cn')
```
### 使用步骤

 **1. CMD**
 键盘同时按下<kbd>WIN</kbd> <kbd>R</kbd> 后,输入CMD
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/1201a6dcc3264af1b36217bcf882bc81.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_14,color_FFFFFF,t_70,g_se,x_16)

 **2. 运行 PYTHON** 
![在这里插入图片描述](https://img-blog.csdnimg.cn/443d654ef0f845abbc1918d01fdf4d7e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_20,color_FFFFFF,t_70,g_se,x_16)
 **3. 复制 运行 PYTHON 代码** 
 
记得敲回车键鸭~
![在这里插入图片描述](https://img-blog.csdnimg.cn/99b8eb45a3134286be335cce5d3d66b6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_20,color_FFFFFF,t_70,g_se,x_16)
**4. 登陆个人账户** 
	****
**5. 切换主页面,记得把新手首次提示点掉** 
	![在这里插入图片描述](https://img-blog.csdnimg.cn/6350164641cf4cc180b4d970deba7ee8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_9,color_FFFFFF,t_70,g_se,x_16)
**6. 运行启动命令
==CMD窗体内输入命令执行即可,务必小写,英文鸭~==
本课程完成,下一课程重新输入go()命令即可后台自动了.
网络慢情况下可以点击浏览器刷新按钮

```python
go()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/804a0e7431e944acb2334a99659de92e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcmFpbmNvYXQyMDA=,size_20,color_FFFFFF,t_70,g_se,x_16)


---
## 功德圆满,普惠众生













