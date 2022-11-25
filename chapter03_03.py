#Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

#선언 (리스트 선언 방식)
a = []
b = list()
c = [70, 75, 80, 85] #Len 0부터 시작
d = [1000, 10000, 'Ace', 'Base', 'Captine'] #서로 다른 자료형 한 리스트에 담기ok
e = [100, 1000, ['Ace', 'Base']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

#인덱싱 - 원하는 데이터 가져오는 것
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ',d[0] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) #첫 번째 리스트의 번호에 해당하는 값 
print('e - ', list(e[-1][1]))

#슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][0:2])

#리스트 연산 - 집합+집합=집합
print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3) # c원소가 3번 출력
print('Test' + str(c[0])) # 변수형 맞춰줘야함

#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

#Identity(id) 같은 id 값
temp = c
print(c == temp)

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4 # 0번에 있는거 숫자 4로 바꿈
print('c - ', c)

c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 리스트 안에 리스트
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3] # 삭제
print('c - ', c)

#리스트 함수
print()
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 끝에 데이터 추가하고 싶을 때 append
print('a - ', a)
a.sort() #데이터 정렬
print('a - ', a) 
a.reverse() #데이터 역순
print('a - ', a) 
print('a - ', a.index(3), a[3]) #a의 index3번 가져와 a.index(3) = a[3]
a.insert(2, 7) # 2번째 위치에 7 넣기 /원하는 위치에 원하는 값 넣음
print('a - ', a)
a.reverse()
print('a - ', a)

# del a[6] 이렇게는 잘 안쓰고 왜냐면 원하는 값이 어느 위치인지 알아야하니까
a.remove(10) # 내가 없애고 싶은 값 넣으면 됨
print('a - ', a)

print('a - ', a.pop()) # 원래 리스트에서 제일 마지막 값 원소 가져오고 나머지 원소들로 list 구성
print('a - ', a)
print('a - ', a.pop())
print('a - ', a) #개수가 자꾸 줄어드네

print('a - ', a.count(4)) #원하는 값이 몇 개 있는지

ex = [8, 9]
a.extend(ex) #리스트 연장
print('a - ', a)

# 삭제 remove, pop(끝만 삭제), del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
