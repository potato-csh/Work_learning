# python 3.5
# 百度tesseract-ocr使用

from aip import AipOcr

""" API """
APP_ID = '24280810'
API_KEY = 'iL52WSgck6SDfGf1FIlrP04c'
SECRET_KEY = 'wwMfH3WKLr4tOknG1Wu5BW2SiIUdQp3s'

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def img_to_str(image_path):
    """ 可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"  # 中英文混合
    options["detect_direction"] = "true"  # 检测朝向
    options["detect_language"] = "true"  # 是否检测语言
    options["probability"] = "false"  # 是否返回识别结果中每一行的置信度

    image = get_file_content(image_path)

    """ 带参数调用通用文字识别 """
    result = client.basicGeneral(get_file_content(filePath), options)

    # 格式化输出-提取需要的部分
    if 'words_result' in result:
        text = ('\n'.join([w['words'] for w in result['words_result']]))
    print(type(result), "和", type(text))

    """ save """
    fs = open("result/baidu_ocr.txt", 'w+', encoding='utf-8')  # 将str,保存到txt
    fs.write(text)
    fs.close()
    return text


if __name__ == '__main__':
    filePath = 'file/code.jpg'
    print(img_to_str(filePath))
    print("识别完成。")
