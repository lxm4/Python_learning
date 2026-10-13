"""
网络编程与多线程基础

1. 进程：CPU 分配资源的最小单位
   - 进程有自己独立的内存空间，进程间不共享全局变量
   - 代码、数据、堆栈等资源互不影响

2. 线程：CPU 调度资源的最小单位
   - 线程共享同一进程中的资源
   - 线程之间更容易通信，但也要注意资源竞争

3. 网络编程：让不同机器上的程序进行数据交换
   - 常见方式：TCP （字节流）/ UDP（数据报包）
   - Python 中常用 socket 模块

4. 多线程：让一个程序在同一时间内执行多个任务
   - 适合 I/O 相关任务
   - 线程创建方式：threading.Thread

"""
import socket
import threading
import time


# -------------------- 一、网络编程基础 --------------------
# 1. TCP 服务端示例
# TCP 是面向连接的协议，适合稳定传输数据，比如文件传输、聊天应用等

def tcp_server(host='127.0.0.1', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"TCP 服务端已启动：{host}:{port}")

    while True:
        conn, addr = server.accept()
        print(f"客户端连接：{addr}")
        data = conn.recv(1024)
        if data:
            print(f"收到消息：{data.decode('utf-8')}")
            conn.sendall("收到消息，服务端返回成功".encode('utf-8'))
        conn.close()


# 2. TCP 客户端示例
# 客户端向服务端发消息，并接收返回值

def tcp_client(host='127.0.0.1', port=9999, message='hello world'):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.sendall(message.encode('utf-8'))
    recv_data = client.recv(1024)
    print(f"服务端回复：{recv_data.decode('utf-8')}")
    client.close()


# 3. UDP 发送示例
# UDP 不需要建立连接，适合广播、实时性要求高的场景

def udp_sender(host='127.0.0.1', port=8888, message='hello udp'):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode('utf-8'), (host, port))
    print(f"UDP 消息已发送：{message}")
    udp_socket.close()


# 4. UDP 接收示例

def udp_receiver(host='127.0.0.1', port=8888):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))
    print(f"UDP 服务端已监听：{host}:{port}")

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"收到来自 {addr} 的消息：{data.decode('utf-8')}")


# -------------------- 二、多线程基础 --------------------
# Python 中创建线程常用 threading 模块

def task1():
    for i in range(5):
        print('任务1执行中...', i)
        time.sleep(0.5)


def task2():
    for i in range(5):
        print('任务2执行中...', i)
        time.sleep(0.5)


# 线程示例：同时执行两个任务

def thread_demo():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('两个线程都执行完毕')


# -------------------- 三、线程安全问题 --------------------
# 多个线程可能同时访问同一个变量，导致数据竞争
# 例如：共享列表、共享账户余额等

money = 0
lock = threading.Lock()


def add_money():
    global money
    for _ in range(100000):
        with lock:
            money += 1


def thread_safe_demo():
    global money
    money = 0

    t1 = threading.Thread(target=add_money)
    t2 = threading.Thread(target=add_money)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"最终 money = {money}")
    # 由于使用了锁，最终值会是 200000


# -------------------- 四、网络编程 + 多线程结合 --------------------
# 现实中的服务器通常会为每个客户端开启一个线程来处理请求

def handle_client(conn, addr):
    print(f"处理客户端：{addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"收到 {addr} 发送的数据：{data.decode('utf-8')}")
            conn.sendall(f"已收到：{data.decode('utf-8')}".encode('utf-8'))
    finally:
        conn.close()


def tcp_threaded_server(host='127.0.0.1', port=7777):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"多线程 TCP 服务端已启动：{host}:{port}")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.daemon = True
        client_thread.start()


# -------------------- 五、简单说明 --------------------
# 常用点总结：
# - socket：用于网络通信
# - TCP：稳定、可靠、面向连接
# - UDP：轻量、快速、不保证稳定
# - threading：用于多任务并发
# - Lock：用于保证线程安全
# - 在服务器开发中，常见方式是“接受连接 + 开线程处理客户端请求”


if __name__ == '__main__':
    # 注意：这些代码中的服务器会一直运行，通常不要在脚本入口处直接启动
    # 如果需要使用，请手动调用对应函数。
    print('网络编程与多线程基础示例已加载。')
    print('可调用：tcp_server()、tcp_client()、udp_sender()、udp_receiver()、thread_demo()、thread_safe_demo()')

    # 下面这几行仅用于测试，不建议直接打开时启动长连接服务
    # tcp_client('127.0.0.1', 9999, 'hello')
    # thread_demo()
    # thread_safe_demo()
