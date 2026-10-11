import pandas as pd
import numpy as np

data= pd.read_csv("student_data.csv")
#cleaning the data
data["Java"]= data["Java"].astype("Int64")
data["Java"] = data["Java"].ffill()
data["Name"]= data["Name"].str.strip()
data["Department"] = data["Department"].str.upper()
data.loc[32, "ML"] = "70"
data["ML"] = data["ML"].astype("Int64")
data.loc[data["Attendance"] > 100, "Attendance"] = round(data["Attendance"].mean())


#OPERATIONS to find avg and total marks
subjects = ["ML", "Java", "Maths", "OS"]

data["Total"] = data[subjects].sum(axis = 1)

data["Average"] = data[subjects].mean(axis = 1)

#operations for pass/fail
data["pass/fail"]= data[subjects].apply(lambda x:"PASS" if (x>=40).all() else "FAIL", axis = 1)

#operations for getting grades
def calculate_grades(total):
    if total>= 360:
        return "A+"
    elif total>=320:
        return "A"
    elif total>=240:
        return "B"
    elif total>=200:
        return "C"
    elif total >=160:
        return "D"
    else:
        return "F"

data["Grades"] = data["Total"].apply(calculate_grades)

#operatins to get top performers

highest_student = data.loc[[data["Total"].idxmax()]]
print("Highest Marks:")
print(highest_student.to_string(index = False))

print("\nTop 5 Highest Marks:")
top_five = data.nlargest(5, "Total")
print(top_five.to_string(index=False))

print("\nTop 5 Lowest Marks:")
last_five = data.nsmallest(5, "Total")
print(last_five.to_string(index=False))

#pass/fail counts
print("\nPass/Fail Statistics:")
result = data["pass/fail"].value_counts()
print("Total Students:", len(data))
print("Total Passed:", result.get("PASS", 0))
print("Total Failed:", result.get("FAIL", 0))


#AVERAGE
ML_avg = np.mean(data["ML"])
print("\nML Average Marks: ", ML_avg)
Maths_avg = np.mean(data["Maths"])
print("Maths Average Marks: ", Maths_avg)
OS_avg = np.mean(data["OS"])
print("OS Average Marks: ", OS_avg)
Java_avg = np.mean(data["Java"])
print("Java Average Marks: ", Java_avg)
avg = data["Average"].mean()
print("\nOverall Class Average: ", round(avg, 2))

averages = {
    "ML": ML_avg,
    "OS": OS_avg,
    "Java": Java_avg,
    "Maths": Maths_avg
}
sub_high_avg = max(averages, key=averages.get)
sub_low_avg = min(averages, key=averages.get)

print(f"\nSubject With the Highest Average: {sub_high_avg} : {averages[sub_high_avg]}")
print(f"Subject With the Lowest Average: {sub_low_avg} : {averages[sub_low_avg]}")

#attendace
avg_attendance = data["Attendance"].mean()
print("\nAvg Attendance of Students:", round(avg_attendance, 2))

highest_att = data.loc[[data["Attendance"].idxmax()]]
print("\nHighest Attendance:")
print(highest_att[["Name", "Attendance"]].to_string(index = False))

lowest_att = data.loc[[data["Attendance"].idxmin()]]
print("\nLowest Attendance:")
print(lowest_att[["Name", "Attendance"]].to_string(index = False))

#saving in a new csv file
data.to_csv("student_results.csv", index=False)