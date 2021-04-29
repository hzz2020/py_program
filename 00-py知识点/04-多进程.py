# 进程之间执行是无序的
# 主进程会等待所有的子进程执行结束再结束
# 进程之间不共享全局变量



import multiprocessing
import time
import os

# 进程1
def dance():
    dance_process_id = os.getpid()
    print(f'dance进程号{dance_process_id}, {multiprocessing.current_process}')
    print(f'dance父进程号{os.getppid()}')

    for i in range(3):
        print('跳舞中...')
        time.sleep(0.3)
# 进程2
def sing():
    # 获取自己进程编号
    sing_process_id = os.getpid()
    print(f'sing进程号{sing_process_id}, {multiprocessing.current_process}')
    # 获取父进程编号
    print(f'sing父进程号{os.getppid()}')

    for i in range(3):
        print('唱歌中...')
        time.sleep(0.3)
        # 根据进程号来kill掉进程
        os.kill(sing_process_id, 9)

# 2、获取进程编号
main_process_id = os.getpid()

# 3、带参数的进程
def show_info(name, age):
    print('name：' + name + ' age：' + age)

# 4、进程之间不共享全局变量
g_list = list()  #  =>[]
# 加数据进程
def add_data():
    for i in range(3):
        g_list.append(i)
        time.sleep(0.2)
    print(g_list)
# 读数据进程
def read_data():
    print(g_list)


def task():
    for i in range(10):
        print(i)
        time.sleep(0.2)


# main
if __name__ == '__main__':
    # 主进程执行
    # dance()
    # sing()

    # 子进程执行
    # dance_process.start()
    # sing_process.start()

    # 创建子进程
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)
    dance_process.start()
    sing_process.start()
    # 带参数的进程
    sub_process1 = multiprocessing.Process(target=show_info, args=('llh', '23'))
    sub_process2 = multiprocessing.Process(target=show_info, kwargs={'name': '哈哈哈', 'age': '24'})
    sub_process3 = multiprocessing.Process(target=show_info, args=('打断点', ), kwargs={'age': '33'})

    sub_process1.start()
    sub_process2.start()
    sub_process3.start()

    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    # join()让当前进程（主进程）等待add子进程执行完成以后代码再继续执行
    add_process.join()

    read_process.start()

    # ---- 结论：主进程会等子进程执行完成后程序再退出
    # ---- 主进程退出，子进程销毁 方法①②
    # 创建子进程
    task_process = multiprocessing.Process(target=task)
    # ①把子进程设置为守护主进程，以后主进程退出子进程直接销毁
    task_process.daemon = True
    task_process.start()
    # 主进程延时0.5秒
    time.sleep(0.5)
    # ②退出主进程之前，先让子进程销毁(终结)
    task_process.terminate()
    print('over')