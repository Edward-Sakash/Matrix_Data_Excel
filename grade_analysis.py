import openpyxl
import numpy as np

# Load the Excel file
file_path = 'grades.xlsx'
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Get the headers (subject names)
subject_names = [cell.value for cell in sheet[1][1:]]

# Get the student names and grades
data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    student_name = row[0]
    grades = row[1:]
    data.append((student_name, grades))

# Calculate mean grades using numpy
mean_grades = []
for student_data in data:
    student_name = student_data[0]
    grades = student_data[1]
    mean_grade = np.mean(grades)
    mean_grades.append((student_name, mean_grade))

# Print the results
for student_name, mean_grade in mean_grades:
    print(f"Name: {student_name}, Mean Grade: {mean_grade}")
