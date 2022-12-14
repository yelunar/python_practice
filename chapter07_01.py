# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리 ***
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다. (다른데로 처리 넘김)
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error)
# print('error'))
#if True (콜론 안붙힘)
#    pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c) - c가 define 되지 않음

# ZeroDivisionError
# print(100 / 0) - 분모에 0 못옴

# IndexError

# x = [50, 70, 90]
# print(x[1])
# print(x[4]) - 4번째가 없음
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) - 4번째가 없음

# KeyError (주로 딕셔너리에서)

# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby']) - hobby가 없음 
# print(dic.get('hobby')) - 권장(error 안남)

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2()) - time2라는 매소드가 없음

# ValueError 참조값이 없을 때

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200) - 200이 없음

# FileNotFoundError

# f = open('test.txt') - 이 위치에 해당 파일이 없을 때

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2] - 리스트
# y = (1,2) - 튜플
# z = 'test' - 문자

# print(x + y) 자료형 달라서 계산 못함
# print(x + z)
# print(y + z)

# print(x + list(y)) - ok (형 변환 후 처리)
# print(x + list(z)) - ok (형 변환 후 처리)

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
try: 
    z = 'Kim' # 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()

# 예제2

try:
    z = 'Cho' # 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except: #위 예제에서 에러 종류만 생략함 - 모든 에러 다 잡을 수 있지만 어떤 에러인진 모름
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()

# 예제3

try:
    z = 'Cho' # 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')
finally: #finally는 에러 발생 유무 상관없이 무조건 실행
    print('Ok! finally')

print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Park':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')