# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X,삭제X) #불변 - 한 번 선언해서 끝까지 씀

# 선언
a= ()
b= (1,) #원소가 하나일 땐 끝에 , 찍어줘야함 그래야 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) #튜플을 리스트로 변환

# 수정x
# d[0] = 1500 - 에러 남
# print('d - ', d)

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3 - ', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(5)) # index - 위치 알려주기
print('a - ', a.count(4)) # count - 넣은 값 개수 알려주기

# 패킹 & 언패킹 (Packing, and Unpacking)

# 패킹 - packing 말그대로 묶는 것
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# 언패킹1
(x1, x2, x3, x4) = t # 괄호 없어도 되긴 함
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹 & 언패킹
t2  =1, 2, 3
t3 = 4, 
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

'''
tuple(튜플)은 불변한 순서가 있는 객체의 집합
list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없음
REPL에서 확인해보기

list와 마찬가지로 다양한 타입이 함께 포함될 수 있음
'''
