#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 演示client.py
# TIME: 2022/6/29 星期三  周三

# from socket import *
#
# phone = socket(AF_INET,SOCK_STREAM)
# phone.connect(('127.0.0.1',8080))
#
# while True:
#
#     msg  = input(">> ").strip()
#     phone.send(msg.encode('utf-8'))
#     print('client >>')
#     data = phone.recv(1024)
#     print(data)

# import socket
# ip_port = ('127.0.0.1',8080)
# BUffSIZE = 1024
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect_ex(ip_port)
#
# while True:
#     msg = input(">>: ").strip()
#     if len(msg) == 0 :continue
#     s.send(msg.encode('utf-8'))
#
#     feedback=s.recv(BUffSIZE)
#     print(feedback.decode('utf-8'))
#
# s.close()

# import socket
# ip_port = ('127.0.0.1',8080)
# BUFFSIZE = 1024
# udp_server_clinet = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# while True:
#     msg = input(">>: ").strip()
#     if not msg:continue
#
#     udp_server_clinet.sendto(msg.encode('utf-8'),ip_port)
#
#     back_msg,addr = udp_server_clinet.recvfrom(BUFFSIZE)
#     print(back_msg.decode('utf-8'),addr)