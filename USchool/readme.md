# U校园自动化测试记录

## 程序入口

`multiThreadedVersion.py`

```python
import multiprocessing

import brushDuration
# 共享资源
shared_resource = multiprocessing.Value('i', 0)

# 创建一个锁
lock = multiprocessing.Lock()

# 创建多个进程来并行运行函数
processes = []
for _ in range(2):
    process = multiprocessing.Process(target=brushDuration.Start())
    processes.append(process)
    process.start()

# 等待所有进程完成
for process in processes:
    process.join()

print("共享资源的值:", shared_resource.value)
```

这里用于解决多账户问题 ,  但是作者暂时没有这个需求此处能用就行

## 认证模块

`authentication.py`

```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 定义一个简单的类
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def chooseAccount():
    account = int(input("选择执行账户:\n 1. Sion \n 2. *** \n 3. *** \n 4. ***\n 输入选项: "))

    '''
    这里不采用input的方式输入账户密码的方式 , 并且也没必要采用数据库
    所以我们直接在代码中写死
    '''

    # 此处修改账户密码
    if account == 1:
        # 创建类的实例
        create_object = Person("****", "****")
        return create_object

    if account == 2:
        # 创建类的实例
        create_object = Person("*****", "*****")
        return create_object

def clickIKonw(driver):
    # 点击我知道了
    Konw = driver.find_element(By.XPATH, f"/html/body/div[3]/div/section/div[2]/div[2]/span")
    Konw.click()

def login(Person):
    # 初始化浏览器对象
    driver = webdriver.Firefox()
    driver.get("https://sso.unipus.cn/sso/login?service=https%3A%2F%2Fu.unipus.cn%2Fuser%2Fcomm%2Flogin%3Fschool_id%3D")

    # 输入用户名字
    # 这里是通过xpath来获取元素对象 , 日后网页改版这里需要重新改
    username = driver.find_element(By.XPATH, "//*[@id='pw-form']/div[1]/input")
    username.send_keys(Person.username)  # 在这里修改自己的账号

    # 输入用户密码
    # 这里是通过xpath来获取元素对象 , 日后网页改版这里需要重新改
    username = driver.find_element(By.XPATH, "//*[@id='pw-form']/div[2]/input")
    username.send_keys(Person.password)  # 在这里修改自己的账号的密码

    # 点击 我已经阅读同意
    clickAgree = driver.find_element(By.XPATH, "//*[@id='agreement']/label/input")
    clickAgree.click()

    # 点击登录
    clickLogin = driver.find_element(By.XPATH, "//*[@id='login']")
    clickLogin.click()

    time.sleep(8)
    return driver

# 关闭检测页面
def closeTest(driver):
    # 测试关闭检测页面
    wait = WebDriverWait(driver, 10)  # 最多等待10秒
    skipDetection = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='layui-layer1']/div[3]/a")))
    skipDetection.click()  # 执行点击操作
    time.sleep(2)

    # 现在有两个标签页，可以使用window_handles来切换到新页面
    # 切换到新页面
    driver.switch_to.window(driver.window_handles[1])

    # 执行你的操作，操作完后需要关闭新页面

    # 关闭新页面
    driver.close()

    # 如果需要切回到原来的标签页，可以使用以下方式
    driver.switch_to.window(driver.window_handles[0])

# 跳过 是否必修提示
# /html/body/div[10]/div/div[1]/div/div/div[3]/div/button/div/div/span
def skipCompulsory(driver):
    # 设置 1000 比较稳定 属于比较暴力的写法又不是不能用(
    for i in range(1000):
        try:
            skipCompulsory = driver.find_element(By.XPATH,
                                                 f"/html/body/div[{i}]/div/div[1]/div/div/div[3]/div/button/div/div/span")
            skipCompulsory.click()
        except Exception as e:
            continue
```

在chooseAccount() 这个函数修改自己的账户密码 , 其他不需要管

## 跳转模块

`LearnFun.py`

```python
import random
import time
from selenium.webdriver.common.by import By

import authentication

# 选择书本 , 进入板块 如 视听说 、 综合教程 、 练习
def selectBookSection(driver):
    # 进入视听说板块 , 其他板块抓取xpath自己改
    enterTheAudiovisual = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/img")
    enterTheAudiovisual.click()

    time.sleep(5)

    # 进入学习教程
    audiovisualContent = driver.find_element(By.XPATH, "//*[@id='menuBox']/ul[1]/li[3]/div[2]/div/span[2]/a/span")
    audiovisualContent.click()
    time.sleep(5)

    # 点击我知道了
    print("--------------------------尝试点击 我知道了-------------------------")
    authentication.clickIKonw(driver)

    # 跳过必修
    authentication.skipCompulsory(driver)
    time.sleep(8)

'''
这个函数是点击 视听说 侧边学习栏 模块的 
比如 1-2 、 2-1 、 3-1
'''

def learn(driver):
    random_number = random.randint(0, 100)
    startLearn = driver.find_element(By.XPATH,
                                     f"//*[@id='sidemenu']/div/div[2]/ul[1]/div[{random_number}]/div/li/span[2]/a")
    startLearn.click()
    authentication.skipCompulsory(driver)

'''
//*[@id="sidemenu"]/div/div[2]/ul[1]/div[9]/div/li/span[2]
//*[@id="sidemenu"]/div/div[2]/ul[1]/div[9]/div/li/span[2]
//*[@id="sidemenu"]/div/div[2]/ul[1]/div[9]/div/li/span[2]
//*[@id="sidemenu"]/div/div[2]/ul[1]/div[11]/div/li/span[2]
//*[@id="sidemenu"]/div/div[2]/ul[1]/div[12]/div/li/span[2]

由此可知 , 侧边栏元素主要是按顺序变化 从1 - N 一直数下来的
'''

# 报活措施 , 当随机连接5次都没有命中 . 则启用这个函数 手动命中 , 保证不会触发到这个长时间不操作
# 可选择特定的模块进行刷题

# Uname 指 u1 u2等大模块
# SingleNum 指的是单元模块下的 小模块
def specificUnits(driver, Unum, SingleNum):
    startLearn = driver.find_element(By.XPATH,
                                     f"//*[@id='sidemenu']/div/div[2]/ul[{Unum}]/div[{SingleNum}]/div/li/span[2]/a")
    startLearn.click()
    authentication.skipCompulsory(driver)
```

