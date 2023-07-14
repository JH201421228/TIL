import random
# 우리반 학생 전체 명단 리스트 만들기
students = ['강성은','강주원','고유한','김연빈','김지수','황성주','김해인','문지호','박주헌','이수빈','배준형','손종민','신현기','옥세훈','이승집','이준우','이흔오','장현욱','정지헌','정창휘','조혜원','최용훈','최재성','탁윤희',]
# print(student)
# 리스트를 무작위로 섞어주는 라이브러리 사용하기
random.shuffle(students)
# print(student)
# 리스트를 순회해서 학생 이름 출력하기
for index in range(0, len(students), 6):
    for i in range(6):
        if i!=0 and i%3==0:
            print('    ',end=' ')
        print(students[index+i], end=' ')
    print()

# 자리 모양에 맞춰서 출력하기
# 출력 모양 바꾸기
# ctrl + alt + 방향키 위, 아래
# ctrl + 왼쪽, 오른쪽 방향키
# alt + 방향키 | 포커싱 되어 있는 줄 위치 이동
