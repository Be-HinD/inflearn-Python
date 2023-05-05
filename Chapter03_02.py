# Python 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""

print(len(str1)) # 공백포함 길이

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# Escape 문자 사용
print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print()

# Row string -> Escape 문자를 그냥 문자로 판단
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력
# 역슬래쉬 사용
multi_str = \
"""
string
Multi line
Test
"""
multi_str2 = 'asdf' \
'asdf' \
'asdf' \
'asdf' \

print(multi_str)
print(multi_str2)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Deagu"

print(str_o1 * 3)
print(str_o1 + ' ' +str_o2)
print('y' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))

# 문자열 함수(upper, isalnum, startswith, count, endwith, isalpha)
print("Capitalize : ", str_o1.capitalize()) # 첫글자 대문자로
print("endswith?: ", str_o2.endswith("!"))
print("replace", str_o1.replace("thon", ' Good'))
print("sorted : ", sorted(str_o1))
print("Split : ", str_o4.split(' '))

# 반복(시퀀스!)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(str_s1[0:3]) # 0 ~ 3-1
print(str_s1[5:11])
print(str_s1[:len(str_s1)])
print(str_s1[1:9:2]) # 3번째 인수는 skip단위
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1]) #음수는 방향전환

# ASCII CODE
a = 'z'

print(ord(a))
print(chr(122))