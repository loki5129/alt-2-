import csv
import statistics
import matplotlib.pyplot as plt

# Step 1: Read data from CSV file
ameruca_sale = []
eur_sale = []
jp_sale = []
rest_sale = []
global_sale = []
row0 = []

with open('alt-2--main\games.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
       ameruca_sale.append(float(row[2]))
       eur_sale.append(float(row[3]))
       jp_sale.append(float(row[4]))
       rest_sale.append(float(row[5]))
       global_sale.append(float(row[6]))
       row0.append(str(row[0]))

# Step 2: Calculate mean and median values
mean_sale_na = statistics.mean(ameruca_sale)
median_sale_na = statistics.median(ameruca_sale)
mean_sale_eu = statistics.mean(eur_sale)
median_sale_eu = statistics.median(eur_sale)
mean_sale_jp = statistics.mean(jp_sale)
median_sale_jp = statistics.median(jp_sale)
mean_sale_rest = statistics.mean(rest_sale)
median_sale_rest = statistics.median(rest_sale)
mean_sale_global = statistics.mean(global_sale)
median_sale_global = statistics.median(global_sale)
labels = ["na sales","eur sales","jp_sale","rest of world sales"]

def plot_pie_chart(values, title):
    total = sum(values)
    fractions = [value / total for value in values]

    # Colors
    colors = ['#ff5733', '#33ff57', '#5733ff', '#33ffff']  # You can adjust colors as needed

    # Plot
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display values and fractions at specified coordinates
    plt.show()


for i in range(len(row0)):
    title = row0[i]
    values = [ameruca_sale[i], eur_sale[i], jp_sale[i], rest_sale[i]]
    plot_pie_chart(values, title)
