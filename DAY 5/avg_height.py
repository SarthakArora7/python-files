# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
count = 0
for i in student_heights:
  sum = sum + i
  count = count + 1

avg_height = round(sum/count)

print(f"The average height of students is {avg_height}")
