import requests

class HttpRequest:
    '''
    利用requests封装get请求和post请求
    '''
    def http_request(self,url,data,method,cookie=None):
        '''
        参数化
        '''
        if method.lower()=='get':
            res = requests.get(url, data, cookies=cookie)
        else:
            res=requests.post(url,data,cookies=cookie)

        return  res  #返回消息实体


if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login'
    data = {'user': 'admin', 'pwd': '123456'}
    res=HttpRequest().http_request(url,data,'post')
    # print('响应正文:',res.text)

    # 充值
    recharge_url = 'http://127.0.0.1:8888/recharge'
    recharge_data = {"mobilephone": 'admin', 'amount': 1000}
    recharge_res = requests.get(recharge_url, recharge_data,'get', res.cookies)