# Create a new text file named "student_records.txt" with the following initial content:
# Student ID | Student Name | Grade
# 101       | Alice        | A
# 102       | Bob          | B
# 103       | Carol        | C

# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

# Solution :

f = open("student_records.txt", "r")
data = f.readline()
while data:
    print(data)
    data = f.readline()
f.close()