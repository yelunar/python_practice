# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expression>:
#       <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n)
    n = n - 1

# 예제 2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

# 예제 3
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop End')

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop End')

# if 중첩
# 예제 5
i = 1

while i <= 10:
    print("i:", i)
    if i == 6:
        break
    i += 1

# while - else 구문
# 예제 6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'jin'

i = 0 # 리스트 안에 주소 0부터 시작
while i < len(a): # i 가 4니까 (문자가 4개니까 4인 것 같음)
    if a[i] == s: 
        break
    i += 1
else:
    print(s, 'not found in list')

# 무한반복
# while True:
#     print('Foo')

# 예제8
a = ['foo', 'bar', 'baz', 'qux']

while True: #while 안에 true 쓸거면 무조건 break 있어야함 아니면 평생 함
    if not a:
        break
    print(a.pop())

