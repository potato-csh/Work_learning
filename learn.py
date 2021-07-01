import requests
from lxml import etree

URL = 'https://www.58.com/ershoufang/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

if __name__ == '__main__':

    page_text = requests.get(URL, HEADERS).text
    with open('58.html', 'w', encoding='utf-8') as f:
        f.write(page_text)

    tree = etree.HTML(page_text)
    res_list = tree.xpath('//div[@id="global"]/table/tr')
    for res in res_list:
        title = res .xpath('./td[2]/a/text()')[0]
        print(title)
