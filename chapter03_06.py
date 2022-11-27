# Chapter03-6
# 집합(Set) 특징
# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} #dic {}에 key없고 원소만 있으면 set
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set 에서 tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3]) # 튜플 특

# 리스트 변환(set 에서 list)
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2: ', s1&s2 ) #교집합
print('s1 & s2: ', s1.intersection(s2))

print('s1|s2 - ', s1 | s2) #합집합
print('s1|s2 - ', s1.union(s2))

print('s1-s2 - ', s1 - s2) #차집합
print('s1-s2 - ', s1.difference(s2))

# 중복 원소 확인
print('l - ', s1.isdisjoint(s2)) #false - 교집합 있다 / true - 교집합 없다

# 부분 집합 확인
print('subset - ', s1.issubset(s2)) #true - 부분집합이다 / false - 아니다
print('superset - ', s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# remove는 없는 원소 삭제하려면 에러 남

s1.discard(3)
print('s1 - ', s1)
# discard는 없는 원소 삭제하려해도 에러 안남

# 모두 제거
s1.clear()
print('s1 - ', s1)