## 测试方式模块

`brushOption.py`

```python
import time

import LearnFun
import authentication
import notice

# 每3分钟换一个模块 停留
def switchEvery_Minutes(driver):
    global usrUnum
    stayTime = int(input('输入停留时间: \n'))
    StopNum = int(input('请输入已解锁 最后一个模块的数字 如 解锁到U2 就 输入2 \n'))
    time.sleep(2)

    authentication.skipCompulsory(driver)
    # 默认从 U1 开始循环
    # 给用户提供选择
    try:
        usrUnum = int(input("输入选择特定的单元作为起点(默认从1开始): "))
        Unum = usrUnum - 1
    except ValueError as e:
        Unum = 0

    while Unum > -1:
        Unum += 1
        # Bark 发送通知
        try:
            notice.SendToBark(Unum)
        except Exception as e:
            print("发送失败 / 未配置Bark ")
            # 这种方式挺不优雅的 , 有空会改
        rangeNumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # for i in range(rangeNum):
        for i in rangeNumList:
            try:
                authentication.skipCompulsory(driver)
                time.sleep(stayTime)
                LearnFun.specificUnits(driver, Unum, i)
                print(f"-----------当前大模块 U{Unum}-------------")
                # 这里并不准确 , 有空再说
                print(f"-----------当前子模块 - {rangeNumList[i]}-------------")

                if Unum > StopNum:
                    print("-----------------所有模块已经完成----------")
                    if usrUnum is not None:
                        Unum = usrUnum
                    else:
                        # 重置Unum 重新开始循环
                        Unum = 1
                # if rangeNum > 15:
                #     print("------------重置子模块---------")
                #     rangeNum = 1

            except Exception as e:
                print("课程未解锁 / 必修认证未跳过")
                # 同时每次都要跳过 是否 必修模块
                # 如果必修跳过失败 , 则再尝试 3 * 1000 次
                for j in range(5):
                    time.sleep(2)
                    authentication.skipCompulsory(driver)
                continue
```

这里只提供了一种跳转单元的方式 ,  如想在题目中输入文字 、 点击选项请参考Selenium官方文档

## 整体业务逻辑模块

`brushDuration.py`

```python
import LearnFun
import brushOption
import authentication

def Start():
    # 选择完参数 , 将实例化的对象传入login
    usr = authentication.chooseAccount()

    # 执行登录操作
    driver = authentication.login(usr)

    # 关闭浏览器 检测页面
    authentication.closeTest(driver)

    # 选择书本 , 进入板块 如 视听说 、 综合教程 、 练习
    LearnFun.selectBookSection(driver)

    # 选取听力内容 循环听力 并且循环 点击选项

    # 模式选择
    optionNum = int(input("选择刷题模式:\n"
                          "1.每N分钟切换一个单元\n "
                          "2.不建议小白使用的功能 特定模块输入文字 / 播放听力 定制\n"))
    if optionNum == 1:
        brushOption.switchEvery_Minutes(driver)

    if optionNum == 2:
        print()
```

本来这里是程序入口 , 但是在面对多账户同时测试时候有点问题.我们决定将其分离出来

同时也方便coder观察整个程序运行的业务逻辑

## 通知模块(可选)

`notice.py`

```python
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
```

将URL改成自己的BarkUrl即可完成推送

该程序作者只参考selenium文档一小会 , 纯属折腾着玩

该脚本有个非常致命的问题就是通过xpath来指定元素 , 所以当U校园改版该程序会失效

时长够20小时之后 , 该脚本不再更新仅作记录

免责声明

1. 本程序（或网站）仅供学习和演示目的而提供，不得用于商业目的或其他非法用途。
2. 本程序的作者或维护者不对程序的使用造成的任何直接或间接损失或损害承担任何法律责任。
3. 本程序的作者或维护者不对程序的准确性、完整性或适用性提供任何明示或暗示的保证。
4. 使用本程序时，用户应遵守所有适用的法律和法规，包括但不限于知识产权法和隐私法。
5. 本程序的作者或维护者保留随时更改或终止程序的权利，而无需提前通知。
6. 本程序可能包含链接到第三方网站或资源的信息，但作者或维护者不对这些第三方内容的准确性或合法性负任何责任。
7. 使用本程序即表示您同意遵守本免责声明的条件。

请在使用本程序之前详细阅读并理解本免责声明。如果您不同意或不接受本免责声明的任何条款，请停止使用本程序。