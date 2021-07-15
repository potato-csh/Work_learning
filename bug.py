import json
from time import sleep
from Baidu_Text_transAPI import translation

with open('result/jd.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('result/trans_jd.txt', 'w', encoding='utf-8') as fp:
    for line in lines:
        json_res = json.loads(line)
        raw_content = json_res['raw_content'].split('\\n')
        for raw in raw_content:
            sleep(1)
            word_dic = translation(raw)
            try:
                dst = word_dic['trans_result'][0]['dst']
                src = word_dic['trans_result'][0]['src']
                result = src + '\n' + dst + '\n'
                fp.write(result)
                print(result)
            except(KeyError, IndexError):
                pass

        try:
            reviewed_experience = json_res['reviewed_experience']
            print('reviewed_experience：', reviewed_experience)
            fp.write('\nreviewed_experience：')
            fp.write(str(reviewed_experience))
        except(KeyError, IndexError):
            pass

        try:
            job_title = json_res['job_title']
            print('job_title：', job_title)
            fp.write('\njob_title：')
            fp.write(job_title)
        except(KeyError, IndexError):
            pass

        try:
            reviewed_mandatory_skill = json_res['reviewed_mandatory_skill']
            print('reviewed_mandatory_skill：', reviewed_mandatory_skill)
            fp.write('\nreviewed_mandatory_skill：')
            fp.write(str(reviewed_mandatory_skill))
        except(KeyError, IndexError):
            pass

        try:
            reviewed_major = json_res['reviewed_major']
            print('reviewed_major：', reviewed_major)
            fp.write('\nreviewed_major：')
            fp.write(str(reviewed_major))
        except(KeyError, IndexError):
            pass

        try:
            reviewed_degree = json_res['reviewed_degree']
            print('reviewed_degree：', reviewed_degree)
            fp.write('\nreviewed_degree：')
            fp.write(str(reviewed_degree))
        except(KeyError, IndexError):
            pass

        fp.write('\n============================================================\n')
        print('\n============================================================\n')
