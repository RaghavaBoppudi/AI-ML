# Install the main packages:
# python -m pip install numpy pandas matplotlib

# Optional charts:
# python -m pip install seaborn plotly cufflinks folium geopandas

# Run with: python Python_From_Zero_Pandas_Visualization_Tutorial.py
# This file makes illustrative data; you do NOT need the Titanic CSV, the Iris internet download, or the London shapefile from your notebooks.
# For chart examples, set RUN_CHARTS = True below. Charts are saved in a folder named python_tutorial_charts next to where you run this script.
# Plotly charts become interactive HTML pages you can open in a browser.
# The topic order follows concepts demonstrated in your FOUR notebooks:
#     Pandas data manipulation (both parts), Pandas visualization, and Plotly and Cufflinks. We also add prerequisite Python fundamentals.

RUN_CHARTS = False  # Change False to True when you are ready to make charts.


def heading(name):
    # def creates a reusable function. This one prints a readable heading.
    print("\n" + "=" * 76)
    print(name)
    print("=" * 76)


# LESSON 1: WHAT IS A MODULE?.

# A MODULE is a Python file containing reusable code (functions, variables, and sometimes classes). Think of it as a toolbox that somebody packaged.

# A PACKAGE groups related modules together, usually inside a folder.

# A LIBRARY is a broad term for reusable code; it may contain many packages.

# IMPORT means "make another module's tools available in THIS file."

# Example: The built-in math module gives us square-root and circle tools. The dot in math.sqrt means "find sqrt INSIDE the math module." print() displays information. It is NOT the same as returning a value.

# 1. MODULES, PACKAGES, AND IMPORTS
import math # importing the math module
print("Square root of 25:", math.sqrt(25))  # Using the sqrt inside the math module
print("Value of pi:", math.pi)  # Using the sqrt inside the math module. Pi is a predefined constant in math.

# "as" creates a SHORT NAME (alias). This does not copy the module.
import math as m
print("2 raised to power 3:", m.pow(2, 3))  # .pow is raised to the power.


# while import imports the entire thing, we can bring into context just what we need.
# "from ... import ..." brings in JUST the named item.
from math import ceil # bring just the ceil function
print("Round 4.2 UP to the next integer:", ceil(4.2))  # Prints the upper ceiling of a number - 4.1 also prints 5.0

# Standard library: tools installed along with Python (e.g., math, os, json).

# Third-party library: tools installed separately (e.g., pandas, NumPy).

# pip: tool that INSTALLS packages; import: tool that USES installed packages.

# "pip install pandas" belongs in a TERMINAL, never as plain Python code.

# Notebook commands like !pip install and %matplotlib inline are IPython-only
# conveniences and are NOT valid in a normal .py file.

import os # os helps with operating-system paths
import json # json helps read/write JSON data
print("Operating-system path separator:", os.sep) # prints out the path separator in OS directories - / on mac (~/Desktop/...)
print("JSON example:", json.dumps({"course": "Python", "level": 1})) # json.dumps converts a python object into a JSON-formatted string

# 2: VARIABLES AND DATA TYPES

# Variable = a NAME pointing to a value, like a labeled storage box.

# The = sign means ASSIGNMENT, not "mathematically equals."

# int = whole number; float = decimal number; str = text; bool = True/False.

# Python indexing (positions) starts at ZERO, not ONE.

age = 25
price = 12.5
person = "Sam" # Strings use quotation marks. "25" is text, but 25 is a number.
is_student = True
missing_answer = None

print(age, type(age)) # type(value) tells you the type of an object.
print(price, type(price))
print(person, type(person))
print(is_student, type(is_student))
print(missing_answer, type(missing_answer))
print("Convert text to integer:", int("25") + 5) # "25" is usually a string. Wrap it in int to convert it to an integer
print("Convert integer to text:", "Age: " + str(age)) # age is usually a number (int). Wrap it in str it to a string

# Operators: + add; - subtract; * multiply; / divide into a float.
# // floor division; % remainder; ** exponent (power).

