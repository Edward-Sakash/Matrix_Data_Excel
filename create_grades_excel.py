import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add column headers
sheet['A1'] = 'Name'
sheet['B1'] = 'Math'
sheet['C1'] = 'Science'
sheet['D1'] = 'English'

# Add data rows
data = [
    ('Alice', 85, 90, 78),
    ('Bob', 70, 75, 85),
    ('Charlie', 95, 88, 92),
    ('David', 78, 82, 80)
]

for row_data in data:
    sheet.append(row_data)

# Save the workbook
file_path = 'grades.xlsx'
workbook.save(file_path)

print(f"Excel file '{file_path}' created successfully.")
