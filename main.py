from geetest import php_result
from gsxt_val_238 import get_val
from Tools import my_request,get_ip
from getphp_new import ajax_result
import time,requests,json,base64

class geetest_slide():
    def __init__(self):
        self.headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, sdch',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Upgrade-Insecure-Requests': '1',
                   'Connection': 'keep-alive',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        self.captcha_headers = {
                    'Content-Type': 'image/jpeg'
                }
        self.proxy = get_ip()
        self.click_chinese_url = 'http://127.0.0.1:80/captcha'
        self.retry = 5

    def init_captcha(self,gt,challenge):
        session = requests.Session()
        self.proxy = get_ip()
        w, aeskey = php_result(gt, challenge)
        params = {'gt': gt, 'challenge': challenge, 'w': w, 'callback': 'geetest_%s' % int(time.time() * 1000),
                  'lang': 'zh-cn', 'pt': '0'}
        res = my_request(conn=session, method='get', url='http://api.geetest.com/get.php',
                         data=params, headers=self.headers, allow_status=[200], timeout=(10, 10), proxy=self.proxy)
        response = res.get('res').text
        items = json.loads(response.split('(')[-1][:-1])
        if items.get('data'):
            s = items.get('data').get('s')
            c = items.get('data').get('c')
            w = ajax_result(gt, challenge, aeskey, c, s)
            params = {'gt': gt, 'challenge': challenge, 'w': w,
                      'callback': 'geetest_%s' % int(time.time() * 1000), 'lang': 'zh-cn', 'pt': '0'}
            resp = my_request(conn=session, method='get', url='http://api.geetest.com/ajax.php', data=params,
                              headers=self.headers,
                              allow_status=[200, ], timeout=(10, 10), proxy=self.proxy)
            if resp.get('res').status_code == 200:
                response = resp.get('res').text
                content = json.loads(response.split("(", 1)[-1].split(")")[0])
                if content.get('status') == 'success':
                    print(content)
                    if 'slide' in response:
                        return None
                    if 'click' in response:
                        print("geetest文字点选验证初始化完成")
                        result = self.download_click_chinese_pic(session=session, gt=gt, challenge=challenge)
                        return result
                    if 'validate' in response:
                        print("一次性通过")
                        return content['data']
        else:
            return None

    def download_click_chinese_pic(self, session, gt, challenge):
        resp = my_request(conn=session, method='get',
                          url='http://api.geetest.com/get.php?is_next=true&type=click&gt={}&challenge={}&lang=zh-cn&https=false&protocol=http%3A%2F%2F&offline=false&product=embed&api_server=api.geetest.com&width=100%25&callback=geetest_{}'.format(
                              gt, challenge, int(time.time() * 1000)), headers=self.headers, allow_status=[200, ],
                          proxy=self.proxy)
        if resp.get('res').status_code == 200:
            response = resp.get('res').text
            content = json.loads(response.split("(", 1)[-1].split(")")[0])
            if content.get('status') == 'success':
                pic = content.get('data')['pic']
                c = json.dumps(content.get('data')['c'], ensure_ascii=False)
                s = content.get('data')['s']
                code_nums = content.get('data')['num']
                img_url = 'http://static.geetest.com%s?challenge=%s' % (pic, challenge)
                while True:
                    resp = my_request(conn=session, method='get', headers=self.headers, allow_status=[200, ],
                                      timeout=(10, 10),
                                      url=img_url, proxy=self.proxy)
                    captcha = resp.get('res').content
                    with open('click.jpg', 'wb')as f:
                        f.write(captcha)
                    image = base64.b64encode(captcha).decode()
                    res = requests.post(url=self.click_chinese_url, data=json.dumps({'img': image}))
                    data = res.json().get('data')
                    print(f'极验文字点选识别结果： {data}')
                    points = [str(int(round(v.get('x') / 344 * 10000, 0))) + '_' + str(
                        int(round(v.get('y') / 344 * 10000, 0))) for v in data.values()]
                    points = ','.join(points)
                    w = get_val(points, challenge, gt, pic, c, s)
                    params = {'gt': gt, 'challenge': challenge, 'lang': 'zh-cn', 'pt': '0', 'w': w,
                              'callback': 'geetest_%s' % int(time.time() * 1000)}
                    resp = my_request(conn=session, method='get', headers=self.headers,
                                      url='http://api.geetest.com/ajax.php', data=params,
                                      allow_status=[200, ], timeout=(10, 10), proxy=self.proxy)
                    if resp.get('res').status_code == 200:
                        response = resp.get('res').text
                        val_items = json.loads(response.split('(')[-1].split(')')[0])
                        print(val_items)
                        if val_items.get('data'):
                            if val_items['data'].get('validate'):
                                result = {"code": 0, "status": "success", "challenge": challenge,
                                          "validate": val_items['data'].get('validate'), "account": None}
                                return result
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None












