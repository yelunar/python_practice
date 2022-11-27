# Chapter03-5
# 파이썬 딕셔러니
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone' : '01012345678', 'birth' : '980531'}
b = {0: 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Nicegirl',
    'City' : 'Ulsan',
    'Age' : 25,
    'Grage' : 'A',
    'Status' : True
}
e = dict([
    ('abc' , 'def')
]) # 잘 쓰이지는 않음

f = dict(
    Cookie = 'Grains'
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(c), e)
print('f - ', type(c), f)

#출력
print('a - ', a['name']) # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리 고로 이 방법 추천!
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('Cookie'))

#딕셔너리 추가
a['address'] = 'Busan'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능

print('a - ', list(a.keys())) #value값 냅두고 key만 가져옴
print('b - ', b.keys())
print('c - ', list(c.keys()))
print('d - ', d.keys())

print('a - ', a.values()) #값만 가져옴
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

print('a - ', a.items()) # key와 value 둘 다 가져옴
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

print()

print('a - ', a.pop('name')) #꺼내고 정렬
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))

print('f - ', f.popitem()) #item 은 순서가 없어서 랜덤으로 꺼냄

print('a - ', 'birth' in a)
print('a - ', 'addr' in a)

# 수정 & 추가
a['test'] = 'test_dict'
print('a - ', a)

f.update(candy = 'seeze')
print('f - ', f)

temp = {'address' : 'Ulsan'}
a.update(temp)
print('a-',a)