print("7 / 2:", 7 / 2)  # 3.5
print("7 // 2:", 7 // 2)  # prints out the quotient rounded-down - 3 in this case
print("7 % 2:", 7 % 2)  # prints out the remainder - 1 in this case
print("2 ** 3:", 2 ** 3)  # 2 raised to the power 3

# 3: LISTS, DICTIONARIES, TUPLES, AND SLICING

# LIST []: an ordered, changeable sequence of values.

# DICTIONARY {}: "key -> value" pairs, like a word and its definition.

# TUPLE (): ordered sequence that cannot be changed after creation.

# SLICING [start:stop:step]: select positions start THROUGH stop-1.

# Negative index -1 means the LAST element.

# List multiplication repeats the LIST; NumPy array multiplication does math.

colors = ["red", "blue", "green", "yellow"]
print("First color:", colors[0]) # returns the value at first index
print("Last color:", colors[-1]) # returns the value at the last index
print("Positions 1 and 2:", colors[1:3])  # Upper limit is non inclusive - Stop 3 not included.
print("Every other color:", colors[0:4:2]) # prints colors from zeroth index to 3rd index in steps of 2

colors.append("purple")  # append adds one item at the end.

print("Updated list:", colors)

# List multiplication - prints out the list as many times as needed
print("List repetition:", [10, 20] * 2)  # Prints the list twice over - [10, 20, 10, 20]

profile = {"name": "Amy", "score": 90}
print("Get value under 'score':", profile["score"])

# Modifying the value at a specific index
profile["score"] = 95  # Change the value at key 'score'.

print("Dictionary items:", list(profile.items())) # prints the items as a list

coordinates = (10, 20)
print("A tuple:", coordinates)

# LESSON 4: COMPARISONS, CONDITIONS, LOOPS, FUNCTIONS, AND LAMBDAS

# == asks "are these equal?"  It is different from assignment (=).
# > greater than; < less than; >= at least; != not equal.
# and requires BOTH conditions; or requires AT LEAST ONE.
# if/elif/else chooses which code to run.
# for loops repeat code once for each item in a sequence.
# def creates a function. return sends a result back to its caller.
# lambda creates a SMALL unnamed function, handy for Pandas .apply().

score = 72
if score >= 90:
    print("Grade: A")
elif score >= 60:
    print("Grade: pass")
else:
    print("Grade: needs improvement")
for fruit in ["apple", "banana", "orange"]:
    print("Fruit:", fruit)

# define a function to print twice the supplied number

def double(number):
    # Input parameter = number. Output = twice the supplied number.
    return number * 2

print("Function result:", double(7)) # prints 14

# Lambda function - anonymous function - used when you don't need the function saved but need a throwaway function

# It can take any number of arguments, evaluates a single expression, and automatically returns the result without needing a return statement

# lambda arguments: expression

triple = lambda number: number * 3 # takes a number as the argument and returns the number multiplied by 3

print("Lambda result:", triple(7)) # prints 21

# use proper def to define a function if you need to reuse it.
# def triple(number):
#     return number * 3

print("Length of text:", len("Python"))  # 6 characters.
print("Split a string:", "CA NV AZ".split())  # List of three words.

# 5: NUMPY -- WHY PANDAS OFTEN USES IT

# NumPy is a third-party package for handling arrays and numerical calculations.

# An array resembles a list, but is designed for efficient number operations.

# np.nan = a missing numerical value (NaN stands for "Not a Number").

# In Pandas, missing data can also be represented with None or pd.NA.

# An operation on an array usually applies to EACH number independently.
# seed fixes the random generator so examples are repeatable.

# Python dependency check for installed libraries
try:
    import numpy as np
    import pandas as pd

# If either library is missing, Python catches the ImportError and stores the error details in a variable named exc
except ImportError as exc: 
    raise SystemExit(
        "Install dependencies first: python -m pip install numpy pandas matplotlib"
    ) from exc

# Create a 1D NumPy array
numbers = np.array([10, 20, 30])

print("NumPy array:", numbers)
print("Array times two:", numbers * 2)  
# Notice how when we did the same with list earlier, it repeated the list twice over? 
# But here with NumPy arrays, each element is multiplied - [20 40 60], not repeated.

# .mean calculates the mean of the values - (10+20+30)/3 = 20.
print("Array mean:", numbers.mean())

# .shape returns a tuple of integers showing the number of elements along each dimension.
print("Array shape:", numbers.shape)  # (3,) = one dimension, 3 entries since it is a 1D array.

# .nan is a placeholder for missing, null, or invalid numerical data in NumPy arrays and Pandas DataFrames
print("Missing-value marker:", np.nan)

# np.random.seed locks NumPy's random number generator so that it produces the exact same sequence of "random" numbers every time you run your code
np.random.seed(101)

# .randn creates an array of random values
print("Three random values:", np.random.randn(3))

# 6: WHAT ARE PANDAS, SERIES, DATAFRAMES, INDEXES?

# Pandas is a library for working with TABULAR data (think Excel worksheets).

# Series = ONE labeled column of data. It has VALUES and an INDEX (labels).

# DataFrame = a 2-D table: rows AND columns. Many Series side by side.

# INDEX = row labels. COLUMNS = column labels.
# The index is NOT automatically the same thing as the first visible column.

# pd is the customary alias for pandas. np is the alias for numpy.

# pd.Series(data, index=labels) makes a labeled 1-D sequence.

# pd.DataFrame(dictionary) makes a table where keys become column headers.

# creates a 1d pandas sequence with the below info at below indexes

series = pd.Series([10, 20, 30], index=["a", "b", "c"])

print("Series:\n", series)

#.loc is label lookup - 
print("Series value with label 'b':", series.loc["b"])

#.iloc is integer position lookup - NOT index lookup
print("Series second value by position:", series.iloc[1])

# Create a 4-row, 3-column pandas DataFrame
students = pd.DataFrame({
    "Name": ["Amy", "Ben", "Cara", "Dan"],
    "Age": [20, 22, 21, 23],
    "Score": [90, 75, 88, 75],
})

print("DataFrame:\n", students)
print("Rows x columns:", students.shape)  # (4, 3)
print("Column names:", students.columns.tolist())
print("Index values:", students.index.tolist())
print("Data types:\n", students.dtypes)

# 7: LOOK AT DATA BEFORE CHANGING IT

# mean = average; std = standard deviation (how spread out values are).
# Sorting a Series differs from selecting data by slices; both are possible.

# head(n) shows first n rows
print("First 2 rows:\n", students.head(2))

# tail(n) shows last n rows.
print("Last 2 rows:\n", students.tail(2))

# describe() summarizes numeric columns: count, mean, std, min, quartiles, max.
print("Numeric summary:\n", students.describe())

# value_counts() counts how often each unique value appears.
print("Counts of each Score:\n", students["Score"].value_counts())

# unique() gives distinct values
print("Unique scores:", students["Score"].unique())

# nunique() gives NUMBER of distinct values.
print("Number of unique scores:", students["Score"].nunique())

# dtypes = type of EACH column; columns = headers; index = row labels.
print("Object/text columns:\n", students.select_dtypes(include="object"))

print("Basic metadata:")
# info() explains count, data type, and missing values for columns.
students.info()

# 8: READ AND WRITE CSV FILES

# CSV = Comma-Separated Values: a common way to store a table as text.

# pd.read_csv(path) loads a file into a DataFrame.
# df.to_csv(path, index=False) saves table without adding row numbers as a separate extra column. Use a path that exists on YOUR computer.

# 8. CSV AND SAMPLE TITANIC-LIKE DATA
# Creating a sample DataFrame

titanic = pd.DataFrame({
    "Name": ["Ava", "Ben", "Cleo", "Dion", "Ella", "Finn"],
    "Sex": ["female", "male", "female", "male", "female", "male"],
    "Age": [24, np.nan, 35, 17, 29, 40],
    "Pclass": [1, 3, 2, 3, 1, 2],
    "Fare": [95.0, 8.5, 20.0, 7.0, 120.0, 18.0],
    "Ticket": ["A1", "B2", "C3", "D4", "E5", "F6"],
    "Cabin": ["C12", None, "B2", None, "A11", "D3"],
    "SibSp": [1, 0, 1, 0, 0, 2],
    "Parch": [0, 0, 1, 0, 0, 1],
    "Survived": [1, 0, 1, 0, 1, 0],
})
print("Practice data:\n", titanic)

# Uncomment these TWO lines if you want to practice with a real saved CSV:
# titanic.to_csv("my_titanic_practice.csv", index=False)
# titanic_from_csv = pd.read_csv("my_titanic_practice.csv")

# 9: PICK COLUMNS, ROWS, AND INDIVIDUAL CELLS

# Avoid ambiguous chained selection when assigning; use .loc instead.

# df['Name'] = return a 1D pandas Series - one column with its index.
print("Single column:\n", titanic["Name"])

# df[['Name', 'Age']] = Double brackets pass a list of column names, returning a 2D DataFrame.
print("Several columns:\n", titanic[["Name", "Age", "Fare"]])

# .iloc uses INTEGER POSITIONS (0-based numbered places).
print("First row by position:\n", titanic.iloc[0])

# .iloc[start:stop] excludes the stop position like normal Python slicing.
print("First three rows:\n", titanic.iloc[0:3])

print("One cell by position:", titanic.iloc[0, 1])

# .loc uses LABELS (row names / column names).
# df.loc[row, column] selects one cell, one slice, or a block.
print("One cell by labels:", titanic.loc[0, "Name"])

# .loc[start:stop] includes BOTH endpoints when labels are sortable slices.
print("Rows 1 and 3, selected columns:\n", titanic.loc[[1, 3], ["Name", "Fare"]])

# First grabs the "Ticket" Series, then slices positions 0 up to 6 (excluding 6) with a step of 2—returning positions 0, 2, and 4
print("Every second Ticket between positions 0 and 5:\n", titanic["Ticket"].iloc[0:6:2])

# 10: FILTERING (BOOLEAN MASKS)

# A Boolean mask is a list/Series of True/False values, one per row.
# df['Age'] > 25 asks the question FOR EVERY ROW.
# df[mask] keeps ONLY rows whose mask result is True.
# For Pandas masks, use & for AND and | for OR, not Python 'and'/'or'.
# Parentheses around EACH condition help Python evaluate correctly.
# .isin([...]) checks membership in a list of values.
# .notna() is True for available values; .isna() for missing ones.

print("Who paid over 20?\n", titanic[titanic["Fare"] > 20])
print("Female passengers in class 1:\n", titanic[(titanic["Sex"] == "female") & (titanic["Pclass"] == 1)])
print("Under 20 OR over 35:\n", titanic[(titanic["Age"] < 20) | (titanic["Age"] > 35)])
print("Classes 1 or 2:\n", titanic[titanic["Pclass"].isin([1, 2])])
print("Fare of highest-paying passenger:\n", titanic.loc[titanic["Fare"].idxmax()])

# 11: CREATE, CHANGE, REMOVE, AND SORT COLUMNS/ROWS

# df['new_name'] = values makes a NEW column if that name doesn't exist.
# If it DOES exist, the assignment overwrites that column.
# Arithmetic on columns is done ROW BY ROW, automatically.
# df.drop(columns=['...']) removes a column; df.drop(index=[...]) removes rows.
# axis=0 refers to ROW index; axis=1 refers to COLUMN names.
# Most Pandas methods return a NEW DataFrame unless you reassign the result.
# inplace=True modifies the existing object in some methods; reassigning the
# result is often easier to read. drop does NOT change df by default.
# sort_values(by='Age') sorts records by a column; ascending=False reverses.

heading("11. ADD, REMOVE, SORT")
titanic["Fare_Double"] = titanic["Fare"] * 2
titanic["Family"] = titanic["SibSp"] + titanic["Parch"]
print("Calculated columns:\n", titanic[["Name", "Fare_Double", "Family"]])
print("Drop column in a NEW result:\n", titanic.drop(columns=["Fare_Double"]).head(2))
print("Original still has the column:", "Fare_Double" in titanic.columns)
print("Sorted by Fare, most expensive first:\n", titanic.sort_values(by="Fare", ascending=False)[["Name", "Fare"]])
print("Original column names:", list(titanic.columns))

# ============================================================================
# LESSON 12: INDEXES, RESET_INDEX, SET_INDEX, CATEGORICAL TYPES
# ============================================================================
# set_index('Name') makes a column become the row labels.
# reset_index() moves row labels back into a normal column.
# reset_index(drop=True) throws away current labels and uses 0,1,2,...
# A category represents values from a known set of groups (e.g., class 1/2/3).
# astype('category') can save memory and makes grouping explicit.
# Important: .set_index() by default creates a NEW DataFrame.

heading("12. INDEXES AND CATEGORIES")
by_name = titanic.set_index("Name")
print("With Name as row index:\n", by_name[["Age", "Fare"]])
print("Lookup by name:\n", by_name.loc["Ava"])
print("Back to normal index:\n", by_name.reset_index().head(2))
print("Fresh numeric index:\n", by_name.reset_index(drop=True).head(2))
titanic["Class_Category"] = titanic["Pclass"].astype("category")
print("Categorical values:\n", titanic["Class_Category"])

# ============================================================================
# LESSON 13: MISSING VALUES (NaN, None, pd.NA)
# ============================================================================
# Real datasets often have empty cells. This is NOT the same as zero.
# NaN = common numeric missing marker; None = Python's empty-value marker.
# isna() / isnull() = "is this missing?" (these are equivalent in Pandas).
# notna() = "does this have a value?"
# dropna() removes rows or columns with missing values, depending on axis.
# axis=0: inspect EACH row; axis=1: inspect EACH column.
# thresh=2: keep a row if it contains AT LEAST TWO nonmissing entries.
# fillna(0): replace missing cells with zero (only if that choice makes sense).
# fillna(mean): use a column's typical number instead of a missing number.
# Important: filling missing age with the mean is an EXAMPLE, not a rule.

heading("13. MISSING VALUES")
missing_df = pd.DataFrame({"A": [1, 2, np.nan],
                           "B": [5, np.nan, np.nan],
                           "C": [1, 2, 3]})
missing_df["States"] = "CA NV AZ".split()
missing_df = missing_df.set_index("States")
print("Original:\n", missing_df)
print("Where values are missing:\n", missing_df.isna())
print("Missing-value count in each column:\n", missing_df.isna().sum())
print("Remove rows with ANY missing value:\n", missing_df.dropna(axis=0))
print("Remove columns with ANY missing value:\n", missing_df.dropna(axis=1))
print("Keep rows with >=2 known values:\n", missing_df.dropna(thresh=2))
print("Replace missing values with zero:\n", missing_df.fillna(0))
print("Fill A with A's average:\n", missing_df.assign(A=missing_df["A"].fillna(missing_df["A"].mean())))
print("Rows with no Age value:\n", titanic[titanic["Age"].isna()])
print("Missing Age count:", titanic["Age"].isna().sum())

# ============================================================================
# LESSON 14: STRING OPERATIONS AND APPLY()
# ============================================================================
# .str gives Pandas string operations for every item in a text column.
# .astype(str) turns values into strings, including missing values, which
# may become text like 'None' or 'nan'. Usually prefer .str operations.
# .apply(function) calls function ONCE per element of a Series.
# lambda x: expression is a brief way to write a function inline.
# len(x) measures length of text; np.log(x) is natural logarithm.
# map() and vectorized .str methods are often simpler/faster than apply().

heading("14. STRING MANIPULATION AND APPLY")
print("Names in lowercase:\n", titanic["Name"].str.lower())
print("First letter of nonmissing cabin values:\n", titanic["Cabin"].str[0])
print("Name length:\n", titanic["Name"].apply(len))
print("Fare log values:\n", titanic["Fare"].apply(lambda x: np.log(x)))
print("Name starts with A?:\n", titanic["Name"].str.startswith("A"))


def transform_number(x):
    # This is based on the custom-function idea in your second Pandas notebook.
    # If a number exceeds 500, transform it with 10*log10(x).
    # Otherwise, divide that number by 10.
    if x > 500:
        return 10 * np.log10(x)
    return x / 10

print("Custom function on 444:", transform_number(444))
print("Custom function on 666:", transform_number(666))

# ============================================================================
# LESSON 15: SERIES ALIGNMENT -- LABELS MATTER
# ============================================================================
# When you add two Pandas Series, Pandas matches the LABELS, not positions.
# A label found in one Series but not the other usually gives NaN.
# This is why index design is so important in data analysis.
# .add(other, fill_value=0) can specify what to use for unmatched entries.

heading("15. SERIES ALIGNMENT")
first = pd.Series({"CA": 10, "NV": 20})
second = pd.Series({"CA": 1, "AZ": 5})
print("Addition matches state labels:\n", first + second)
print("Fill unmatched labels with 0:\n", first.add(second, fill_value=0))

# ============================================================================
# LESSON 16: GROUPBY = SPLIT, CALCULATE, COMBINE
# ============================================================================
# Imagine a pile of sales receipts from many companies.
# groupby('Company') means "put receipts from the same company together."
# Then .sum(), .mean(), .count(), etc. calculate ONE result per group.
# 'mean' is average; 'sum' is total; 'count' counts nonmissing entries.
# 'size' counts rows including ones with missing values in other columns.
# .agg() computes more than one summary for a group in one operation.

heading("16. GROUPBY")
sales = pd.DataFrame({
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350],
})
print("Original sales:\n", sales)
print("Total per company:\n", sales.groupby("Company")["Sales"].sum())
print("Average per company:\n", sales.groupby("Company")["Sales"].mean())
print("Several statistics:\n", sales.groupby("Company")["Sales"].agg(["count", "sum", "mean", "min", "max"]))
print("Stats for FB only:\n", sales.groupby("Company")["Sales"].describe().loc["FB"])

