import  requests

# 进行伪装请求，伪装请求的服务信息，发送给服务器
url='http://127.0.0.1:8888/index'
header={'User-Agent':'2.26.0'}
res=requests.get(url,headers=header)
# print(res)
# 响应头  响应状态码  响应报文  正文
print('响应头:'+str(res.headers))
# print('响应状态码:'+res.status_code)
# print('响应正文:'+res.text)  #xml  html  json
print('请求头:'+str(res.request.headers))