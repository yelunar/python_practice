# chapter02-1
# print 사용법
# 파이썬은 주석이 #이다

#기본 출력
print('Python start!')
print("Python start!")
print() #띄어쓰기 처리
print('''Python start!''')
print("""Python start!""")

# separator 옵션 - 분리가 무엇으 되어있는가
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('010', '1234', '5678', sep='-')

# end 옵션 - 줄 바꿈 안하고 하나의 라인으로 연결 
print('Welcome to', end=' ')
print('IT NEWS', end=' ')
print('Web Site')

#file 옵션 - 현재 이 내용을 내 하드디스크에 어떤 특정한 파일로 쓸 것이다
import sys 

print('Learn Python', file=sys.stdout)

# format 사용 (d - 정수 , s - 문자열 , f - 실수) 
#C에서도 배움

print('%s %s' % ('one', 'two')) #이 방법 더 추천
print('{} {}'. format('one', 'two'))

print('{1} {0}'. format('one', 'two')) 

# %s
print('%10s' % ('nice')) #10자 채우기 위해 부족한 부분 공백으로 채움
print('{:>10}' .format('nice'))

print('%-10s' % ('nice')) #왼쪽부터 글씨 채우고 공백
print('{:10}' .format('nice'))

print('{:_>10}' .format('nice')) #공백을 _로 채움

print('{:^10}' .format('nice')) # ^ 넣으면 중앙정렬

print('%.5s' % ('pythonstudy')) # 5자리만 출력, 나머지는 절삭
print('%5s' % ('pythonstudy')) #5자리 초과해도 모두 출력

# %d
print('%d %d' % (1,2))

print('%4d' % (42))
print('{:4d}' .format(42))

# %f
print('%f' % (3.12345))
print('{:f}'. format(3.12345))

print('%06.2f' % (3.13484188)) #6자리인데 .2 - 소수부가 2개


