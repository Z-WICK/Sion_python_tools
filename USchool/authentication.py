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
    该脚本不考虑小白用户
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