# ============================================================================
# LESSON 17: CONCATENATE = STACK TABLES
# ============================================================================
# pd.concat([df1, df2], axis=0) puts tables ONE UNDER THE OTHER (new rows).
# pd.concat([df1, df2], axis=1) puts tables SIDE BY SIDE (new columns).
# axis=1 lines rows up by INDEX labels, NOT by apparent screen location.
# If labels don't match, Pandas inserts missing values (NaN).
# ignore_index=True creates a new simple row index when stacking vertically.
# Duplicate row indexes may occur with concat(axis=0) if you don't reset.

heading("17. CONCATENATION")
df1 = pd.DataFrame({"A": ["A0", "A1"], "B": ["B0", "B1"]})
df2 = pd.DataFrame({"A": ["A2", "A3"], "B": ["B2", "B3"]})
print("Stack DOWN:\n", pd.concat([df1, df2], axis=0, ignore_index=True))
print("Stack SIDEWAYS:\n", pd.concat([df1, df2], axis=1))

# ============================================================================
# LESSON 18: MERGE = MATCH ROWS USING A SHARED KEY
# ============================================================================
# Merging is similar to matching rows in two Excel worksheets by an ID.
# A KEY is the column whose values indicate which rows belong together.
# INNER merge: keep keys appearing in BOTH tables.
# LEFT merge: keep every row in LEFT; add right matches if they exist.
# RIGHT merge: keep every row in RIGHT; add left matches if they exist.
# OUTER merge: keep keys from EITHER table; unmatched fields become NaN.
# A merge can use ONE key or MULTIPLE keys (on=['key1','key2']).
# Duplicate keys can multiply the number of rows. Inspect your key uniqueness.

