# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：360新闻标题获取器  
#   版本：0.5  
#   作者：闲云  
#   日期：2013-11-03  
#   语言：Python 2.7    
#   功能：将360新闻标题的内容打包txt存储到本地。  
#---------------------------------------  
   
import string  
import urllib2  
import re  
  
#----------- 处理页面上的各种标签 -----------  
class HTML_Tool:  
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片  
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")  
      
    # 用非 贪婪模式 匹配 任意<>标签  
    EndCharToNoneRex = re.compile("<.*?>")  
  
    # 用非 贪婪模式 匹配 任意<p>标签  
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  
  
    # 将一些html的符号实体转变为原始符号  
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]  
      
    def Replace_Char(self,x):  
        x = self.BgnCharToNoneRex.sub("",x)  
        x = self.BgnPartRex.sub("\n    ",x)  
        x = self.CharToNewLineRex.sub("\n",x)  
        x = self.CharToNextTabRex.sub("\t",x)  
        x = self.EndCharToNoneRex.sub("",x)  
  
        for t in self.replaceTab:    
            x = x.replace(t[0],t[1])    
        return x    
      
class xw_News:  
    # 申明相关的属性  
    def __init__(self,url):    
        self.myUrl = url  
        self.datas = []  
        self.myTool = HTML_Tool()  
        print u'已经启动360新闻爬虫，咔嚓咔嚓'  
    
    # 初始化加载页面并将其转码储存  
    def News(self):  
        # 读取页面的原始信息并将其从gbk转码  
        myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8")   
        # 获取最终的数据  
        self.save_data(self.myUrl)   
    # 用来存储楼主发布的内容  
    def save_data(self,url):  
        # 加载页面数据到数组中  
        self.get_data(url)  
        # 打开本地文件  
        f = open(('今日新闻头条.doc').decode('utf-8'),'w+')  
        f.writelines(self.datas)  
        f.close()  
        print u'爬虫报告：文件已下载到本地并打包成doc文件'  
        print u'请按任意键退出...'  
        raw_input();  
  
    # 获取页面源码并将其存储到数组中  
    def get_data(self,url):  
            myPage = urllib2.urlopen(url).read()  
            # 将myPage中的html代码处理并存储到datas里面  
            self.deal_data(myPage.decode('utf-8'))  
              
  
    # 将内容从页面代码中抠出来  
    def deal_data(self,myPage):  
        myItems = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>',myPage,re.S)
        for item in myItems:
            data = self.myTool.Replace_Char(item[1].replace("\n","").encode('utf-8'))
            self.datas.append(data+'\n')
            data = self.myTool.Replace_Char(item[0].replace("\n","").encode('utf-8'))
            self.datas.append(data+'\n')
              
  
  
  
#-------- 程序入口处 ------------------  
print u"""#--------------------------------------- 
#   程序：360新闻标题获取 
#   版本：0.5 
#   作者：闲云 
#   日期：2013-11-03 
#   语言：Python 2.7 
#   操作：获取360当日的新闻标题 
#   功能：将360新闻的内容打包doc存储到本地。 
#--------------------------------------- 
"""  
  

  
print u'360新闻获取'  
bdurl = 'http://sh.qihoo.com/index.html'
  
#调用  
mySpider = xw_News(bdurl)  
mySpider.News()  
