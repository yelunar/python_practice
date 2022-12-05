# 모듈 사용 실습

import sys
import time

print(time.time())

print(sys.path) #경로말해줌

print(type(sys.path))

sys.path.append('C:/python_practice')

print(sys.path)

import chapter06_02 #만든 모듈 불러옴

print(chapter06_02.power(10, 3))



