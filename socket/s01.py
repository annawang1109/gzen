import socket

####
#服务器端的本质
####
sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(5)


while True:
    conn,addr = sock.accept()
    # 有人来链接，获取用户发送的数据
    data = conn.recv(8096)
    print(data)
    print(addr)

    data.decode(uni.split("\r\n\r\n")
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"123123<br>123123")
    conn.close()
