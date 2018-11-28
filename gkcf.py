import requests
import json 
import re

h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept': 'application/json, text/javascript, */*; q=0.01','X-Requested-With': 'XMLHttpRequest','DNT': '1','Referer': 'http://www.ynzs.cn/2018gkcf/web.html','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Host': 'www.ynzs.cn','Content-Length':' 26'}

def get_html(user,pa,header):
    d = {'user':user,'pass':pa}
    h = header
    r = requests.post("http://www.ynzs.cn/2018gkcf/check.php?action=query", data=d,headers=h)
    rr=r.text.replace("\/","/")
    rrr=re.search('http.*html',rr)
    ru=requests.get(rrr.group())
    ru.encoding='utf-8'
    return ru.text

def parse_page(html):
    pattern = re.compile('<ul>.*?<li>考生姓名:<span>(.*?)\s+</span>.*?准考证号:<span>(\d+)</span>.*?文.*?class="bold">.*?(\d+)</em>.*?学.*?bold">.*?(\d+)</em>.*?外.*?语.*?bold">.*?(\d+).*?综合.*?bold">.*?(\d+).*?量化成绩.*?(\d+)</em>.*?总成绩.*?(\d+).*?次.*?(\d+)',re.S)
    items = re.findall(pattern,html)
    for i in items:
        for j in i:
            print (j, end = '\t')
    print('\r')
    return items

def write_file(items):
    with open('result.txt','a') as f:
        for i in items:
            f.write('\n')
            for j in i:
                f.write(j+'\t')
            f.close()
            
#将下面的262711000替换为学校起始准考证号
user = 262711000
#将下面的26271101替换为最后一个准考证号
while (user<=262711001):
    html=get_html(user,777777,h)#将前面的777777替换为为学生统一设置的查询密码
    w=parse_page(html)
    write_file(w)
    user = user+1 

#程序运行后会在当前目录生成一个result.txt文件，直接将文件内容复制到Excel中粘贴即可。
