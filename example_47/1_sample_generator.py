#-*-coding:euc-kr
"""
Author : Soohan Bae
Github : https://github.com/shawnbae
Last Modification : 2021.04.14
"""
import time
import random
import os

# 작업 시작 메시지를 출력
print("Process Start.")

# 시작 시점의 시간 기록하기
start_time = time.time()

# 생성할 개인정보 파일 개수를 정의하기
NUM_SAMPLES = 1000

# 이메일 생성에 사용할 샘플 글자들을 정의하기
alphabet_samples = "abcdefghijklmnopqrstuvwxyz1234567890"

# 무작위로 선택된 영어 글자를 생성하는 함수
def random_string(length):
  result = ""
  for i in range(length):
    result += random.choice(alphabet_samples)
    
  return result

# 이름 생성에 사용할 글자들을 정의하기
first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"

# 무작위로 사람 이름을 생성하는 함수
def random_name():
  result = ""
  result += random.choice(first_name_samples)
  result += random.choice(middle_name_samples)
  result += random.choice(last_name_samples)
  return result

# 결과물을 저장할 폴더 생성하기
os.mkdir("personal_info")

# 개인정보 파일을 자동으로 생성하는 부분
for i in range(NUM_SAMPLES):
  name = random_name()
  
  # 결과물 파일의 이름을 정의
  filename = "personal_info/" + str(i) + "_" + name + ".txt"
  
  # 결과물 파일을 생성. 텅 빈 파일이 생성됨
  outfile = open(filename, 'w')
  
  # 결과물 파일에 이름 기재하기
  outfile.write("name : " + name + "\n")
  
  # 결과물 파일에 무작위로 생성된 나이를 기재
  outfile.write("age : " + str(time.time())[-2:] + "\n")
  
  # 결과물 파일에 무작위로 생성된 이메일을 기재
  outfile.write("e-mail : " + random_string(8) + "@naver.com\n")

  # 결과물 파일에 무작위로 생성된 부서명을 기재합니다.
  outfile.write("division : " + random_string(3) + "\n")
    
  # 결과물 파일에 무작위로 생성된 핸드폰 번호를 기재
  outfile.write("telephone : 010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2] + "\n")
  
  # 결과물 파일에 무작위로 선정된 성별을 기재
  outfile.write("sex : " + random.choice(["male", "female"]))
  
  # 결과물 파일 수정 마무리하기
  outfile.close()
  
# 작업 종료 메시지 출력하기
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력하기
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
  
  
  