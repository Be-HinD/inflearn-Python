# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 논리형
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
# float = 10.0
# int = 7
# list = [str1, str2]
# dict = {
#     "name": "Machine Learning",
#     "version": 2.0
# }
# tuple = (3, 5, 7)
# set = {7, 8, 9}

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x ** y -> x^y

"""

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b),type(c),type(d))
print()

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 자동으로 몫/나머지 할당
print(x,y)
print(pow(5,3), 5**3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print('%1.100f' % math.pi) 