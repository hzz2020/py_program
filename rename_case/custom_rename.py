import os
import time


work_path = os.getcwd()


# 显示操作主菜单
def show_menu():
    print('当前操作目录：', work_path)
    # 选择操作
    while True:
        print('请选择如下功能：')
        print('1：添加文本')
        print('2：替换文本')
        print('3：指定格式')
        print('0：退出程序')
        option = input("请输入操作编号：")
        if option == '1':
            show_add_menu()
            break
        elif option == '2':
            show_replace_menu()
            break
        elif option == '3':
            show_custom_menu()
            break
        elif option == '0':
            # 退出程序 exit()
            break
        else:
            print('操作编号输入错误，请重新输入')


# 添加文本的子菜单
def show_add_menu():
    while True:
        print('#'*15+' 添加文本操作 '+'#'*15)
        print('请选择如下功能（扩展名不处理）：')
        print('1：名称之前')
        print('2：名称之后')
        print('0：返回上一步')
        option = input("请输入操作编号：")
        if option == '0':
            show_menu()
            break
        add_text = input("请输入添加的文本：")
        if option == '1':
            handle_add_text(True, add_text)
            break
        elif option == '2':
            handle_add_text(False, add_text)
            break
        else:
            print('操作编号输入错误，请重新输入')


# 添加文本处理
def handle_add_text(is_before, add_text):
    # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
    # os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
    sample_tree = os.walk(work_path)
    for dirname, subdirs, files in sample_tree:
        # dirname 为目录
        # subdirs 为子目录集合 List
        # files 为子文件集合 List
        for file_name in files:
            print('排序+', file_name)
            # 过滤隐藏文件和自己
            if file_name.startswith('.') or file_name == os.path.split(__file__)[-1]:
                continue
            # 添加文本在原名称之前
            if is_before:
                after_name = add_text + file_name
            else:  # 添加文本在原名称之后
                # 分离文件名字和后缀名，防止修改文件后缀
                names = os.path.splitext(file_name)
                after_name = names[0] + add_text + names[1]
            # 检查是不是已经存在after_name的文件
            if os.path.exists(work_path + '/' + after_name):
                print('文件已经存在，不支持覆盖改名')
                continue
            else:
                # 将当前工作目录修改为待修改文件夹的位置
                os.chdir(work_path)
                # 改名
                os.rename(file_name, after_name)
        # 只处理当前目录下的文件，其子目录的不处理
        break
    print('操作完成')
    # 继续操作
    show_menu()


# 替换文本的子菜单
def show_replace_menu():
    print('#' * 15 + ' 替换文本操作 ' + '#' * 15)
    print('查找文本为空将返回上一步')
    old_text = input("查找：")
    if len(old_text) == 0:
        show_menu()
    else:
        new_text = input("替换成：")
        handle_replace_text(old_text, new_text)


# 替换（删除）文本处理
def handle_replace_text(old_text, new_text):
    # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
    # os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
    sample_tree = os.walk(work_path)
    for dirname, subdirs, files in sample_tree:
        # dirname 为目录
        # subdirs 为子目录集合 List
        # files 为子文件集合 List
        for file_name in files:
            # 过滤隐藏文件和自己
            if file_name.startswith('.') or file_name == os.path.split(__file__)[-1]:
                continue
            # 分离文件名字和后缀名，防止修改文件后缀
            names = os.path.splitext(file_name)
            # 组装新的文件名after_name
            after_name = names[0].replace(old_text, new_text) + names[1]
            # 检查是不是已经存在after_name的文件
            if os.path.exists(work_path + '/' + after_name):
                print('文件已经存在，不支持覆盖改名')
                continue
            else:
                # 将当前工作目录修改为待修改文件夹的位置
                os.chdir(work_path)
                # 改名
                os.rename(file_name, after_name)
        # 只处理当前目录下的文件，其子目录的不处理
        break
    print('操作完成')
    # 继续操作
    show_menu()


# 指定格式菜单
def show_custom_menu():
    while True:
        print('#' * 15 + ' 指定格式操作 ' + '#' * 15)
        print('请选择如下功能（扩展名不处理）：')
        print('1：名称+索引（默认）')
        print('2：名称+计数')
        print('3：名称+日期')
        print('0：返回上一步')
        option = input("请输入操作编号：")
        if option == '0':
            show_menu()
            break
        if option != '2' and option != '3':
            option = '1'
        print('1：名称之前')
        print('2：名称之后（默认）')
        index_optn = input('选择位置：')
        if index_optn != '1':
            index_optn = '2'
        name_text = input('自定格式：')
        if option != '3':
            start_str = input('开始数字：')
            if not start_str.isdigit():
                start_str = '1'
        else:
            start_str = time.strftime("%Y-%m-%d %X")

        handle_custom_text(option, index_optn, name_text, start_str)
        break


# 指定格式处理
def handle_custom_text(option, index_optn, name_text, start_str):
    # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
    # os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
    sample_tree = os.walk(work_path)
    for dirname, subdirs, files in sample_tree:
        # dirname 为目录
        # subdirs 为子目录集合 List
        # files 为子文件集合 List
        for file_name in files:
            print('file_name = ', file_name)
            # 过滤隐藏文件和自己
            if file_name.startswith('.') or file_name == os.path.split(__file__)[-1]:
                continue
            # 分离文件名字和后缀名，防止修改文件后缀
            names = os.path.splitext(file_name)
            if len(name_text) == 0:
                name_text_after = names[0]
            else:
                name_text_after = name_text
            # 组装新的文件名after_name
            if option == '3':
                if index_optn == '1':
                    after_name = start_str + name_text_after + names[1]
                else:
                    after_name = name_text_after + start_str + names[1]
                time.sleep(1)
                start_str = time.strftime("%Y-%m-%d %X")
            else:
                if option == '2':
                    start_str_format = start_str.zfill(5)
                else:
                    start_str_format = start_str

                if index_optn == '1':
                    after_name = start_str_format + name_text_after + names[1]
                else:
                    after_name = name_text_after + start_str_format + names[1]
                start_str = str(int(start_str)+1)
            print('after_name = ', after_name)
            # 检查是不是已经存在after_name的文件
            if os.path.exists(work_path + '/' + after_name):
                print('文件已经存在，不支持覆盖改名')
                continue
            else:
                # 将当前工作目录修改为待修改文件夹的位置
                os.chdir(work_path)
                # 改名
                os.rename(file_name, after_name)
        # 只处理当前目录下的文件，其子目录的不处理
        break
    print('操作完成')
    # 继续操作
    show_menu()


# 程序入口
def start():
    # 确认需要编辑的工作目录
    print('#'*15 + ' 开始 ' + '#'*15)
    while True:
        yn = input('工作目录：' + os.getcwd() + ' y/n? ')
        if yn.upper() == 'Y':
            show_menu()
            break
        elif yn.upper() == 'N':
            global work_path
            print('工作目录如：', os.getcwd())
            work_path = input("请输入工作目录：")
            # 校验目录是否存在
            if os.path.exists(work_path):
                show_menu()
            else:
                print(work_path + '目录不存在')
            break
        else:
            print('输入错误，请重新输入')


# 运行入口
if __name__ == "__main__":
    start()
