#first class activity
fruits = ["banana", "avocado", "mango", "apple", "berries"]
print(fruits[0])
print(fruits[4])
item = input("enter name of the fruit:")
fruits.append(item)
for i in fruits:
   print(f"{i} has index {fruits.index(i)}")
#second class activity
student_grades = {'kevin': 9.8, 'ishami': 9.9, 'kenia': 10}
print(student_grades["kevin"])
student_grades["Bior"] = 9.8
for student, grade in student_grades.items():
   print(f"{student} has grade {grade}")
#working with tupples
student_grade = (10,9,8,9,3,6,2)
print(student_grade[2])