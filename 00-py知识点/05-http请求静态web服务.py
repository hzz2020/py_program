import socket
import threading
import sys


class HttpWebServer(object):
    def __init__(self, port):
        # 创建服务端套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口号
        server_socket.bind(('', port))
        # 设置监听
        server_socket.listen(128)
        # 端口复用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        self.server_socket = server_socket

    @staticmethod
    def handle_client_request(client_socket):
        # 接收数据
        recv_data = client_socket.recv(4096)
        # 数据判断
        if len(recv_data) == 0:
            client_socket.close()
            return
        # 对接收到的二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        print('收到了', recv_content)

        request_list = recv_content.split(' ', 2)
        request_path = request_list[1]
        print('路径为：', request_path)

        if request_path == '/':
            request_path = '/index.html'

        try:
            with open('resume' + request_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            with open('../resume/error.html', 'rb') as file:
                file_data = file.read()
            # 响应行
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            # 响应头
            response_head = 'Server: PWS/1.0\r\n'
            # 响应体
            response_body = file_data
            # 封装响应数据
            response = (response_line + response_head + '\r\n').encode('utf-8') + response_body
            # 发送数据
            client_socket.send(response)
        else:
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_head = 'Server: PWS/1.0\r\n'
            # 响应体
            response_body = file_data
            # 封装响应数据
            response = (response_line + response_head + '\r\n').encode('utf-8') + response_body
            # 发送数据
            client_socket.send(response)
        finally:
            # 关闭套接字
            client_socket.close()

    def start(self):
        # 等待客户端连接
        while True:
            client_socket, ip_port = self.server_socket.accept()

            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            sub_thread.setDaemon(True)
            sub_thread.start()


def main():
    print(sys.argv)
    params = sys.argv
    # 判断命令行参数是否等于2
    if len(params) != 2:
        print('执行命令如下：python3 xxx.py 9000')
        return
    # 判断第2个参数是否为数字组成
    if not params[1].isdigit():
        print('执行命令如下：python3 xxx.py 9000')
        return

    port = int(params[1])

    web_server = HttpWebServer(port)
    web_server.start()


if __name__ == '__main__':
    main()