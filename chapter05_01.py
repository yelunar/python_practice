# Chapter05-1
# 파이썬 함수 및 중요성 - 코드의 재사용, 안정성
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제1
def first_func(w1):
    print("Hello, ", w1)

word = "GOODGIRL"

first_func(word)

# 예제2
def return_func(w1):
    return "Hello, "+ str(w1)

x = return_func('Goodgirl2')
print(x)

# 예제3 (다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

x, y, z = func_mul(10)

print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul2(30)

print(type(p), p, set(q))

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul3(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs - 별표 붙은거

# *args(언팩킹)
def arg_func(*args): #매개 변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('----')

arg_func('Kim')
arg_func('Kim', 'Na')
arg_func('Kim', 'Na', 'Sim')

# **kwargs(언팩킹)
def kwargs_func(**kwargs):  #매개 변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('----')

kwargs_func(name1 = 'Kim')
kwargs_func(name1 = 'Kim', name2 = 'Na')
kwargs_func(name1 = 'Kim', name2 = 'Na', name3 = 'Sim')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

# 중첩함수 (함수안에 함수가 들어있음)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 100)

nested_func(100)
# 실행불가
# func_in_func(1000) - 얘가 단독으로 나와있으면 에러남

# ---------------------

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스 (메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#    return x * y
    
# lambda x, y:x*y (함수에 이름이 없음)

# 일반적 함수 -> 할당

def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20,50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50,50))


def func_final(x, y, func):
    print('>>>', x * y * func(100, 100))

func_final(10, 20, lambda x,y:x * y)
func_final(10, 20, lambda_mul_func)
func_final(10, 20, mul_func) # 다 똑같이 출력됨