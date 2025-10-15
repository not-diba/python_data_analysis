# dataframe_access_examples.py

import pandas as pd

# -----------------------------------------------------------
# CREATE A SIMPLE DATAFRAME
# -----------------------------------------------------------

# Data as a dictionary
data = {"Age": [25, 30], "Income": [55000, 65000], "Expenditure": [30000, 45000]}

# Create a DataFrame with named rows (Alice and Bob)
df = pd.DataFrame(data, index=["Alice", "Bob"])

print("=== DataFrame ===")
print(df)
print("\n")

# -----------------------------------------------------------
# ACCESSING ROWS
# -----------------------------------------------------------

# 1. Selecting rows using .loc (Label-based selection)
print("1️⃣ Selecting rows using .loc[] (label-based):")
print("df.loc['Alice'] -> Select the row labeled 'Alice'")
print(df.loc["Alice"])
print("\n")

# 2. Selecting rows using .iloc (Integer-location based selection)
print("2️⃣ Selecting rows using .iloc[] (integer-based):")
print("df.iloc[0] -> Select the first row (index 0)")
print(df.iloc[0])
print("\n")

# -----------------------------------------------------------
# ACCESSING COLUMNS
# -----------------------------------------------------------

# 3. Selecting columns using .loc
print("3️⃣ Selecting columns using .loc[]:")
print("df.loc[:, 'Income'] -> Select all rows for the 'Income' column")
print(df.loc[:, "Income"])
print("\n")

# 4. Selecting columns using .iloc
print("4️⃣ Selecting columns using .iloc[]:")
print("df.iloc[:, 1] -> Select all rows for the column at position 1 (Income)")
print(df.iloc[:, 1])
print("\n")

# -----------------------------------------------------------
# RANGE SELECTION (SLICING)
# -----------------------------------------------------------

# 5. Range selection using .loc (label range)
print("5️⃣ Range selection using .loc[] (label range):")
print(
    "df.loc['Alice', 'Income':'Expenditure'] -> Select 'Income' through 'Expenditure' for 'Alice'"
)
print(df.loc["Alice", "Income":"Expenditure"])
print("\n")

# 6. Range selection using .iloc (integer range)
print("6️⃣ Range selection using .iloc[] (integer range):")
print("df.iloc[0, 1:3] -> Select row 0 and columns from index 1 to 2 (3 is exclusive)")
print(df.iloc[0, 1:3])
print("\n")

# -----------------------------------------------------------
# EXTRA EXAMPLES: MULTIPLE ROWS OR COLUMNS
# -----------------------------------------------------------

# Selecting multiple rows
print("7️⃣ Selecting multiple rows:")
print("df.loc[['Alice', 'Bob']] -> Select rows for both Alice and Bob")
print(df.loc[["Alice", "Bob"]])
print("\n")

# Selecting multiple columns
print("8️⃣ Selecting multiple columns:")
print(
    "df.loc[:, ['Income', 'Expenditure']] -> Select only 'Income' and 'Expenditure' columns"
)
print(df.loc[:, ["Income", "Expenditure"]])
print("\n")

# -----------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------

print("✅ SUMMARY:")
print(".loc[] → Label-based (uses names for rows and columns)")
print(".iloc[] → Index-based (uses numerical positions)")
print("\n")

# -----------------------------------------------------------
# 🔹 DATA CLEANING AND TRANSFORMATION (FILTERING)
# -----------------------------------------------------------

# Let's extend our dataframe with more rows for filtering examples
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [28, 32, 35, 29, 31],
    'Income': [45000, 52000, 59000, 48000, 51000],
    'Expenditure': [30000, 46000, 50000, 32000, 40000]
}

df2 = pd.DataFrame(data2)

print("=== Extended DataFrame for Filtering ===")
print(df2)
print("\n")

# 1️⃣ Filtering rows by condition
print("1️⃣ Filtering rows where Age > 30:")
print("df2[df2['Age'] > 30]")
filtered_age = df2[df2['Age'] > 30]
print(filtered_age)
print("\n")

# 2️⃣ Selecting specific columns
print("2️⃣ Selecting specific columns (Name and Income):")
print("df2[['Name', 'Income']]")
selected_columns = df2[['Name', 'Income']]
print(selected_columns)
print("\n")

# 3️⃣ Using query() method
print("3️⃣ Filtering using the query() method:")
print('df2.query(\"Age > 30 & Income > 50000\")')
filtered_query = df2.query("Age > 30 & Income > 50000")
print(filtered_query)
print("\n")

