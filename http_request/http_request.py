# utf-8
import  requests

url='http://127.0.0.1:8888/index'
# header={'User-Agent':'2.26.0'}
# res=requests.get(url,headers=header)
res=requests.get(url)
print(res)
# 响应头  响应状态码  响应报文  正文
print('响应头:'+str(res.headers))
print('响应状态码:'+res.status_code)
print('响应正文:'+res.text)  #xml  html  json
print('请求头:'+str(res.request.headers))


# post请求
post_url='http://127.0.0.1:8888/login'
data={"mobilephone":'admin','pwd':123456}
post_res=requests.post(url,data)
print('响应头'+post_res.headers)
print('响应状态码'+post_res.status_code)
print("cookie"+post_res.cookies) #登录之后才有cookie产生  类字典形式 可以通过key取值
print("cookie value"+post_res.cookies['cookies']) #类字典形式 可以通过key取值
print('响应正文'+post_res.json())  #xml  html  json

# 重点：html xml  json  > text
#html xml  >json （）会报错！只有json类型的返回值才支持json


# 充值
recharge_url='http://127.0.0.1:8888/recharge'
recharge_data={"mobilephone":'admin','amount':1000}
recharge_res=requests.get(recharge_url,recharge_data,cookies=post_res.cookies)
print("充值结果:",recharge_res.json())
print("状态码：",recharge_res.status_code)
print("代理user-agent",res.request.headers)

#抱歉，请先登录！ 因为http是无状态的，所以需要加上cookie, status_code:200  这说明 200 不是代表成功，只是代表在服务器中找到了对应的地址
# 这里解决了cookie的问题

# 验证码：
# 1、屏蔽
# 2、数据库查实时的
# 3、万能码
# 4、手动填写