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
