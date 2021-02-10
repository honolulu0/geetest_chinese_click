#-*-coding:utf-8-*-
from flask import request
from flask import Flask
import logging
import json
from main import geetest_slide

app = Flask(__name__)

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
geet_slide = geetest_slide()
global t_orbit

@app.route('/captcha', methods=['POST','GET'])
def parse_server():
  data = request.args

  gt = data.get('gt', None)
  challenge = data.get('challenge', None)
  res = {}
  if gt is None:
    msg = "need img param"
    code = 400
    res['msg'] = msg
    res['code'] = code
    res['data'] = []
  else:
    result = geet_slide.init_captcha(gt,challenge)
    res['msg'] = 'success'
    res['code'] = 200
    res['data'] = result
  return json.dumps(res)





if __name__ == '__main__':
  app.run(port=8001, host="0.0.0.0")
  #请求方式
  # f = open(image_path, 'rb')
  # s = base64.b64encode(f.read()).decode()
  # res=requests.post(url='http://127.0.0.1:5000/captcha',data=json.dumps({'img':s}))
  # print(res.text)


