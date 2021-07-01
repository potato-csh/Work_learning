# 提取字符


import time
import re
import xlwt
import time
from Baidu_Text_transAPI import translation

INDEX = 0
file = xlwt.Workbook(encoding = 'utf-8')
table = file.add_sheet('my sheet', cell_overwrite_ok=True)


# 处理父系
def handle_parent(parents):
    parents = parents.split(',', 1)[1].split(',')
    list_parents = []
    for p in parents:
        res = re.findall(r".*u'(.*)'.*", p)
        list_parents.append(res.pop())
    return list_parents


# 处理子系
def handle_son(sons):
    list_sons = []
    son = sons.split(',', 1)[1].split(',')
    for s in son:
        son = re.findall(r".*u'(.*)'.*", s)[0]
        list_sons.append(son)
    return list_sons


def write_excel(parents,sons):
    global INDEX
    # global INDEX
    for p in range(len(parents)):
        for s in range(len(sons)):
            print(sons[s], parents[p])
            table.write(INDEX, 0, parents[p])
            table.write(INDEX, 1, sons[s])
            INDEX += 1
    file.save('result/jd.xls')


with open('file/jd_results_suchas.txt', 'r', encoding='utf-8') as f:
    words = f.read()

with open('result/jd_suchas.txt', 'w', encoding='utf-8') as fp:
    with open('result/trans_jd.txt', 'w', encoding='utf-8') as ft:
        word = words.split('\n\n')
        for item in word:
            line = item.split('\n')
            if not line[0].startswith('--'):
                detail = line[-4]

                parent = line[-3]
                parents = handle_parent(parent)

                son = line[-2]
                sons = handle_son(son)

                # write_excel(parents,sons)

                time.sleep(1)
                res = translation(query=detail)


                try:
                    detail_src = res['trans_result'][0]['src']
                    detail_dst = res['trans_result'][0]['dst']
                #     child_src = res['trans_result'][1]['src']
                 #     child_dst = res['trans_result'][1]['dst']
                #     parent_src = res['trans_result'][2]['src']
                #     parent_dst = res['trans_result'][2]['dst']
                #     result = detail_src + '\n' + detail_dst + '\n' + child_src + '\n' + child_dst + '\n' + parent_src + '\n' + parent_dst + '\n================================================\n'
                #     print(parent_dst)
                #     fp.write(result)
                #     print(detail_src,'\n',detail_dst)
                #
                except(KeyError, IndexError):
                    print('' + '\n')


                print(detail_src + '\n'+ detail_dst + '\n' + '------------------------------ '+ '\n')
                ft.write(detail_src + '\n'+ detail_dst + '\n' + '------------------------------ '+ '\n')










