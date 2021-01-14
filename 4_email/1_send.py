#-*- coding: UTF-8 -*-

import smtplib
import urllib.parse # 유니코드 에러 해결을 위한 모듈
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(urllib.parse.quote(EMAIL_ADDRESS), urllib.parse.quote(EMAIL_PASSWORD)) # 로그인

    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문

    msg = f"Subject: {subject}\n{body}"

    # 발신자, 수신자, 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, "nadocoding@gmail.com", msg) 
    