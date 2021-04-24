import socket

# 1. 创建socket（实现网络之间的通信，还可以实现进程间通信）
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定host和port端口
# 默认使用localhost，client，connect()，会无法连接服务端
server.bind(('127.0.0.1', 8011))

# 3. 监听
server.listen()

# 4. 等待接受客户端连接
print('服务器以启动，等待连接。。。')
client, address = server.accept() # 阻塞的方法
print('%s 已连接' % address[0])
msg = client.recv(4096)
print(msg.decode('utf-8'))


# 5.向客户端发送消息
client.send('你好，我是小AI同学，很高兴认识你!'.encode('utf-8'))

# 6.等待客户端发来消息
msg = client.recv(4096) # 阻塞方法
print(address, '说：', msg.decode())

client.close()
server.close()