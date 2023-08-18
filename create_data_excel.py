import openpyxl

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add column headers
sheet['A1'] = 'Name'
sheet['B1'] = 'Math'
sheet['C1'] = 'Science'

# Add data rows
data = [
    ('Alice', 85, 90),
    ('Bob', 70, 75),
    ('Charlie', 95, 88),
    ('David', 78, 82)
]

for row_data in data:
    sheet.append(row_data)

# Save the workbook
file_path = 'data.xlsx'
workbook.save(file_path)

print(f"Excel file '{file_path}' created successfully.")
