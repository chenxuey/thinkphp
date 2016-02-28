#-*-conding:utf8-*-
import requests
from lxml import etree
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class RollSohu:
    def __init__(self,url,charset):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'}
        html = requests.get(url,headers)
        html.encoding = charset
        print html.text
        self.text = etree.HTML(html.text)

    def comtent(self,xpath):
        return self.text.xpath(xpath)


# url = 'http://roll.sohu.com'
# test = RollSohu(url,'GBK')
# content = dict()
#
# #href url
# href = '//*[@id="contentA"]/div[2]/div[3]/ul/li/a/@href'
# content['href'] = test.comtent(href)
# # title
# title = '//*[@id="contentA"]/div[2]/div[3]/ul/li/em/a/text()'
# content['title'] = test.comtent(title)
# # text
# text = '//*[@id="contentA"]/div[2]/div[3]/ul/li/a/text()'
# content['text'] = test.comtent(text)
# # time
# time = '//*[@id="contentA"]/div[2]/div[3]/ul/li/span/text()'
# content['time'] = test.comtent(time)
#
# # write into file
# fp = open('hongjun.text','a+')
# for i in range(len(content['text'])):
#     htmlText = '';
#     htmlText = content['title'][i]+','+content['text'][i]+','+content['time'][i].replace('(','').replace(')','')+','+content['href'][i]+'\r\n'
#     fp.write(htmlText)
# fp.close


url = 'http://news.163.com/latest'
test = RollSohu(url,'GBK')
content = dict()
#//*[@id="d_list"]/ul[1]/li[1]/span[1]/a
href1 = '//*[@id="instantPanel"]/div[1]/ul/li[1]/a/text()'
href = test.comtent(href1)
print href
# url2 = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&spec=&type=&date=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1&last_time=1452626265&r=0.1587367133237421'
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'}
# html = requests.get(url2,headers)
# html.encoding = 'GBK'
# print html.text