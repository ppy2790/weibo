#coding=utf-8
import requests
from lxml import etree

url = 'http://weibo.cn/ppy2790' #此处请修改为微博地址
url_login = 'https://login.weibo.cn/login/'

html = requests.get(url_login).content
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
action = selector.xpath('//form[@method="post"]/@action')[0]
imgsrc = selector.xpath('/html/body/div[2]/form/div/img[1]/@src')[0]
index = imgsrc.find('cpt=')
capId = imgsrc[index + 4:]

print imgsrc

code = raw_input("plz input code:")


print action
print password
print vk

new_url = url_login + action
data = {
    'mobile' : 'ppy2790@***.com',#你的微博帐号
     password : '1234567**', #你的微博密码
    'remember' : 'on',
    'backURL' : 'http://weibo.cn/u/2508944032', #此处请填写微博地址
    'backTitle' : u'微博',
    'tryCount' : '',
    'vk' : vk,
    'capId':capId,
    'code':code,
    'submit' : u'登录'
    }

newhtml = requests.post(new_url,data=data).content
new_selector = etree.HTML(newhtml)


content = new_selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    print text