heading("18. MERGES: INNER, LEFT, RIGHT, OUTER")
left = pd.DataFrame({"key": ["K0", "K1", "K2"], "A": [10, 20, 30]})
right = pd.DataFrame({"key": ["K0", "K2", "K3"], "B": [100, 300, 400]})
for how in ["inner", "left", "right", "outer"]:
    print(how.upper(), "merge:\n", pd.merge(left, right, on="key", how=how))

left_two = pd.DataFrame({"key1": ["A", "A", "B"],
                         "key2": [1, 2, 1], "Sales": [50, 60, 70]})
right_two = pd.DataFrame({"key1": ["A", "B"],
                          "key2": [2, 1], "Region": ["West", "East"]})
print("Merge using TWO keys:\n", pd.merge(left_two, right_two, on=["key1", "key2"], how="left"))

# ============================================================================
# LESSON 19: JOIN = OFTEN MATCH ON INDEXES
# ============================================================================
# df.join(other) is convenient when row INDEXES are the matching keys.
# join defaults to 'left', meaning keep index labels from the left table.
# how='outer' keeps labels appearing in either table.
# merge is most convenient when the keys are ordinary columns.

heading("19. JOIN ON INDEX")
labeled_left = pd.DataFrame({"Score": [95, 81]}, index=["A", "B"])
labeled_right = pd.DataFrame({"City": ["NY", "LA"]}, index=["A", "C"])
print("LEFT join:\n", labeled_left.join(labeled_right))
print("OUTER join:\n", labeled_left.join(labeled_right, how="outer"))

