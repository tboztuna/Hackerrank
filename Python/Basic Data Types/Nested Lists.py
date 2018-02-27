match_list = []
student_list = []
num_to_match = 0

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    student_list.append([name, score])

student_list.sort(key=lambda x: float(x[1]))
min_number = min(student_list, key=lambda x: float(x[1]))[1]

for i in range(len(student_list)):
    if student_list[i][1] > min_number:
        num_to_match = student_list[i][1]
        break

for j in range(len(student_list)):
    if student_list[j][1] == num_to_match:
        match_list.append(student_list[j][0])

match_list.sort()
print "\n".join(match_list)