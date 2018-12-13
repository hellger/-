import requests
import re
from requests.exceptions import RequestException

#定义一个方法，用来获取学生成绩存放的url,并访问这个url，然后返回网页内容
def get_url(url,user,pa,header):
    try:
        d = {'user':user,'pass':pa}
        r = requests.post(url, data=d,headers=header)
        rr=r.text.replace("\/","/")
        rrr=re.search('http.*html',rr)
        ru=requests.get(rrr.group())
        ru.encoding='utf-8'
        return ru.text
    except RequestException:
        return None
#h定义一个方法，用来解析网页内容
def parse_page(html):
    pattern = re.compile('<ul>.*?<li>考生姓名:<span>(.*?)\s+</span>.*?准考证号:<span>(\d+)</span>.*?文.*?class="bold">.*?(\d+)</em>.*?学.*?bold">.*?(\d+)</em>.*?外.*?语.*?bold">.*?(\d+).*?综合.*?bold">.*?(\d+).*?量化成绩.*?(\d+)</em>.*?总成绩.*?(\d+)\+?(\d+)?\(?(....)?\)?.*?次.*?(\d+)',re.S)
    items = re.findall(pattern,html)
    for i in items:
        for j in i:
            print (j, end = '\t')
    print('\r')
    return items
#d定义一个方法，将学生成绩写入文件
def write_file(items):
    with open('result.txt','a') as f:
        for i in items:
            f.write('\n')
            for j in i:
                f.write(j+'\t')
            f.close()
            
#定义main方法，变量user表示开始的准考证号
def main():
    u = "http://www.ynzs.cn/2018gkcf/check.php?action=query"
    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept': 'application/json, text/javascript, */*; q=0.01','X-Requested-With': 'XMLHttpRequest','DNT': '1','Referer': 'http://www.ynzs.cn/2018gkcf/web.html','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Host': 'www.ynzs.cn'}
    user = 262751116
    while (user<=262751202):
        html=get_url(u,user,777777,h)
        w=parse_page(html)
        write_file(w)
        user = user+1 

if __name__=='__main__':
    main()

#程序运行后会在当前目录生成一个result.txt文件，直接将文件内容复制到Excel中粘贴即可。
