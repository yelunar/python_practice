# Chapter04-1
# 파이썬 제어문
# If 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc" 문자,  [1,2,3], (1,2,3) ... 
print(type(False) ) #비어있는 모든 것 0, "",[], ()

# 예1
if True:
    print('Good') #true 여야만 출력됨

if False:
    print('Bad')

# 예2
if False:
    print('Bad!')
else:
    print('Good!')

# 관계 연산자
# >, >=, <, <=, ==, != (같지 않다)

x = 15
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

city = ""
if city:
    print("You are in:", city)
else:
    print("plz enter your city")

city = "Ulsan"
if city:
    print("You are in:", city)
else:
    print("plz enter your city")

# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b < c)
print('or:', a > b or b < c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용

print('e1 : ', 3+12 > 7+4)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 80
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A' :
    print('Pass')
else:
    print('Fail')

# 예제
id1 = 'VIP'
id2 = 'admin'
grade = 'platinum'

if id1 == 'VIP' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

# 다중 조건문

num = 70

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else :
    print('과락')

# 중첩 조건문

grade = 'A'
total = 44

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('전액 등록금')

# in, not in

q = [10, 20, 30] #리스트
w = {70, 80, 90} #튜플
e = {"name" : "Kim", "city" : "Busan", "grade" : "A"} #딕셔너리
r = (10, 12, 13) #튜플

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e) # 딕셔너리는 key 만 가져옴
print("Busan" in e.values()) #e.values 키는 버리고 값만 가져옴
