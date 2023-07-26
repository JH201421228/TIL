# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스를 생성
singer1 = Person('IU')
singer2 = Person('BTS')
print(singer1.singing())
print(singer2.singing())

print(singer1.blood_color)
print(singer2.blood_color)

