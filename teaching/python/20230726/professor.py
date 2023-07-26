# 함수는 def 두에 함수 이름
# 클래스는 class 뒤에 클래스 이름
# 단, 클래스 name의 컨벤션은 PascalCase를 사용
# 컨벤션은 상호간의 약속이다. 어디서 어떤 라이브러리를 사용하든, PascalCase로 작성된 값들은 모두 클래스라는 사실을 내가 별도로 내부 코드를 확인하지 않아도 알 수 있다.
# 의문? list, str, int 얘네는 PascalCase 아닌데요? -> 이건 예외
# library 클래스에는 
    # 책의 관리 | 책의 정보: 제목, 작성자, 보유 권수 인스턴스 생성
    # 총 보유 책 권수
    # 대여 시스템 메서드

# User 클래스에서는
    # 유저 정보 관리 | 유저 정보 : 이름, 나이

class Library:
    # 클래스 변수
    number_of_book = 0
    
    # 생성자 : 클래스에 의해 인스턴스가 생성되는 순간, 실행되는 매직 매서드다.
    # double underscore 로 작성되는 메서드들은 모두 매직 메서드
    # 파이썬이 내부적으로 특정한 동작을 하도록 만들어놓은 메서드들
    
    # self의 역할 : 호출 대상 인스턴스 자체를 의미
    # numbers.append(3) -> append
    # self에는 특별한 의미가 없지만 암묵적으로 사용

    def __init__(self, title, author, volumes=1):
        self.title = title
        self.author = author
    
        # 책 정보에 책마다의 보유 권수를 따로 저장
        # 일반적으로, 동일한 책은 1권씩 추가되고, 특별한 경우에만 여러권이 추가가 된다면?
        self.volumes = volumes

        # 클래스 변수 호출하여 값 증가
        # 아래 방식은 생성자에서만 허용하는 느낌
        # 되도록이면 클래스 메서드를 호출하는 것을 권장
        # Library.number_of_book += 1
        
    # 데코레이터 classmathod를 함수 위에 작성시 해당 함수는 첫번째 인자를 호출 주체의 class를 받게 된다.
    # 인스턴스가 호출시에도 첫번째 인자는 호출한 인스턴스의 클래스를 인자로 넘겨주게 된다. 그래서, 인스턴스는 클래스 메서드도 호출시 정상적으로 작동하기는 하지만, 그렇게 쓰지는 말자.

    @classmethod
    def increase_book(cls, volumes):
        cls.number_of_book += volumes
    
    def __str__(self):
        return self.title
    
    # 소멸자
    # def __del__(self):
    #     print(f'{self.title}책을 제거하였습니다!')
    #     return None
    

# Library 클래스에 의해 만들어지는 book1 인스턴스는 자신만의 고유한 title과 author 정보를 가질 수 있다.



book1 = Library('홍길동전', '허균')
book2 = Library('레미제라블', '빅토리 위고', 10)
print(book1.volumes)
print(book1)
print(book1.title)
print(book2.volumes)
print(book2)
print(book2.title)
print('='*30)
print(Library.number_of_book)

class User:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.increase_user()

    @classmethod
    def increase_user(cls):
        cls.number_of_people += 1

person1 = User('김준호', 12)
print(person1.name)