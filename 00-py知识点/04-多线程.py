# 线程之间执行是无序的
# 主线程会等所有的子线程执行结束再结束
# 线程之间共享全局变量
# 线程之间共享全局变量数据出现错误问题

# 1、导入线程模块
import threading
import time

def sing():
    # 获取当前线程
    cur_thread = threading.current_thread()
    print(cur_thread)

    for i in range(3):
        print('唱歌中...')
        time.sleep(0.3)

# 带有参数的线程
def dance(name):
    # 获取当前线程
    cur_thread = threading.current_thread()
    print(cur_thread)

    print(name)

def task():
    for i in range(10):
        print(i)
        time.sleep(0.2)

g_list = list()

lock = threading.Lock()

def add_data():
    # 上锁
    lock.acquire()
    for i in range(10):
        g_list.append(i)
        time.sleep(0.2)
    print(g_list)
    # 解锁
    lock.release()

def read_data():
    # 上锁
    lock.acquire()

    print('fff'*20)
    print(g_list)
    # 解锁
    lock.release()


if __name__ == '__main__':
    cur_thread = threading.current_thread()
    print(cur_thread)

    # 2、创建子线程
    sing_thread = threading.Thread(target=sing)
    # 3、启动子线程执行对应的任务
    sing_thread.start()

    dance_thread1 = threading.Thread(target=dance, args=('拉丁舞',))
    dance_thread1.start()
    dance_thread2 = threading.Thread(target=dance, kwargs={'name': '爵士舞'})
    dance_thread2.start()

    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    # join()让当前线程（主线程）等待add子线程执行完成以后代码再继续执行
    # add_thread.join()

    read_thread.start()

    # # ---- 结论：主进程会等子进程执行完成后程序再退出
    # # ---- 主进程退出，子进程销毁 方法①②
    # # 创建子进程
    # task_thread = threading.Thread(target=task)
    # # ①把子进程设置为守护主进程，以后主进程退出子进程直接销毁
    # task_thread.setDaemon(True)
    # task_thread.start()
    # # 主进程延时0.5秒
    # time.sleep(0.5)
    # print('over')



