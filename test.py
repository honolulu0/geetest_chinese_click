import requests,time
from multiprocessing.dummy import Pool as ThreadPool



def get_validate_wander(challenge,gt):
    url=f'http://127.0.0.1:8001/captcha?gt={gt}&challenge={challenge}'
    print(url)
    response = requests.get(url=url)
    print(response.json())

def run():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
            }
            session = requests.session()
            query_url = f'https://www.geetest.com/demo/gt/register-click-official?t={int(time.time() * 1000)}'
            query_res = session.get(url=query_url, headers=headers).json()
            print(query_res)
            gt = query_res['gt']
            challenge = query_res['challenge']
            s = get_validate_wander(challenge, gt)
        except:
            pass




if __name__ == '__main__':
    run()



