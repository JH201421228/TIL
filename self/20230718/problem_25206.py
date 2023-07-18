

subject_num = 20

total_score = 0
subject_score = 0
score = ['D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
info_subject = []

for j in range(subject_num):
    info_subject.append(str(input()))
    length = len(info_subject[j])

    if info_subject[j][-1] == 'F':
        subject_score += int(info_subject[j][-5])

    elif info_subject[j][-1] == 'P':
        pass

    else:
        for i in range(8):
        
            if score[i] == info_subject[j][length-2:length]:
                score = int(info_subject[j][-6])
                total_score += ((i + 2) / 2) * score
                subject_score += score

print(total_score / subject_score)

# test = 'ObjectOrientedProgramming1 3.0 A+'
# print(test[len(test)-2:len(test)] == score[-1])

# for i in range(8):
#     print(score[i])