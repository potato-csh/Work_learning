import time
from Baidu_Text_transAPI import translation

with open('result/extract_wiki3.txt', 'r', encoding='utf-8') as f:
    word = f.read()

with open('result/wiki3.txt', 'w', encoding='utf-8') as fp:
    lines = word.split('===============================================')
    for line in lines:
        time.sleep(1)
        res = translation(query=line)
        print(res)

        try:
            detail_src = res['trans_result'][0]['src']
            detail_dst = res['trans_result'][0]['dst']
            child_src = res['trans_result'][1]['src']
            child_dst = res['trans_result'][1]['dst']
            parent_src = res['trans_result'][2]['src']
            parent_dst = res['trans_result'][2]['dst']
            result = detail_src + '\n' + detail_dst + '\n' +child_src + '\n' +child_dst + '\n' +parent_src + '\n'+parent_dst+'\n================================================\n'
            print(parent_dst)
            fp.write(result)


        except(KeyError, IndexError):
            print('' + '\n')
