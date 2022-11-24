# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy 쓸 때 ' 이거 예외 시키기
print("I'm Boy")
print('I\'m Boy')
print(' a\t b')
print('a\"\n b')

"""
참고 : Escape 코드

\n : 줄바꿈
\t : 띄우기
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "What\'s on TV"
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New line \n Check!"
print(t_s1)
print(t_s2)
print()

# Raw String - \를 있는 그대로 그냥 출력
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

# 멀티라인 입력
# """를 다음 줄에 띄워서 입력하려면 역슬러시 넣어야함 
multi_str1 = \
"""
type
multiline input
test
"""
print(multi_str1)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Ulsan Busan Seoul Jeju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o2)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(int(True), type(int(True)))

#문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha .. )

print("Capitalize: ", str_o1.capitalize()) # 첫 글자만 대문자로 변경
print("endswith?: ", str_o1.endswith("e")) # 끝 글자 뭔지 알려줌
print("replace", str_o1.replace("thon", 'Good')) # 해당 글자 대체
print("sorted ", sorted(str_o1)) # 알파벳 순서에 따라 정렬
print()
print("join str: ", str_o1.join(["I'm ", "!"]))
print("split: ", str_o4.split(' '))  # Type 확인 공백을 기준으로 단어 나눔
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복(시퀀스)
im_str = "Good girl!"

print(dir(im_str)) # __iter__ 확인

# 출력
for i in im_str:
    print(i) # 한글자 씩 엔터치고 나열

# 슬라이싱
str_s1 = "Nice Python"

#슬라이싱 연습
print(str_s1[0:3]) #앞에서부터 3개 나옴 3-1까지 나옴 0부터 2까지
print(str_s1[5:]) # 5부터 끝까지
print(str_s1[:]) # 처음부터 다
print(str_s1[:len(str_s1)]) # 처음부터 다
print(str_s1[1:4:2]) # 1부터 4까지 2개씩
print(str_s1[-5:])
print(str_s1[::-1])

#아스키 코드
a = 'z'  

print(ord(a)) #아스키코드
print(chr(122)) #문자로