# ============================================================================
# LESSON 20: MORE STATISTICS, SORTING, AND DIFFERENCES
# ============================================================================
# .sum() = total; .mean() = average; .min()/.max() = extrema.
# .std() = how dispersed the values are around the mean.
# .diff() = CURRENT value MINUS PREVIOUS value.
# .cumsum() = running total; 5, 3, 7 becomes 5, 8, 15.
# sort_index() sorts by labels; sort_values() sorts by contents.
# A DataFrame's .describe() produces numerical summary statistics.

heading("20. STATISTICS, DIFF, CUMSUM")
measurements = pd.Series([5, 3, 7], index=["Day 1", "Day 2", "Day 3"])
print("Running sum:\n", measurements.cumsum())
print("Change since previous day:\n", measurements.diff())
print("Mean:", measurements.mean())
print("Std dev:", measurements.std())
print("Descending values:\n", measurements.sort_values(ascending=False))

# ============================================================================
# LESSON 21: MULTIINDEX -- TWO LEVELS OF ROW LABELS
# ============================================================================
# Normal indexes can say: A, B, C. A MultiIndex can say: (Group, Member).
# For example: (G1,1), (G1,2), (G2,1).
# This is useful when data naturally has subgroups within groups.
# pd.MultiIndex.from_tuples makes that hierarchical list of row labels.
# .loc[('G1', 1)] selects a precise multi-level row.

heading("21. MULTIINDEX")
labels = [("G1", 1), ("G1", 2), ("G2", 1), ("G2", 2)]
multi = pd.MultiIndex.from_tuples(labels, names=["Group", "Member"])
hierarchical = pd.DataFrame({"Score": [80, 85, 90, 95]}, index=multi)
print("MultiIndex DataFrame:\n", hierarchical)
print("All of G1:\n", hierarchical.loc["G1"])
print("One row:\n", hierarchical.loc[("G2", 1)])

# ============================================================================
# LESSON 22: DATES AND TIME SERIES
# ============================================================================
# pd.date_range creates an ordered sequence of calendar dates.
# periods=5 means "give me 5 dates"; freq='D' means one per DAY.
# A TIME SERIES is data collected in time order, e.g., daily temperatures.
# When dates are the index, Pandas graphs dates on the x-axis naturally.

