import csv
import statistics
import matplotlib.pyplot as plt

# Step 1: Read data from CSV file
attendance_percentages = []
test_scores = []

with open('dataclass.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        attendance_percentages.append(int(row[1]))
        test_scores.append(int(row[2]))

# Step 2: Calculate mean and median values
mean_attendance = statistics.mean(attendance_percentages)
median_attendance = statistics.median(attendance_percentages)

mean_test_score = statistics.mean(test_scores)
median_test_score = statistics.median(test_scores)

# Step 3: Plot the data in a bar graph
labels = ['Attendance Percentage', 'Test Score']
values = [mean_attendance, mean_test_score]

plt.bar(labels, values, color=['skyblue', 'orange'])
plt.title('Mean Values')
plt.xlabel('Categories')
plt.ylabel('Mean Value')
plt.show()

# Print mean and median values
print("Mean Attendance Percentage:", mean_attendance)
print("Median Attendance Percentage:", median_attendance)
print("Mean Test Score:", mean_test_score)
print("Median Test Score:", median_test_score)
