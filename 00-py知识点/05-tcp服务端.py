import socket
import time
import threading


def handle_client_action(ip_port, tcp_socket):
    print('连接地址和端口号为：', str(ip_port))
    while True:
        # 读取已连接客户端发送的消息
        try:
            recv_data = tcp_socket.recv(1024)
        except Exception:
            print('客户端连接断开了', ip_port)
            break
        print('客户端发来的内容：', recv_data.decode('utf-8'))
        if not recv_data:
            print('客户端下线了', ip_port)
            break
        # 获取结构化事件戳
        send_msg = time.strftime("%Y-%m-%d %X")
        msg = '[%s]:%s' % (send_msg, recv_data.decode('utf-8'))
        # 发送消息给已连接客户端
        tcp_socket.send(msg.encode('utf-8'))
    # 关闭客户端套接字
    tcp_socket.close()


# 1、创建tcp服务端套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定端口号
tcp_server_socket.bind(('', 9090))
# 3、设置监听最大连接数
tcp_server_socket.listen(5)
# 设置端口号复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

while True:
    print('服务端启动，监听客户端连接')
    # 3、等待连接
    tcp_client_socket, ip_port = tcp_server_socket.accept()

    sub_thread = threading.Thread(target=handle_client_action, args=(ip_port, tcp_client_socket))
    sub_thread.setDaemon(True)
    sub_thread.start()

# 关闭服务端套接字 此行代码可注销
tcp_server_socket.close()