heading("22. DATES AND TIME SERIES")
dates = pd.date_range("2026-01-01", periods=5, freq="D")
temperatures = pd.Series([20, 21, 19, 22, 23], index=dates, name="Temperature")
print("A time series:\n", temperatures)
print("Daily change:\n", temperatures.diff())

# ============================================================================
# LESSON 23: VISUALIZATION -- WHAT CHART SHOULD YOU USE?
# ============================================================================
# Visualization = turning numbers into pictures to see patterns faster.
# LINE plot: trend over time or ordered x values.
# BAR plot: compare values across categories.
# BARH: horizontal bar chart (useful for long category names).
# HISTOGRAM: how often values fall into numeric intervals called 'bins'.
# SCATTER plot: relationship between TWO numeric variables (x and y).
# BOX plot: median, quartiles, and possible outliers of a distribution.
# PIE plot: how parts combine into a whole (ideally few, positive categories).
# AREA plot: quantity over time shown with a filled region.
# HEXBIN plot: hexagonal bins useful for dense scatter data.
# KDE: smoothed estimate of a variable's distribution.
# HEATMAP: values represented by colors (e.g., a numeric matrix).
# SUBPLOTS: multiple small charts rather than one crowded image.
# SECONDARY Y AXIS: displays measures with very different numeric scales.
# LOG Y AXIS: logarithmic y axis; requires POSITIVE values.
# The original notebook uses .plot(), .hist(), scatter_matrix, KDE,
# Andrews curves, and a sample GeoPandas shapefile map.
# Figures from this plain .py script can be saved rather than relying on
# notebook-specific automatic output.

# ============================================================================
# LESSON 24: MATPLOTLIB / PANDAS CHART EXAMPLES
# ============================================================================
# plt is the common alias for matplotlib.pyplot.
# A 'figure' is the overall canvas; 'axes' is an individual plot area.
# plt.close() releases the figure after saving to avoid using extra memory.
# These examples do not depend on seaborn internet datasets.
# When RUN_CHARTS=False, these are skipped to keep the basic lessons quick.

if RUN_CHARTS:
    import matplotlib
    matplotlib.use("Agg")  # Save image files; don't require a graphical screen.
    import matplotlib.pyplot as plt
    from pathlib import Path
    from pandas.plotting import scatter_matrix, andrews_curves

    charts_dir = Path("python_tutorial_charts")
    charts_dir.mkdir(exist_ok=True)

    def save_chart(filename):
        # bbox_inches='tight' avoids cutting labels off around an image.
        plt.tight_layout()
        plt.savefig(charts_dir / filename, dpi=140, bbox_inches="tight")
        plt.close("all")
        print("Saved:", charts_dir / filename)

    heading("24. MATPLOTLIB AND PANDAS CHARTS")

    # LINE: show the temperature on each calendar day.
    temperatures.plot(kind="line", title="Temperature over Time", marker="o")
    plt.ylabel("Degrees")
    save_chart("01_line.png")

    # BAR: compare total sales by company.
    sales.groupby("Company")["Sales"].sum().plot(kind="bar", title="Company Sales")
    plt.ylabel("Total sales")
    save_chart("02_bar.png")

    # BARH: same comparison, bars extending sideways.
    sales.groupby("Company")["Sales"].sum().plot(kind="barh", title="Horizontal Bars")
    save_chart("03_barh.png")

    # HISTOGRAM: e.g., a bin from 0 to 25 counts fares inside that interval.
    titanic["Fare"].plot(kind="hist", bins=5, title="Fare Distribution")
    plt.xlabel("Fare")
    save_chart("04_histogram.png")

    # SCATTER: each marker represents one passenger with numeric Age and Fare.
    titanic.plot.scatter(x="Age", y="Fare", title="Age versus Fare")
    save_chart("05_scatter.png")

    # BOX: center line is median; box covers middle half of observations.
    sales.boxplot(column="Sales", by="Company")
    plt.suptitle("")
    plt.title("Sales Spread by Company")
    save_chart("06_box.png")

    # PIE: total 100% divided between company shares.
    sales.groupby("Company")["Sales"].sum().plot.pie(autopct="%.1f%%")
    plt.ylabel("")
    save_chart("07_pie.png")

    # AREA: shaded running total by date.
    temperatures.cumsum().plot.area(title="Cumulative Temperatures")
    save_chart("08_area.png")

    # DIFFERENCE HISTOGRAM: distribution of step-to-step changes.
    temperatures.diff().dropna().plot.hist(bins=4, title="Changes between Days")
    save_chart("09_diff_hist.png")

    # Reproducible fake flower dataset for numerical plot practice.
    rng = np.random.default_rng(10)
    flowers = pd.DataFrame({
        "sepal_length": rng.normal(5.8, 0.7, 60),
        "sepal_width": rng.normal(3.0, 0.3, 60),
        "petal_length": rng.normal(4.1, 1.4, 60),
        "petal_width": rng.normal(1.3, 0.5, 60),
    })
    flowers["species"] = ["setosa", "versicolor", "virginica"] * 20

    # HEXBIN: the x/y dots are grouped into hexagonal bins by density.
    flowers.plot.hexbin(x="sepal_length", y="petal_length", gridsize=8)
    save_chart("10_hexbin.png")

    # KDE: smooth distribution estimated from numeric observations.
    flowers["sepal_length"].plot.kde(title="Smoothed Sepal Length Distribution")
    save_chart("11_kde.png")

    # SCATTER MATRIX: compare each numerical column against every other one.
    scatter_matrix(flowers.select_dtypes(include="number"), figsize=(9, 9), diagonal="hist")
    save_chart("12_scatter_matrix.png")

    # ANDREWS CURVES: display multivariate patterns for labeled categories.
    andrews_curves(flowers, "species")
    save_chart("13_andrews_curves.png")

    # MULTIPLE PANELS: one small separate plot per column.
    flowers.select_dtypes(include="number").plot(subplots=True, layout=(2, 2), figsize=(8, 6))
    save_chart("14_subplots.png")

    # SECONDARY Y: two series with different scales shown on separate axes.
    two_scales = pd.DataFrame({"small": [1, 2, 3], "large": [500, 600, 900]})
    ax = two_scales["small"].plot(label="small")
    two_scales["large"].plot(secondary_y=True, ax=ax, label="large")
    save_chart("15_secondary_y.png")

    # A simple color-grid heatmap using Matplotlib, no extra package required.
    plt.imshow(np.array([[1, 2, 3], [4, 5, 6]]), cmap="viridis")
    plt.colorbar(label="Value")
    plt.title("Heatmap")
    save_chart("16_heatmap.png")

    # LOG SCALE: useful when positive values span several orders of magnitude.
    pd.Series([1, 10, 100, 1000]).plot(logy=True, title="Logarithmic Y Axis")
    save_chart("17_log_scale.png")

