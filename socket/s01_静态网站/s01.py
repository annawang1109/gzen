import socket
from pprint import pprint
####
#服务器端的本质
####
def f1():
    return b"f1"

def f2():
    return b"f2"

routers = [
    ("/xxxx", f1),
    ("/oooo", f2)
    
]


def run():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)


    while True:
        conn,addr = sock.accept()
        # 有人来链接，获取用户发送的数据
        data = conn.recv(8096)
        print(data)
        print(addr)
        headers, bodys = str(data, encoding="utf-8").split("\r\n\r\n")
        headers_items = headers.split("\r\n")
        method, url, protocal = headers_items[0].split(" ")
        print("请求方式是：",method)
        print("链接地址是：",url)
        print("协议是：", protocal)

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name()
        else:
            response = b"404"

        conn.send(response)
        conn.close()
if __name__ == '__main__':
    run()