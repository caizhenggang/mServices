import socket

# 1.创建socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接服务器
socket.connect(('127.0.0.1',8011))
socket.send(b'connect')


# 3.接受数据
msg = socket.recv(4096) # 阻塞
print('Server: ', msg.decode('utf-8'))

# 4.向服务端发送数据
socket.send('你好，我想听张学友的歌！'.encode('utf-8'))

# 关闭
socket.close()