# ============================================================================
# LESSON 25: INTERACTIVE PLOTLY
# ============================================================================
# Matplotlib commonly generates STATIC charts such as PNG images.
# Plotly generates INTERACTIVE charts: hover, zoom, pan, and tooltips.
# plotly.express (usually px) is an easier entry point for common plots.
# .write_html(path) saves a web page that opens in a normal browser.
# Plotly's graph_objects (usually go) offers deeper customization.
# The notebook uses both the Plotly library and Cufflinks' DataFrame .iplot().
# Plotly Express is a modern alternative for common interactive plots.
# Plotly maps may require extra data, internet, or version-specific options;
# the sample here uses a self-contained latitude/longitude table.

if RUN_CHARTS:
    try:
        import plotly.express as px
        import plotly.graph_objects as go
    except ImportError:
        print("Plotly is optional: install with python -m pip install plotly")
    else:
        heading("25. PLOTLY INTERACTIVE CHARTS")
        fig = px.line(x=list(range(len(temperatures))), y=temperatures.to_list(),
                      labels={"x": "Day number", "y": "Temperature"},
                      title="Interactive Line Chart")
        fig.write_html(charts_dir / "18_plotly_line.html")

        fig = px.scatter(titanic, x="Age", y="Fare", color="Sex",
                         hover_name="Name", title="Interactive Scatter")
        fig.write_html(charts_dir / "19_plotly_scatter.html")

        fig = px.bar(sales, x="Company", y="Sales", color="Person",
                     title="Interactive Sales Bars")
        fig.write_html(charts_dir / "20_plotly_bar.html")

        fig = px.box(sales, x="Company", y="Sales", title="Interactive Box Plot")
        fig.write_html(charts_dir / "21_plotly_box.html")

        fig = px.histogram(titanic, x="Fare", nbins=5, title="Interactive Histogram")
        fig.write_html(charts_dir / "22_plotly_hist.html")

        fig = px.area(x=list(range(len(temperatures))), y=temperatures.cumsum().to_list(),
                      title="Interactive Area Chart")
        fig.write_html(charts_dir / "23_plotly_area.html")

        fig = px.imshow([[2, 4], [1, 3]], text_auto=True, title="Interactive Heatmap")
        fig.write_html(charts_dir / "24_plotly_heatmap.html")

        # go.Surface makes a 3-D surface from a grid of numeric heights.
        fig = go.Figure(data=[go.Surface(z=[[1, 2, 3], [2, 5, 2], [3, 2, 1]])])
        fig.update_layout(title="3D Surface")
        fig.write_html(charts_dir / "25_plotly_surface.html")

        # Bubble plot = scatter plot where marker SIZE encodes another quantity.
        fig = px.scatter(sales, x="Company", y="Sales", size="Sales",
                         color="Person", title="Bubble Chart")
        fig.write_html(charts_dir / "26_plotly_bubble.html")

        # A 3-D scatter uses three numeric columns to place each point in space.
        points3d = pd.DataFrame({"x": [1, 2, 3], "y": [3, 1, 2],
                                 "z": [2, 3, 1]})
        fig = px.scatter_3d(points3d, x="x", y="y", z="z", title="3D Scatter")
        fig.write_html(charts_dir / "27_plotly_3d_scatter.html")

        # Basic map without fetching a remote CSV or GeoJSON.
        locations = pd.DataFrame({"city": ["New York", "Los Angeles"],
                                  "lat": [40.7128, 34.0522],
                                  "lon": [-74.0060, -118.2437]})
        fig = px.scatter_geo(locations, lat="lat", lon="lon", hover_name="city",
                             scope="usa", title="Locations on a Map")
        fig.write_html(charts_dir / "28_plotly_map.html")
        print("Saved interactive HTML charts to:", charts_dir)

