#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 演示server.py
# TIME: 2022/6/29 星期三  周三


# from socket import *
# phone = socket(AF_INET,SOCK_STREAM)
# phone.bind(('127.0.0.1',8080))
# phone.listen(5)
#
#
#
# conn,addr = phone.accept()
#
# while True:
#
#     data = conn.recv(1024)
#     print("server > ")
#     print(data)
#     conn.send(data.upper())
# connect.close()
# phone.close()


# import socket
#
# ip_port = ('127.0.0.1',8080)
# BUFFSIZ = 1024
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(ip_port)  # 绑定IP信息
# s.listen(5)   # 监听
#
# while True:
#     conn,addr=s.accept()
#     print(f'接到来自{addr[0]}的电话')
#     while True:
#         msg = conn.recv(BUFFSIZ)
#         print(msg,type(msg))
#         conn.send(msg.upper())
#     conn.close()
# s.close()


# UDP
# import socket
# ip_port=('127.0.0.1',8080)
# BUFFSIZE=1024
# udp_server_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# udp_server_client.bind(ip_port)
#
# while True:
#     msg,addr = udp_server_client.recvfrom(BUFFSIZE)
#     print(msg,addr)
#     udp_server_client.sendto(msg.upper(),addr)
