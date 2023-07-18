# 진법 변경 (10진수 -> n진수)
print(bin(12))
print(oct(12))
print(hex(12))

print(2 / 3)
print(5 / 3)

# 지수 표현(10^)
print(314e-2) #3.14
print(314e2) #31400.0

# f-strig
bugs = 'roaches'
counts = 13
area = 'living room'

print(f'Debugging {bugs} {counts} {area}')
print('Debugging {} {} {}'.format(bugs, counts, area))
print('Debugging %s %d %s' % (bugs, counts, area))

# f-string 응용 (f-string advanced 검색하면 나옴)
greeting = 'hi'
print(f'{greeting:^10}')
print(f'{greeting:>10}')
print(f'{greeting:<10}')
print(f'{3.141592:.4f}')

my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

print(len(my_list))
print(my_list[4][-1])
print(my_list[-1][1][0])

# 불변과 가변
# my_str = 'hello'
# my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)