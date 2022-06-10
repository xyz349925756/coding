#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 配置文件解析器.py
# TIME: 5月  星期二

# import configparser
#
# config=configparser.ConfigParser()
# config.read('rsyncd.ini')
# print(config)
# print(config['rsync'])
# print(config['rsync']['uid'])
# print(config.get('rsync','uid'))
#
# print(config.items('rsync'))
# print(config.items('backup'))
# config.add_section("hello")
# config['hello']['name']='bob'
#
# with open('rsyncd.ini','w',encoding='utf-8') as f:
#     config.write(f)
import hashlib

# text_md5=hashlib.md5()
# text_md5.update(bytes('hello',encoding='utf-8'))
# print("md5:",text_md5.hexdigest())
#
# text_sha1 = hashlib.sha1()
# text_sha1.update(bytes('hello',encoding='utf-8'))
# print('sha1:',text_sha1.hexdigest())
#
# text_sha3_256 = hashlib.sha3_256()
# text_sha3_256.update(bytes('hello',encoding='utf-8'))
# print('sha3_256:',text_sha1.hexdigest())
#
# text_blake2s = hashlib.blake2s()
# text_blake2s.update(bytes('hello',encoding='utf-8'))
# print('blake2s:',text_blake2s.hexdigest())

# text_md5=hashlib.md5(b'key')
# text_md5.update(bytes('hello',encoding='utf-8'))
# print("md5:",text_md5.hexdigest())

# key = 'string1-abc'
# yan = 'string2+anb'
# text_md5=hashlib.md5()
# text_md5.update(bytes((key+yan),encoding='utf-8'))
# print("md5:",text_md5.hexdigest())  #返回十六进制哈希值
# print("md5:",text_md5.digest())  #返回二进制哈希值

# import subprocess
# res = subprocess.Popen(['ping','-n','6','www.baidu.com'],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# # print(res)
# r1 = res.stdout.read()
# print(r1.decode('gbk'))
#
# err_res = res.stderr.read()
# print(err_res.decode('utf-8'))


