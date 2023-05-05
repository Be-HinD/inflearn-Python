# Python List
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o) 유일한 자료형

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d =[1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) # 리스트안의 리스트 접근
print('e - ', list(e[-1][1]))

# 슬라이싱
print()
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print()
print('>>>>>')
print('c + d = ', c+d)
print('c * 3', c*3)
print('c * 3', sorted(c *3))
print("'Test' + c[0]", 'Test' + str(c[0]))
print()

# 값 비교
print(c == c[:3] + c[3:])

# Identity(id)
temp = c #주소참조형식
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print()
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = [] # 삭제
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 맨 뒤 추가
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # 원하는 위치에 추가
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[index]
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop()) # 마지막값을 제거 후 반환
print('a - ', a)
print('a - ', a.count(4)) # 리스트 안에 해당하는 Index 개수 찾기
ex = [8,9]
a.extend(ex)
print('a -', a)

# 삭제 : remove**, pop*, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)




