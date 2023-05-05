# Python 3가지 Print Formatting

"""
참고 : Escape Code

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : NULL 문자
'''
"""

x = 50
y = 100
text = 308276567
n = 'Lee'

#출력 1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

#출력 2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력 3
ex3 = f'n = {n}, s = {text}, sum = {x+y}' # f 스트링 f''
print(ex3)
print(f'n = {n}, s = {text}, sum = {x+y}')
print()

# 구분기호
m = 10000000

print(f'm : {m:,}')

print()
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20

print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t center : {t:<10}")
print(f"t center : {t:>10}")

print()
print()

print(f"t center : {t:*^10}")