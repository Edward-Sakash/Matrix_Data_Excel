# Exercise1:  Spreadsheet Data Manipulation with openpyxl
1. Install the `openpyxl` library if you haven't already: `pip install openpyxl`.
2. create the `data.xlsx` file
**data.xlsx:**
|   Name   |  Math  | Science |
|:--------:|:------:|:-------:|
|  Alice   |   85   |   90    |
|   Bob    |   70   |   75    |
| Charlie  |   95   |   88    |
|  David   |   78   |   82    |
3. The Excel file contains three columns: "Name", "Math", and "Science". Your task is to calculate the average score for each student across the two subjects.
Calculate the average scores using `openpyxl` and write the results in a new column called "Average".
4. Save your script in a file named `excel_processing.py`.
5. Run the script and verify that the average scores have been calculated and written correctly.
After running the script, the `data.xlsx` file should be modified as follows:
|   Name   |  Math  | Science | Average |
|:--------:|:------:|:-------:|:-------:|
|  Alice   |   85   |   90    |   87.5  |
|   Bob    |   70   |   75    |   72.5  |
| Charlie  |   95   |   88    |   91.5  |
|  David   |   78   |   82    |   80.0  |

# Exercise 2:
*Task:*
1. save the Excel file named grades.xlsx
2. The Excel file contains student grades for three subjects: "Math", "Science", and "English". Your task is to calculate the mean grade for each student across the three subjects.
3. Calculate the mean grades using openpyxl and numpy, and store the results in a NumPy array.
4. Print the student names along with their calculated mean grades.
*Instructions:*
1. Install the openpyxl and numpy libraries if you haven't already: pip install openpyxl numpy.
2. create the grades.xlsx file
3. The Excel file contains student grades for three subjects: "Math", "Science", and "English". Your task is to calculate the mean grade for each student across the three subjects.
Calculate the mean grades using openpyxl and numpy, and store the results in a NumPy array.
Print the student names along with their calculated mean grades.
4. Save your script in a file named grade_analysis.py.
5. Run the script and verify that the mean grades are calculated correctly.
*grades.xlsx:*
|   Name   |  Math  | Science | English |
|:--------:|:------:|:-------:|:-------:|
|  Alice   |   85   |   90    |   78    |
|   Bob    |   70   |   75    |   85    |
| Charlie  |   95   |   88    |   92    |
|  David   |   78   |   82    |   80    |
*Expected Output:*
After running the script, the output should look like this:
Name: Alice, Mean Grade: 84.33333333333333
Name: Bob, Mean Grade: 76.66666666666667
Name: Charlie, Mean Grade: 91.66666666666667
Name: David, Mean Grade: 80.0