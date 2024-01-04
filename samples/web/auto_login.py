import requests
from bs4 import BeautifulSoup

# 登录页面的URL
login_url = 'http://10.80.66.220:8099/portal/redirect/portal/10.1.45.200?wlanuserip=10.1.45.170&wlanacname=AC&client%5Fmac=B8-76-3F-A6-E7-AF'

# 创建会话
session = requests.Session()

# 发送GET请求以获取登录页面
response = session.get(login_url)

# 解析登录页面的HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到用户名和密码的输入框
username_input = soup.find('input', {'id': 'usr'})
password_input = soup.find('input', {'id': 'pwd'})


# 填充用户名和密码
username = '181500236'
password = 'w@181500236'
username_input['value'] = username
password_input['value'] = password

# 找到登录按钮并模拟点击
login_button = soup.find('div', {'class': 'subbtn'})
onclick_value = login_button['onclick']
session_id = onclick_value.split('(')[1].split(')')[0]
payload = {'session_id': session_id}  # 根据实际情况构造payload
response = session.get(login_url, data=payload)

# 检查登录是否成功
if '登录成功' in response.text:
    print('登录成功！')
else:
    print('登录失败！')