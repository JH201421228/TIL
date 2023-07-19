### 함수의 정의와 호출
- 함수는 필요한 경우 결과를 반환할 수 있음
-  return 키워드 이후에 반환할 값을 명시
- return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
- 반환값이 없으면 None이 return된다.

### 매개변수와 인자
- 함수를 선언할 때 쓰는 것은 매개변수
- 함수를 사용할 때 쓰는 것은 인자

### 기본 인자 값
```python
def greet(name, age = 30):
# age는 공란으로 둘 시 30을 출력함
```

### 키워드 인자
```python
greeting(age = 25, name = 'Alice')
# 키워드 인자를 쓰면 순서를 지키지 않아도 된다.
```

### 임의 인자 목록
```python
def calculate_sum(*args):
# '*'를 붙이면 여러개를 입력받을 수 있다.
```

### 정해지지 않은 개수의 키워드 인자를 처리하는 인자
```python
def calculate_sum(**args):
# '**'를 붙이면 여러개의 키워드를 입력받을 수 있다.(dict 형태로 출력))
```

### 함수 인자 권장 작성순서
- 위치, 기본, 가변, 키워드, 가변키워드(권장)

### Python의 범위(scope)
> scope
- global scope : 코드 어디서근 참조할 수 있는 공간
- local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)

> variable
- global variable : global scope에 정의된 변수
- local variable : local scope에 정의된 변수

### 변수 수명주기
1. built-in scope
- 파이썬이 실행된 이후부터 영원히 유지
2. global scope
- 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
- 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### LEGB Rule

1. local scope
2. Enclose scope
3. Global scope
4. Built-in scope
> 상단에 명시한 순서대로 이름을 찾아나감

### Global 선언
```python
global num
# num을 전역 변수로 선언
```

### 매개변수에 global 사용 불가

### 재귀함수
- 함수내에서 본인을 호출하는 함수
> 팩토리얼
- 무한 호출 될 위험이 있음
- 종료 조건을 명확히
- 반복되는 호출이 종료 조건을 향하도록
```python
def factorial(n):
  if n == 0:
    return 0
  return n * factorial(n - 1)
```
### map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
- function 위치에 직접 만든 함수도 사용가능, 범용성이 높다.(map 최고)

### zip
- 넣은 값을 같은 인덱스별로 묶어 출력해줌(dict으로 출력 가능)

### lambda 매개변수 : 설명식
- map과 lambda를 같이쓰는 경우가 있음
- 익명함수이면서 1회성으로 사용할 때 사용

### 가변인자로 매개변수를 정의하면...
- 함수를 호출할 때 

### inport 하는 방법
- inport 파이썬 파일 명(상대경로)
- 파이썬 파일 명.함수

### 패키지
- 관련된 모듈들을 한군데 모아놓은 것
```python
from '패키지' import '모듈'
# 모듈 역시 해당 형식으로 사용 가능
```

### pip list
- 해당 명령어는 pip 개수를 보여줌

### pip install '라이브러리'
- 배쉬에서 실행하면 해당 라이브러리를 실행

### 함수명이 같을 수 있기 때문에 별명 지어줄 수 있음
```python
from '패키지' import '모듈' as '별명'
# 모듈 역시 해당 형식으로 사용 가능
```