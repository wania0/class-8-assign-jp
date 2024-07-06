# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

# Solution :

f = open("updated_records.txt","w")

f = open("student_records.txt", "r")

f.read