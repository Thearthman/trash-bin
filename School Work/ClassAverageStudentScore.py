import numpy as np

desired_mean = 85
mean = 75
sd = 20

marks_list = np.random.normal(mean, sd, size=(20, 30))
current_mean = np.mean(marks_list)
scaling_factor = desired_mean / current_mean
scaled_marks_list = np.clip((marks_list - current_mean) * scaling_factor + desired_mean, 0, 100).astype(int)
new_mean = np.mean(scaled_marks_list)
all_marks = [mark for marks in scaled_marks_list for mark in marks]

highest = max(all_marks)
lowest = min(all_marks)
average = sum(all_marks) / len(all_marks)
print("Highest marks awarded in the class: {}".format(highest))
print("Lowest marks awarded in the class: {}".format(lowest))
print("Average marks awarded in the class: {:.2f}".format(average))

for i in range(20):
    student_marks = scaled_marks_list[i]
    highest = max(student_marks)
    lowest = min(student_marks)
    average = sum(student_marks) / len(student_marks)
    print("For student {},  highest marks awarded: {}, lowest marks awarded: {}, "
          "average marks awarded: {:.2f}".format(i + 1, highest, lowest, average))

for j in range(6):
    subject_marks = [scaled_marks_list[i][j * 5:j * 5 + 5] for i in range(20)]
    all_marks = [mark for marks in subject_marks for mark in marks]
    highest = max(all_marks)
    lowest = min(all_marks)
    average = sum(all_marks) / len(all_marks)
    print("For subject {}, highest marks awarded: {}, lowest marks awarded: {}, "
          "average marks awarded: {:.2f}".format(j + 1, highest, lowest, average))
