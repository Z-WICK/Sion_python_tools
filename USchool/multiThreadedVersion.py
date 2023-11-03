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




