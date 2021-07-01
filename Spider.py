import requests
import json
import re
from lxml import etree

URL = 'https://growjo.com/sitemap.xml'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


def get_link(URL):
    response = requests.get(URL)
    html_text = response.text
    url_list = re.findall(r'.*<loc>(.*)</loc>.*', html_text.strip())
    return url_list


def spider_detail(tree):
    title = tree.xpath('//div[@id="root"]//div[@class="card-header"]/h1/text()')
    title = ''.join(title)
    detail_list = []
    detail = tree.xpath('//div[@id="root"]//div[@class="company-badge"]//div[@style="display:flex"]')
    for d in detail:
        info = d.xpath('.//text()')
        info = ''.join(info).split(':')
        name = info[0]
        para = info[1]
        detail_dic = {
            name: para
        }
        detail_list.append(detail_dic)
    print(detail_list)

    tmp = {
        'title': title,
        'detail': detail_list
    }

    with open('info.json', 'w', encoding='utf-8') as fp:
        fp.write(json.dumps(tmp, indent=4))


if __name__ == '__main__':
    links = get_link(URL)

    for link in links:
        if link == 'https://growjo.com/sitemap-25.xml':
            urls = get_link(link)
            # test code
            urls = urls[:1]
            for url in urls:
                response = requests.get(url)
                html = response.text


                spider_detail(etree.HTML(html))

                break
            break

# //*[@id="root"]/div/div/main/div/div/div/div[2]/h1/text()[1]
