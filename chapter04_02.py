# Chapter04-2
# 파이썬 반복문
# FOR 실습

#  코딩의 핵심
# for in <collection>
#       <loop body>

for v1 in range (10): # 0부터 n-1까지 총 n개 출력 됨
    print('v1 is :', v1)

print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2): # 1부터 10까지 2개씩 스킵하면서
    print('v3 is : ', v3)

print()

# 1 ~ 1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)) )

print('1~ 1000 4의 배수의 합: ', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리) - 전부 다 for문 사용 가능
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Na', 'Sim', 'Park', 'Cho', 'Yoo']

for n in names:
    print('You are in : ' , n)

# 예제2
lotto_numbers = [11, 12, 42, 13, 24, 52]

for n in lotto_numbers:
    print('Current number : ', n)

# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name" : 'Yejin',
    "Age" : 25,
    "City" : "Busan"
}

for k in my_info:
    print('key: ', my_info[k]) #key만 가져오기

for v in my_info.values():
    print('value : ', v) 

# 예제 5
name = 'FineApplE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break문

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not found: : ', num)
    
# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: # bool 은 true false 같은 논리값
        continue
    print("currnet type: ", v, type(v))
    print('multiply by 2', v*3)

# for - else 구문

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print('Not Found: 24')

for num in numbers:
    if num == 49:
        print("Found : 49")
        break
else:
    print('Not Found: 49')

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end="") # end 옵션 - 줄 바꿈 안하고 하나의 라인으로 연결 
    print()

# 변환 예제
name2 = 'Cindy'
print('Reversed : ', reversed(name2)) #이상한 id 값 나옴
print('List : ', list(reversed(name2)))
print('Tuple : ', tuple(reversed(name2)))
print('Set : ', set(reversed(name2)))  # 순서X