# ============================================================================
# LESSON 26: CUFFLINKS -- PANDAS + PLOTLY SHORTCUT
# ============================================================================
# Cufflinks is an additional package that connects Pandas with Plotly.
# Its popular syntax is df.iplot() or df.iplot(kind='bar').
# .iplot() is NOT a built-in Pandas method; Cufflinks adds it.
# In the original notebook, cf.go_offline() sets offline notebook behavior,
# and py.offline.init_notebook_mode() configures Plotly for Jupyter.
# Those notebook setup commands are different from a plain Python script.
# Your notebook demonstrates these chart kinds: line, scatter, bar, barh,
# box, area, surface, scatter3d, spread, hist, bubble3d, and heatmap.
# The exact availability of legacy Cufflinks APIs can depend on versions.
# For standalone scripts, Plotly Express + write_html is more reliable.
# The example below is OPTIONAL: it may not work with some package versions.

# Uncomment INSIDE A JUPYTER NOTEBOOK (not necessary for this script):
# import cufflinks as cf
# cf.go_offline()
# display(sales.iplot(kind='bar', x='Company', y='Sales', asFigure=True))
# For this .py tutorial, Lesson 25 shows standalone Plotly equivalents.
# 'spread' compares differences between data series over a shared x-axis.
# 'ratio' compares their relative magnitudes using division.
# 'barmode=stack' stacks series on top of each other rather than side by side.
# 'bins' in a histogram controls the approximate number of value intervals.
# 'colorscale' controls how numeric values map to colors in a heatmap/surface.

# ============================================================================
# LESSON 27: FOLIUM, GEOJSON, AND GEOPANDAS
# ============================================================================
# Folium creates interactive map pages based on geographic coordinates.
# LATITUDE = north/south position; LONGITUDE = east/west position.
# GeoJSON is a text format containing geographic shapes and their metadata.
# A choropleth colors geographic areas according to numerical values.
# GeoPandas extends Pandas with geometry-aware columns and spatial methods.
# A shapefile is a set of geographic files (not a normal single CSV).
# Your notebooks mention a London borough SHP file and a U.S. county
# GeoJSON fetched over the internet. Those external assets were NOT attached.
# The Folium example below makes a simple map from two known city locations.

if RUN_CHARTS:
    try:
        import folium
    except ImportError:
        print("Folium is optional: python -m pip install folium")
    else:
        heading("27. FOLIUM MAP")
        city_map = folium.Map(location=[39.0, -98.0], zoom_start=4)
        folium.Marker([40.7128, -74.0060], popup="New York").add_to(city_map)
        folium.Marker([34.0522, -118.2437], popup="Los Angeles").add_to(city_map)
        city_map.save(str(charts_dir / "29_folium_map.html"))
        print("Saved:", charts_dir / "29_folium_map.html")

# ============================================================================
# LESSON 28: COMMON BEGINNER ERRORS -- AND WHAT THEY MEAN
# ============================================================================
# SyntaxError: your Python grammar is invalid; look for missing : or brackets.
# NameError: you referred to a variable/import that doesn't exist yet.
# TypeError: you tried an operation on an unsuitable value type.
# KeyError: a label/column/key you selected does not exist.
# IndexError: you selected an integer position that is out of bounds.
# ModuleNotFoundError: you tried importing a package that is not installed.
# FileNotFoundError: a CSV or shapefile path points to a missing file.
# AttributeError: a method doesn't exist on this object or package version.
# ValueError: supplied value is wrong for the operation.
# Read the LAST LINE of an error traceback first. It usually names the error.

heading("28. SAFE ERROR EXAMPLE")
try:
    print(titanic["NotARealColumn"])
except KeyError as exc:
    print("We caught a KeyError rather than crashing:", exc)

# ============================================================================
# LESSON 29: MINI EXERCISES (WITH SOLUTIONS)
# ============================================================================
# Try predicting each output BEFORE running it.
# 1. Find the age of Ava using .loc or .iloc.
# 2. Count missing Ages.
# 3. Find the mean Fare by Sex.
# 4. Show passengers with Fare >= 20.
# 5. Build a new column that is Fare + 10.
# 6. Sort by that new column, descending.
# 7. Which company has the greatest combined Sales?
# 8. Merge two tables on 'key' and explain the NaNs from an outer merge.
# 9. When RUN_CHARTS=True, locate the interactive Plotly HTML files.
# 10. Why does [1,2]*2 differ from np.array([1,2])*2?

heading("29. PRACTICE ANSWERS")
print("1. Ava's Age:", titanic.loc[titanic["Name"] == "Ava", "Age"].iloc[0])
print("2. Missing ages:", titanic["Age"].isna().sum())
print("3. Mean Fare by Sex:\n", titanic.groupby("Sex")["Fare"].mean())
print("4. Fare >=20:\n", titanic.loc[titanic["Fare"] >= 20, ["Name", "Fare"]])
practice = titanic.assign(Fare_Plus_10=titanic["Fare"] + 10)
print("5/6. New column sorted:\n", practice[["Name", "Fare_Plus_10"]].sort_values("Fare_Plus_10", ascending=False))
print("7. Highest total sales company:", sales.groupby("Company")["Sales"].sum().idxmax())
print("8. Outer merge example:\n", pd.merge(left, right, on="key", how="outer"))
print("9. Set RUN_CHARTS=True and see python_tutorial_charts/")
print("10. List repeats; NumPy array multiplies numbers elementwise.")

# ============================================================================
# END OF TUTORIAL
# ============================================================================
# What to learn next: using real CSVs, cleaning realistic messy datasets,
# multiple groups and aggregations, writing functions, and making dashboards.
# TIP: If the output is too long, execute ONE LESSON at a time in VS Code:
# select some lines and use 'Run Selection/Line in Python Terminal'.
# You can also open the file in any plain text editor: explanations remain
# readable because all theory is written in # comments.
print("\nDONE! You finished the beginner Python / Pandas tutorial.")
