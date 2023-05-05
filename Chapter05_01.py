# 딕셔너리(사전)
# 딕셔너리 자료형 (순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name':'Kim', 'Phone':'01033337777'
     , 'birth':'870514'}
b = {0:'Hello Python'}
c = {'arr':[1,2,3,4]}
d = {
    'Name':'Niceman',
    'City':'Seoul',
    'Age':33,
    'Grade':'A',
    'Status':True
}
e = dict([
    ('Name','Niceman'),
    ('City','Seoul'),
    ('Age',33),
    ('Grade','A'),
    ('Status',True)
])

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 키 존재x -> 에러발생
print('a - ', a.get('name1')) # 키 존재x -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Seoul' # 이런식으로 기존 값 수정도 가능
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 추가
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print()

# 딕셔너리 함수 (주로 반복문을 사용하기 위해)
# dice_keys, dict_values, dict_items : 반복문(__iter__)에서 사용가능
print('a - ', a.keys()) # Values x
print('a - ', list(a.keys()))

print()

print('a - ', a.values())
print('a - ', list(a.values()))

print()

print('a - ', a.items()) # 튜플 형태의 결과
print('a - ', list(a.values()))

print()

print('a - ', a.pop('name'))
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem()) # 딕셔너리는 순서x라서 무작위로
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'city' in d)
print()

# 수정
a['test'] = 'test_dict'
a['address'] = 'deagu'

a.update(birth='910904')

temp = {'address':'Busan'}
a.update(temp)

print('a - ', a)
