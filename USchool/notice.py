import requests


# ios 用户专属 可将完成情况发送到Bark 监控刷新情况
def SendToBark(UserialNumber):
    # 指定目标URL
    url = f'https://api.day.app/***********/当前执行到--- U{UserialNumber}--模块?group=USchool'

    # 发起GET请求
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 请求成功，输出响应内容
        print(response.text)
    else:
        # 请求失败，输出错误信息
        print(f'Request failed with status code {response.status_code}')
        print("发送失败 / 未配置Bark ")

