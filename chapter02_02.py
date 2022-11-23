#chapter02-2
# 파이썬 변수

# 기본 선언
n=700

print(n)  #n에 700 입력
print(type(n)) #type - 안에 있는 type 자료형을 알려줌

# 동시선언
x = y = z = 700
print(x,y,z)

#선언
var =75

#재선언
var="Change Value"

#출력
print(var)
print(type(var))

# object references
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성 2. 값 생성 3. 콘솔 출력

#예시1
print(300)
print(int(300)) 
#int(300) class형태로 300이 int니까 출력 - type에 맞는 오브젝트 생성

#예시2
n=777
print(n, type(n))
print()

m = n
print(m, n)
print(type(m), type(n))

m=400
print(m, n)
print(type(m), type(n))

# id(identity)확인: 객체의 고유값 확인

m=800
n=655

print(id(m))
print(id(n)) # 이상한 id(고유값)이 나옴 - 중복불가
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m=800
n=800

print(id(m))
print(id(n)) # 이상한 id(고유값)이 나옴 - 중복불가
print(id(m) == id(n))
print() #이때는 true

#다양한 변수 선언
# Camel case: numberOfColledgeGraduates - 처음 단어는 소문자 연결되는 단어 첫 글자는 대문자 (method)
# Pascal case: NumberOfColledgeGraduates - 시작단어 대문자 (class)
# Snake case: number_of_college_graudates - 모두 소문자 이어지는 단어 _로연결

student_grage = 3
print(student_grage)

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 7

# 예약어는 변수명으로 불가능
# for , as , class 등등 (python reserved words)

"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""