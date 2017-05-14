# -*- coding:utf-8 -*-
import os
import sys
import urllib.request

#client_id = "5aswYI9qgxt45cEqJ1WP"
#client_secret = "BkUPYoTP4W"
client_id = "xf924K4IYWlnu5iFAjsm"
client_secret = "eNuA0yqy0X"
encText = urllib.parse.quote("내이름은 주새별. 아니 주뉴별. 아니 뉴 스타")
data = "speaker=mijin&speed=0&text=" + encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if (rescode == 200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)