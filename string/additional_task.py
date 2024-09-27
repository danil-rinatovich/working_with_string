grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

li_ = list(students)
sorted_list = sorted(li_)
students_average_score = {}
size_list = len(grades)
size_set = len(sorted_list)
print(f"{size_set}, {size_list}")

first_student = float(sum(grades[0]) / len(grades[0]))
second_student = float(sum(grades[1]) / len(grades[1]))
third_student = float(sum(grades[2]) / len(grades[2]))
fourth_student = float(sum(grades[3]) / len(grades[3]))
fifth_student = float(sum(grades[4]) / len(grades[4]))

students_average_score.update({sorted_list[0]: first_student,
                               sorted_list[1]: second_student,
                               sorted_list[2]: third_student,
                               sorted_list[3]: fourth_student,
                               sorted_list[4]: fifth_student})
print(students_average_score)

