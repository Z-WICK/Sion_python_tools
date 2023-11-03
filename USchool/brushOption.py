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
