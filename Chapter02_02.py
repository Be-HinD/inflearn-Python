# Python 변수

# 기본 선언
n = 700

print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x,y,z)
print()

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Objedt References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300)
print(int(300))
print()

# ex2)
# n -> 777
n = 777

m = n

# id(identity) 확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 값이 할당되면 같은 id를 가짐
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfcollegeGraduates -> Class
# Snake Case : number_of_college_graduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 숫자시작, 특수문자 X

# 에약어는 변수명으로 불가능
