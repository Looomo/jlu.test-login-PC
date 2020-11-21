# -*- coding: utf-8 -*-
import requests

user = '' # put your user name here , shanyx20 for example.
passwd = '' # your password.

headers = {
'Host': 'net.jlu.edu.cn',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-CN; MI 8 UD Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 Quark/4.5.0.149 Mobile Safari/537.36',
'Accept': 'text/css,*/*;q=0.1'
}
url='https://net.jlu.edu.cn/login?DDDDD='+ user +  '&upass=' + passwd + '&R1=0&R2=&R3=0&R6=1&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=&v6ip='

r = requests.get(url , headers)

if r.status_code == 200:
    print("登录成功")
else:
    print("登录失败，返回值" + r.status_code)
