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
