import smtplib
import urllib.parse # 유니코드 에러 해결을 위한 모듈
from email.mime.text import MIMEText
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login("로그인할 메일계정", "앱 비밀번호") # 로그인

    msg = MIMEText('내용 : 안녕하세요.')
    msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'

    # 발신자, 수신자, 정해진 형식의 메시지
    smtp.sendmail("보내는 메일", "받는 메일", msg.as_string()) 
    smtp.quit()
