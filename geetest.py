from Crypto.Cipher import AES
import rsa
import random
import binascii
import hashlib
import time

class AESCipher():
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, raw):
        """加密"""
        text = raw.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, '0000000000000000'.encode('utf-8'))
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text +(chr(add)*add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text +(chr(add)*add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        sigBytes = len(self.ciphertext)
        words=[]
        for i in range(0,sigBytes,4):
            words.append(int.from_bytes(self.ciphertext[i:i+4], byteorder='big', signed=True))
        S8q = 10
        M5 = []
        D5 = 0
        I5=words
        while S8q * (S8q + 1) * S8q % 2 == 0 and D5 < sigBytes:
            U0Q = I5[D5 >> 2] >> 24 - D5 % 4 * 8 & 255
            M5.append(U0Q)
            if S8q > 82393:
                S8q=S8q - 10
            else:
                S8q=S8q + 10
            D5+=1
        return M5

        # return {'words':words,'sigBytes':sigBytes}



def sd(Z9):
    u2q = 0
    while u2q!=6:
        if u2q==0:
            U7q = 0
            u2q = 2
            continue
        if u2q==2:
            w9 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()";
            if U7q * (U7q + 1) % 2 + 5 and (Z9 < 0 or Z9 >= len(w9)):
                return "."
            else:
                return w9[Z9]

def ae(h9, N9):
    return h9 >> N9 & 1

def be(c9, O9):
    f2q = 0
    O9 = {'Td': 7274496, 'Ud': 9483264, 'Vd': 19220, 'Wd': 235, 'Xd': 24,'Sd':'.'}
    while f2q!=10:
        if f2q==26:
            e9=None
            f2q = 15
            continue
        if f2q==24:
            return {
                'res': l9,
                'end': n9
            }
        if f2q==34:
            if 2 == C9:
                e9 = (c9[u9] << 16) + (c9[u9 + 1] << 8)
                l9 += sd(b9(e9, O9["Td"])) + sd(b9(e9, O9["Ud"]))+ sd(b9(e9, O9["Vd"]))
                n9 = O9["Sd"]
            else:
                if 1==C9:
                    e9 = c9[u9] << 16
                    l9 += sd(b9(e9, O9["Td"])) + sd(b9(e9, O9["Ud"]))
                    n9 = O9["Sd"] + O9["Sd"]
            f2q = 30
            continue
        if f2q==3:
            C9 = a9 % 3
            f2q = 34
            continue
        if f2q==18:
            u9 += 3
            f2q = 9
            continue
        if f2q==6:
            def b9(x9, V9):
                L2q = 0
                while L2q!=26:
                    if L2q==0:
                        o9 = 0
                        s9 = O9["Xd"] - 1
                        L2q = 2
                        continue
                    if L2q==11:
                        if 1==ae(V9, s9):
                            o9 = (o9 << 1) + ae(x9, s9)
                        L2q = 6
                        continue
                    if L2q==6:
                        s9 -= 1
                        L2q = 2
                        continue
                    if L2q==9:
                        return o9
                    if L2q==2:
                        if s9 >=0:
                            L2q=11
                        else:
                            L2q = 9
            l9 = ""
            n9 = ""
            a9 = len(c9)
            u9 = 0
            f2q = 9
            continue
        if f2q==0:
            O7q = 0
            if not O9:
                O9={}
            f2q = 6
            continue
        if f2q==15:
            if u9 + 2 < a9:f2q=33
            else:f2q=3
        if f2q==30:
            if O7q >= 25198:
                O7q=O7q / 1
            else:
                O7q=O7q * 1
            f2q = 18
            continue
        if f2q==33:
            e9=(c9[u9] << 16) + (c9[u9 + 1] << 8) + c9[u9 + 2]
            l9 += sd(b9(e9, O9["Td"])) + sd(b9(e9, O9["Ud"])) + sd(b9(e9, O9["Vd"])) + sd(b9(e9, O9["Wd"]))
            f2q = 30
            continue
        if f2q==9:
            if u9 < a9 and O7q * (O7q + 1) % 2 + 8:
                f2q=26
            else:
                f2q=24
            continue

def get_aeskey():
    return hex((int(65536 * (1 + random.random())) | 0))[3:]+hex((int(65536 * (1 + random.random())) | 0))[3:]+hex((int(65536 * (1 + random.random())) | 0))[3:]+hex((int(65536 * (1 + random.random())) | 0))[3:]


def get_rsa(aeskey):
    public_key_n = '00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81'
    public_key_e = '10001'
    rsa_n = int(public_key_n, 16)
    rsa_e = int(public_key_e, 16)
    key = rsa.PublicKey(rsa_n, rsa_e)
    endata = rsa.encrypt(aeskey.encode(), key)
    endata = binascii.b2a_hex(endata)
    return endata.decode()

def wd(q3Q,m3Q,i5f):
    #'abc':b48.D48()[21][5][9][17]
    v4B='abc'
    while v4B!='':
        #b48.D48()[1][23][8]=b48.D48()[21][5][9][17]
        if v4B=='abc':
            v8h = 7
            B8h = 1
            #'def':b48.U48()[32][11][2]
            v4B='def'
        #b48.U48()[7][17][2]=b48.U48()[32][11][2]
        if v4B=='def':
            if B8h * (B8h + 1) * B8h % 2 == 0 and (not m3Q or not i5f):
                #'err':b48.U48()[7][28][13]
                v4B='err'
            else:
                #'hij':b48.U48()[20][14][23]
                v4B='hij'
        #b48.U48()[10][23][23]=b48.U48()[20][14][23]
        if v4B=='hij':
            F3Q=0
            M3Q=0
            p3Q=q3Q
            O3Q = m3Q[0]
            a3Q = m3Q[2]
            Q3Q = m3Q[4]
            #'klm':b48.U48()[12][12][30]
            v4B='klm'
        #b48.D48()[32][27][30]=b48.U48()[12][12][30]
        if v4B=='klm':
            F3Q = i5f[M3Q:M3Q+2]
            if F3Q and v8h * (v8h + 1) * v8h % 2 == 0:
                #'nop':b48.D48()[16][14][20]
                v4B='nop'
            else:
                # 'qrs':b48.D48()[24][29][11]
                v4B = 'qrs'
        #b48.U48()[10][26][7][2]=b48.D48()[16][14][20]
        if v4B=='nop':
            M3Q += 2
            Z3Q=eval('0x'+F3Q)
            N5f=chr(Z3Q%256)
            J3Q = (O3Q * Z3Q * Z3Q + a3Q * Z3Q + Q3Q) % len(q3Q)
            #'tuv':b48.U48()[30][28][22]
            v4B='tuv'
        #b48.D48()[8][28][22]=b48.U48()[30][28][22]
        if v4B=='tuv':
            p3Q=p3Q[0:J3Q]+ N5f +p3Q[J3Q:]
            #'wxy':b48.U48()[11][5][17]
            v4B='wxy'
        #b48.U48()[8][11][17]=b48.U48()[11][5][17]
        if v4B=='wxy':
            if v8h >= 64237:
                v8h=v8h - 1
            else:
                v8h=v8h + 1
            #'klm':b48.U48()[23][12][30]=b48.D48()[32][27][30]
            v4B='klm'
        if v4B=='qrs':
            return p3Q
        if v4B=='err':
            return q3Q

def create_k6v(gt,challenge,aeskey,c,s):
    rv6="M(n?Nc9MM(mFBB)U-(.O5T.VGi:TK4U)L:11(2Y-,.*ME)c.,IE1(E9(ESW(E3)(M3ZHU(Abb1(1K"

    model={"lang":"zh-cn",
           "type":"fullpage",
           "tt":"M(n?Nc9M1M(mFBB)U-(.O5?T.VGi:TK4U)L:11(2Y-,.*ME)c.,IE1(Ev9(ESW(E33)(M3ZHU(Abb1(1K",
           "light":"IMG_0|INPUT_1",
           "s":"c7c3e21112fe4f741921cb3e4ff9f7cb",
           "h":"88f51f4ee75ea2c1756ac7f872112e01",
           "hh":"4c1eacd27d37797a12a9aa5f14b18634",
           "hi":"98591f96727dbc5a69922eb1833ec326",
           "ep":{"ts":1547305412374,
                 "v":"8.6.6",
                 "ip":"",
                 "f":"dffa73f7724fc7c6e24bc0d7d9afc99b",
                 "de":False,"te":False,"me":True,"ven":"Google Inc.",
                 "ren":"ANGLE (NVIDIA GeForce GTX 1060 6GB Direct3D11 vs_5_0 ps_5_0)",
                 "ac":"fbb8562ae948a14c9ac9228a00afcce3",
                 "pu":False,"ph":False,"ni":False,"se":False,
                 "fp":["down",322,20,1547305378606,"pointerdown"],
                 "lp":["move",345,337,1547305380454,"pointermove"],
                 "em":{"ph":0,"cp":0,"ek":"11","wd":0,"nt":0,"si":0,"sc":0},
                 "tm":{"a":1547305358407,"b":1547305358436,"c":1547305358436,"d":0,"e":0,"f":1547305358408,"g":1547305358408,"h":1547305358408,"i":1547305358408,"j":1547305358408,"k":0,"l":1547305358408,"m":1547305358433,"n":1547305358436,"o":1547305358444,"p":1547305358602,"q":1547305358602,"r":1547305358633,"s":1547305358948,"t":1547305358948,"u":1547305358948},"by":2},
           "passtime":53450,"rp":"b92399f60336f2a6e857bbd44cd54d50"}
    model['tt']=wd(rv6,c,s)
    start=int(time.time())*1000-10000
    current_time=start-10000
    model['ep']['ts']=start
    model['ep']['fp']=["down",322,20,start-5000,"pointerdown"]
    model['ep']['lp'] = ["move",345,337,start-4000,"pointermove"]
    model['ep']['tm'] = {'a': current_time,
          'b': current_time + 258,
          'c': current_time + 258,
          'd': 0,
          'e': 0,
          'f': current_time + 1,
          'g': current_time + 4,
          'h': current_time + 38,
          'i': current_time + 38,
          'j': current_time + 166,
          'k': current_time + 100,
          'l': current_time + 166,
          'm': current_time + 256,
          'n': current_time + 257,
          'o': current_time + 287,
          'p': current_time + 538,
          'q': current_time + 538,
          'r': current_time + 549,
          's': current_time + 782,
          't': current_time + 782,
          'u': current_time + 782

          }
    m=hashlib.md5()
    m.update((gt+challenge).encode())
    model['ep']['f'] = m.hexdigest()
    n = hashlib.md5()
    n.update((gt + challenge+'53450').encode())
    model['rp'] = n.hexdigest()
    return json.dumps(model,ensure_ascii=False)





def Yd(L9):
    r2q=0
    while r2q!=33:
        if r2q==11:
            if W7q * (W7q + 1) % 2 + 4 and  R9 < P9:
                r2q=6
            else:
                r2q=15
            continue
        if r2q==0:
            W7q = 1
            r2q = 2
            continue
        if r2q==2:
            v9 = []
            R9 = 0
            P9 = len(L9)
            r2q = 11
            continue
        if r2q==15:
            R9 += 1
            r2q = 11
        if r2q==6:
            v9.append(L9[R9])
            if W7q > 56639:
                W7q=W7q - 10
            else:
                W7q=W7q + 10
            r2q = 26
            continue

def php_result(gt,challenge):
    timestamp = int(time.time() * 1000)
    aeskey = get_aeskey()
    rasstr = get_rsa(aeskey)
    e = AESCipher(aeskey)
    secret_data = '{"gt":"%s","challenge":"%s","offline":false,"product":"bind","width":"300px","protocol":"http://","slide":"/static/js/slide.7.5.3.js","fullpage":"/static/js/fullpage.8.6.6.js","type":"fullpage","aspect_radio":{"slide":103,"pencil":128,"beeline":50,"click":128,"voice":128},"voice":"/static/js/voice.1.1.7.js","static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"geetest":"/static/js/geetest.6.0.9.js","beeline":"/static/js/beeline.1.0.1.js","click":"/static/js/click.2.7.0.js","pencil":"/static/js/pencil.1.0.3.js","cc":4,"ww":true,"i":"3396!!17311!!CSS1Compat!!50!!-1!!-1!!-1!!-1!!3!!-1!!-1!!-1!!9!!9!!-1!!9!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!9!!-1!!4!!-1!!-1!!0!!0!!0!!0!!150!!938!!1920!!1040!!zh-CN!!zh-CN,zh!!-1!!1!!24!!Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36!!1!!1!!1920!!1080!!1920!!1040!!1!!1!!1!!-1!!Win32!!0!!-8!!076c43c07c085055349bb5d34baf5b00!!00d5137005d67b44eb23e7868362c796!!internal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjai,internal-nacl-plugin!!0!!-1!!0!!4!!Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings!!%s!!-1,-1,1,0,0,0,0,3,153,3,4,4,11,343,343,428,556,556,556,-1!!-1!!-1!!60!!6!!-1!!-1!!14!!false!!false"}' % (
    gt, challenge, timestamp)
    enc_str = e.encrypt(secret_data)
    c = be(enc_str, '')
    w = c['res'] + c['end'] + rasstr
    return (w,aeskey)

def ajax_result(gt,challenge,aeskey,c,s):
    e = AESCipher(aeskey)
    kv6 = create_k6v(gt, challenge, aeskey, c, s)
    enc_str = e.encrypt(kv6)
    c = be(enc_str, '')
    w = c['res'] + c['end']
    return w


def slide_result(aa,challenge,gt,passtime,userresponse):
    start = int(time.time()) * 1000 - 10000
    current_time = start - 10000
    tm={'a': current_time,
          'b': current_time + 258,
          'c': current_time + 258,
          'd': 0,
          'e': 0,
          'f': current_time + 1,
          'g': current_time + 4,
          'h': current_time + 38,
          'i': current_time + 38,
          'j': current_time + 166,
          'k': current_time + 100,
          'l': current_time + 166,
          'm': current_time + 256,
          'n': current_time + 257,
          'o': current_time + 287,
          'p': current_time + 538,
          'q': current_time + 538,
          'r': current_time + 549,
          's': current_time + 782,
          't': current_time + 782,
          'u': current_time + 782

          }
    n = hashlib.md5()
    n.update((gt + challenge).encode())
    f = n.hexdigest()
    ep = {
        'f': f,
        'me': True,
        'te': False,
        'tm': tm,
        'v': '7.5.3'
    }
    d4f = {'aa': aa, 'ep': ep, 'imgload': 106, 'lang': 'zh-cn', 'passtime': passtime, 'userresponse': userresponse}
    n = hashlib.md5()
    n.update((gt + challenge[:32] + str(passtime)).encode())
    d4f['rp'] = n.hexdigest()
    aeskey = get_aeskey()
    e = AESCipher(aeskey)
    kv6 = json.dumps(d4f,ensure_ascii=False)
    enc_str = e.encrypt(kv6)
    c = be(enc_str, '')
    w = c['res'] + c['end']
    rasstr = get_rsa(aeskey)
    return w+rasstr



if __name__ == '__main__':

    import time
    import requests
    import json
    res=requests.get(url='http://12315.jlgs.gov.cn:198/api/idcPublicityV/geetest?t=1547111150641')
    result=json.loads(res.text)
    gt=result.get('gt')
    challenge=result.get('challenge')
    timestamp=int(time.time()*1000)
    aeskey=get_aeskey()
    # aeskey='d97c963efa1ab389'
    rasstr=get_rsa(aeskey)
    e = AESCipher(aeskey)
    secret_data = '{"gt":"%s","challenge":"%s","offline":false,"product":"bind","width":"300px","protocol":"http://","slide":"/static/js/slide.7.5.3.js","fullpage":"/static/js/fullpage.8.6.6.js","type":"fullpage","aspect_radio":{"slide":103,"pencil":128,"beeline":50,"click":128,"voice":128},"voice":"/static/js/voice.1.1.7.js","static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"geetest":"/static/js/geetest.6.0.9.js","beeline":"/static/js/beeline.1.0.1.js","click":"/static/js/click.2.7.0.js","pencil":"/static/js/pencil.1.0.3.js","cc":4,"ww":true,"i":"3396!!17311!!CSS1Compat!!50!!-1!!-1!!-1!!-1!!3!!-1!!-1!!-1!!9!!9!!-1!!9!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!9!!-1!!4!!-1!!-1!!0!!0!!0!!0!!150!!938!!1920!!1040!!zh-CN!!zh-CN,zh!!-1!!1!!24!!Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36!!1!!1!!1920!!1080!!1920!!1040!!1!!1!!1!!-1!!Win32!!0!!-8!!076c43c07c085055349bb5d34baf5b00!!00d5137005d67b44eb23e7868362c796!!internal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjai,internal-nacl-plugin!!0!!-1!!0!!4!!Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings!!%s!!-1,-1,1,0,0,0,0,3,153,3,4,4,11,343,343,428,556,556,556,-1!!-1!!-1!!60!!6!!-1!!-1!!14!!false!!false"}'%(gt,challenge,timestamp)
    # secret_data='{"gt":"62756445cd524543f5a16418cd920ffd","challenge":"166591aaf9147b1592a945ed5325fd30","offline":false,"product":"bind","width":"300px","protocol":"http://","fullpage":"/static/js/fullpage.8.6.6.js","voice":"/static/js/voice.1.1.7.js","static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"geetest":"/static/js/geetest.6.0.9.js","type":"fullpage","pencil":"/static/js/pencil.1.0.3.js","beeline":"/static/js/beeline.1.0.1.js","slide":"/static/js/slide.7.5.0.js","click":"/static/js/click.2.7.0.js","aspect_radio":{"pencil":128,"voice":128,"slide":103,"click":128,"beeline":50},"cc":4,"ww":true,"i":"3391!!17322!!CSS1Compat!!50!!-1!!-1!!-1!!-1!!3!!-1!!-1!!-1!!9!!9!!-1!!9!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!9!!-1!!4!!-1!!-1!!0!!0!!0!!0!!150!!938!!1920!!1040!!zh-CN!!zh-CN,zh!!-1!!1!!24!!Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36!!1!!1!!1920!!1080!!1920!!1040!!1!!1!!1!!-1!!Win32!!0!!-8!!076c43c07c085055349bb5d34baf5b00!!00d5137005d67b44eb23e7868362c796!!internal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjai,internal-nacl-plugin!!0!!-1!!0!!4!!Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings!!1547296041683!!-1,-1,2,2,34,0,39,0,85,3,4,4,13,374,374,462,473,473,473,-1!!-1!!-1!!60!!6!!-1!!-1!!14!!false!!false"}'
    enc_str = e.encrypt(secret_data)
    c=be(enc_str,'')
    w=c['res']+c['end']+rasstr
    params={'gt':gt,'challenge':challenge,'lang':'zh-cn','pt':0,'w':w,'callback':'geetest_%s'%timestamp}
    resp2=requests.get(url='http://api.geetest.com/get.php',params=params)
    print(resp2.text)
    data = json.loads(resp2.text.split('(', 1)[-1].split(')')[0])
    c = data.get('data',{}).get('c')
    s = data.get('data',{}).get('s')
    kv6=create_k6v(gt,challenge,aeskey,c,s)
    enc_str = e.encrypt(kv6)
    c = be(enc_str, '')
    w = c['res'] + c['end']
    params = {'gt': gt, 'challenge': challenge, 'lang': 'zh-cn', 'pt': 0, 'w': w, 'callback': 'geetest_%s' % timestamp}
    resp3 = requests.get(url='http://api.geetest.com/ajax.php', params=params)
    print(resp3.text)





