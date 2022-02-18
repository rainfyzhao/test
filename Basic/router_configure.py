#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import paramiko
import time

ssh = paramiko.SSHClient() # 创建SSH Client
ssh.load_system_host_keys() # 加载系统SSH密钥
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 添加新的SSH密钥

# paramiko.util.log_to_file('ssh.log')
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#def router_configure(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):

def router_configure(ip, username, password, enable='', wait_time=2, verbose=True):
    # SSH连接
    ssh.connect(ip, username=username, password=password, port=22, timeout=10, compress=True,allow_agent=False, look_for_keys=False)
    command = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(3)  # 等待网络设备回应
    x =command.recv(4096).decode()  # 获取路由器返回的信息
    print(x)
    command.send('terminal length 0'.encode())  # 发送命令
    command.send(b'\n')  # 回车
    command.send('show run'.encode())
    command.send(b'\n')
    # command.send('end'.encode())  # 发送命令
    # command.send(b'\n')  # 回车
    # command.send('terminal length 0'.encode())  # 发送命令
    # command.send(b'\n')  # 回车
    # command.send('show version'.encode())  # 发送命令
    # command.send(b'\n')  # 回车
    time.sleep(5)
    y = command.recv(40960).decode()  # 获取路由器返回的信息
    print(y)

if __name__ == '__main__':
    # router_configure('192.168.19.254','netdxs','8MmQksKJiTz')
    router_configure('192.168.19.201', 'cisco', 'cisco123')
