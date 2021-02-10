import requests
import time
import json

def get_ip():
    return None

def my_request(url='', conn=requests, proxy=None, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
               , allow_status=[200,404], timeout=(5, 8), method='get', data=None, retry=5,
               timesleep=0, show_result=False, allow_redirects=False, verify=True, change_ip_times=5,log_record=False,error_path='request_error.txt'):
    request_count = 0
    status_code_not_allow = 0
    while True:
        if proxy and status_code_not_allow > change_ip_times:
            proxy = get_ip()
        try:
            if method.lower() == 'get':
                response = conn.get(url=url, headers=headers, params=data, timeout=timeout,
                                    allow_redirects=allow_redirects,
                                    proxies=proxy, verify=verify)
                print("响应状态：{} 访问url：{} 请求参数：{}".format(response.status_code, url, data))
                if response.status_code in allow_status:
                    return {'res': response, 'conn': conn, 'proxy': proxy}
                if response.status_code not in allow_status:
                    status_code_not_allow += 1
                if proxy and response.status_code == 403:
                    proxy = get_ip()
                if show_result:
                    print(response.text)

            elif method.lower() == 'post':
                response = conn.post(url=url, headers=headers, data=data, timeout=timeout,
                                     allow_redirects=allow_redirects,
                                     proxies=proxy, verify=verify)
                print("响应状态：{} 访问url：{} 请求参数：{}".format(response.status_code, url, data))
                if response.status_code in allow_status:
                    return {'res': response, 'conn': conn, 'proxy': proxy}
                if response.status_code not in allow_status:
                    status_code_not_allow += 1
                if proxy and response.status_code == 403:
                    proxy = get_ip()
                if show_result:
                    print(response.text)
        except Exception as e:
            if log_record:
                print("本次请求失败,重试次数剩余：{} ,错误日志记录位置：{}".format(retry - request_count,error_path))
                with open(error_path, 'a')as f:
                    error = {'url': url, 'data': data, 'error': str(e),'headers':headers,'proxy': proxy,  'method': method,'retry_times':retry ,'retry_times_now': request_count,
                             'allow_statu_code': allow_status, 'allow_redirects': allow_redirects}
                    error = json.dumps(error)
                    f.write(error + '\n')
            else:
                print("本次请求失败,重试次数剩余：{} ".format(retry - request_count))
            proxy = get_ip()
        request_count += 1
        time.sleep(timesleep)
        if request_count > retry - 1:
            print("请求失败 request_way：{} URL：{} data：{} retry_times：{}".format(method, url, data, retry))
            return None
