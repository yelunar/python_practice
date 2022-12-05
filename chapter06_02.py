# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
# 모듈이 모이면 패키지

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y
    
def power(x, y): #제곱
    return x ** y

# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)

# 모듈화!!!
# 함수 만들어서 재사용 가능하게 하는 것
# 다른 파일에서도 가능

# __name__ 사용 
# 여기에서 컴파일하면 밑에꺼 실행, 외부에서 모듈로 불러오면 실행 안하는 예약어
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-' * 15)
