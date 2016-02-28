#-*- coding:utf-8 -*-
from lxml import etree
import requests
html = '''
    <html>
        <head></head>
        <body>
        <div id='content'>
            <ul id='useful'>
                <li>第一条信息</li>
                <li>第2条信息</li>
                <li>第3条信息</li>
            </ul id='useless'>
            <ul>
                <li>第一水 木 条信息</li>
                <li>第2 is 条信息</li>
                <li>第3 is 条信息</li>

            </ul>

            <div id='url'>
                <a href="http://www.baidu.com">baidu</a>
                <a href="http://www.sina.com" title='xinlang'>sian</a>

            </div>
        </div>
        </body>
    </html>
'''
select = etree.HTML(html)

# content = select.xpath("//ul[@id='useful']/li/text()")
# for each in content:
#     print each

# content = select.xpath("//div[@id='url']/a/@href")
# for each in content:
#     print each
#
# content = select.xpath("//div[@id='url']/a/text()")
# for each in content:
#     print each
html1 = '''
    <html>
        <head></head>
        <body>
        <div id='content'>
        <div id='test-1'>This is one</div>
        <div id='test-2'>This is two</div>
        <div id='testfault'>This is three</div>
        </div>
        </body>
    </html>
'''

html2 = '''
    <html>
        <head></head>
        <body>
        <div id='content'>
        <div id='test-1'>one,
            <span>two</span>
            <font>three</font>
            four
            </div>
        </div>
        </body>
    </html>
'''

#//*[@id="cid:491,sid:20,t:link"]/span[@class="title"]/text()

select = etree.HTML(html1)
contents = select.xpath("//div[starts-with(@id,'test')]/text()")
for each in contents:
    print each
select = etree.HTML(html2)
contents = select.xpath("//div[@id='test-1']")[0]
info = contents.xpath('string(.)')
content_2 = info.replace('\n','').replace(' ','')
print content_2


html = requests.get('http://v.gaodun.com');
#print html.text
list = etree.HTML(html.text)
content = list.xpath('//div[starts-with(@id,"cid")]')
print content
for each in content:
    print each