# -----------------------------------------------------------
# ✅ FILTERING SUMMARY
# -----------------------------------------------------------

print("✅ SUMMARY (Filtering Data):")
print("1. Filter rows by condition → df[df['column'] condition]")
print("2. Select specific columns → df[['col1', 'col2']]")
print('3. Use query method → df.query(\"condition\")')
print("\n")

# -----------------------------------------------------------
# 🔸 RESHAPING DATA: WIDE TO LONG USING pd.melt()
# -----------------------------------------------------------

print("🔸 WIDE TO LONG FORMAT USING pd.melt()")

# Suppose we have a dataframe where each column after 'Name' represents a different year of income
wide_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Income_2023': [50000, 60000, 65000],
    'Income_2024': [52000, 63000, 68000],
    'Income_2025': [54000, 65000, 70000]
})

print("=== Wide DataFrame (Before Melt) ===")
print(wide_df)
print("\n")

# Use pd.melt() to convert from wide to long format
long_df = pd.melt(
    wide_df,
    id_vars=['Name'],               # columns to keep as identifier variables
    var_name='Year',                # name of the new "variable" column
    value_name='Income'             # name of the new "value" column
)

print("=== Long DataFrame (After Melt) ===")
print(long_df)
print("\n")

# Cleaning the 'Year' column to extract just the year (optional step)
long_df['Year'] = long_df['Year'].str.replace('Income_', '', regex=False)
print("=== Long DataFrame (Cleaned Year Column) ===")
print(long_df)
print("\n")

# -----------------------------------------------------------
# ✅ MELT SUMMARY
# -----------------------------------------------------------

print("✅ SUMMARY (pd.melt):")
print("pd.melt() converts wide-form data (many columns) into long-form data (fewer columns).")
print("It's especially useful for plotting or analysis tools that expect data in long format.")
print("\nExample:")
print("pd.melt(wide_df, id_vars=['Name'], var_name='Year', value_name='Income')")
print("\n")

# -----------------------------------------------------
# Example: Using pd.pivot() to convert Long → Wide
# -----------------------------------------------------

# Long format DataFrame
df_long = pd.DataFrame({
    "Name": ["Alice", "Alice", "Bob", "Bob", "Charlie", "Charlie"],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science"],
    "Score": [85, 80, 90, 88, 95, 92]
})

print("\n=== Long Format ===")
print(df_long)

# Pivot (Long → Wide)
df_wide = df_long.pivot(index="Name", columns="Subject", values="Score").reset_index()

print("\n=== Wide Format (after pd.pivot) ===")
print(df_wide)
print("\n")

# -----------------------------------------------------------
# 🔹 DATA AGGREGATION: Combining Multiple DataFrames
# -----------------------------------------------------------


print("\n🔹 DATA AGGREGATION EXAMPLES\n")

# -----------------------------------------------------------
# SAMPLE DATA
# -----------------------------------------------------------

employees = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'DepartmentID': [10, 20, 10, 30]
})

departments = pd.DataFrame({
    'DepartmentID': [10, 20, 40],
    'DepartmentName': ['HR', 'Finance', 'IT']
})

salaries = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 5],
    'Salary': [50000, 60000, 55000, 45000]
})

print("=== Employees DataFrame ===")
print(employees)
print("\n=== Departments DataFrame ===")
print(departments)
print("\n=== Salaries DataFrame ===")
print(salaries)
print("\n")

# -----------------------------------------------------------
# 🔸 .merge() — Combining DataFrames on Common Columns
# -----------------------------------------------------------

print("🔸 Using .merge() — combine DataFrames using a common key")

merged_df = employees.merge(salaries, on='EmployeeID', how='left')
print("\nMerged employees with salaries (based on EmployeeID):")
print(merged_df)

# -----------------------------------------------------------
# 🔸 .concat() — Combine DataFrames vertically or horizontally
# -----------------------------------------------------------

print("\n🔸 Using .concat() — stack DataFrames vertically or side-by-side")

# Vertical concatenation (stacking rows)
dept_extra = pd.DataFrame({
    'DepartmentID': [50],
    'DepartmentName': ['Operations']
})

concat_vertical = pd.concat([departments, dept_extra], ignore_index=True)
print("\nVertical Concatenation (adding new department):")
print(concat_vertical)

# Horizontal concatenation (side-by-side)
concat_horizontal = pd.concat([employees, salaries['Salary']], axis=1)
print("\nHorizontal Concatenation (side-by-side):")
print(concat_horizontal)

