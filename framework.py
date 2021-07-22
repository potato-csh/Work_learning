"""miniweb框架，负责处理动态资源请求"""
import time

route_list = []


def route(path):
    def decorator(func):
        # 当执行装饰器装饰指定函数的时候，把路径和函数添加到路由列表
        route_list.append((path, func))

        def inner():
            # 执行指定函数
            return func()

        return inner

    # 返回装饰器
    return decorator


# 获取首页数据
@route("/index.html")
def index():
    # 响应状态
    status = "200 OK"
    # 响应头
    response_header = [("Server", "PWS2.0")]
    # 处理后的数据
    data = time.ctime()
    return status, response_header, data


# 获取中心数据
@route("/center.html")
def center():
    # 响应状态
    status = "200 OK"
    # 响应头
    response_header = [("Server", "PWS2.0")]
    # 模板替换
    with open("static/index.html", 'r') as fp:
        file_data = fp.read()
    data = time.ctime()
    result = file_data.replace("{%content%}", data)
    return status, response_header, result


# 没有找到动态资源
def not_found():
    # 响应状态
    status = '404 Not Found'
    # 响应头
    response_header = [("Server", "PWS2.0")]
    # 处理后的数据
    data = time.ctime()
    return status, response_header, data


# 处理动态资源请求
def handle_request(env):
    # 获取动态请求的资源路径
    request_path = env["request_path"]
    print('接受到的动态资源请求：', request_path)
    route_list = {
        ('/index.html', index),
        ('/center.html', center)
    }
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
        else:
            result = not_found()
            return result