# -----------------------------------------------------------
# 🔸 .join() — Combine DataFrames using their index
# -----------------------------------------------------------

print("\n🔸 Using .join() — join DataFrames based on index")

# Set EmployeeID as index for joining
employees_indexed = employees.set_index('EmployeeID')
salaries_indexed = salaries.set_index('EmployeeID')

joined_df = employees_indexed.join(salaries_indexed, how='left')
print("\nJoined DataFrame (based on EmployeeID index):")
print(joined_df)

# -----------------------------------------------------------
# 🔸 Types of Joins — INNER, OUTER, LEFT, RIGHT
# -----------------------------------------------------------

print("\n🔸 Types of Join Operations (using .merge())")

# INNER JOIN → only rows with matching DepartmentID in both DataFrames
inner_join = employees.merge(departments, on='DepartmentID', how='inner')
print("\n1️⃣ INNER JOIN (only matching rows):")
print(inner_join)

# OUTER JOIN → all rows from both DataFrames
outer_join = employees.merge(departments, on='DepartmentID', how='outer')
print("\n2️⃣ OUTER JOIN (all rows, unmatched filled with NaN):")
print(outer_join)

# LEFT JOIN → all employees, matching departments if available
left_join = employees.merge(departments, on='DepartmentID', how='left')
print("\n3️⃣ LEFT JOIN (all from left, match from right):")
print(left_join)

# RIGHT JOIN → all departments, matching employees if available
right_join = employees.merge(departments, on='DepartmentID', how='right')
print("\n4️⃣ RIGHT JOIN (all from right, match from left):")
print(right_join)

# -----------------------------------------------------------
# ✅ SUMMARY
# -----------------------------------------------------------

print("\n✅ SUMMARY (Data Aggregation):")
print(".merge() → Combines DataFrames using common columns or keys")
print(".concat() → Stacks DataFrames vertically (rows) or horizontally (columns)")
print(".join() → Combines DataFrames using their index")

print("\nTypes of Joins:")
print(" - Inner Join → only matching rows")
print(" - Outer Join → all rows, unmatched = NaN")
print(" - Left Join → all from left, match from right")
print(" - Right Join → all from right, match from left")
print("\n")

# -----------------------------------------------------------
# 🔹 DATA AGGREGATION (Grouping and Aggregation)
# -----------------------------------------------------------


print("\n🔹 GROUPING AND AGGREGATION EXAMPLES\n")

# -----------------------------------------------------------
# SAMPLE DATA
# -----------------------------------------------------------

sales = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Revenue': [1200, 700, 1100, 900, 1500, 800, 1300, 950],
    'Units_Sold': [5, 3, 4, 2, 6, 3, 5, 2]
})

print("=== Sales Data ===")
print(sales)
print("\n")

# -----------------------------------------------------------
# 🔸 .groupby() — Group data by one or more columns
# -----------------------------------------------------------

print("🔸 Using .groupby() — group data by Region")

grouped = sales.groupby('Region')
print("\nGrouped by 'Region': (printing groups)")
for name, group in grouped:
    print(f"\nRegion: {name}")
    print(group)

# -----------------------------------------------------------
# 🔸 .agg() — Perform multiple aggregations on grouped data
# -----------------------------------------------------------

print("\n🔸 Using .agg() — apply multiple aggregations to grouped data")

aggregated = sales.groupby('Region').agg({
    'Revenue': ['sum', 'mean', 'max'],      # total, average, and max revenue per region
    'Units_Sold': ['sum', 'mean']           # total and average units sold per region
})

print("\nAggregated Results (by Region):")
print(aggregated)

# -----------------------------------------------------------
# 🔸 Combine .groupby() and aggregation in one line
# -----------------------------------------------------------

print("\n🔸 Group by multiple columns and calculate total revenue")

multi_group = sales.groupby(['Region', 'Salesperson'])['Revenue'].sum().reset_index()
print("\nTotal Revenue by Region and Salesperson:")
print(multi_group)

# -----------------------------------------------------------
# ✅ SUMMARY
# -----------------------------------------------------------

print("\n✅ SUMMARY (Grouping & Aggregation):")
print(".groupby() → Groups data based on one or more keys")
print(".agg() → Applies one or more aggregate functions (sum, mean, max, etc.) to grouped data")
print("\nCommon aggregate functions: sum(), mean(), max(), min(), count(), median(), std()")
