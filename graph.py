import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
# Step 1: Read data from CSV file
ameruca_sale = []
eur_sale = []
jp_sale = []
rest_sale = []
global_sale = []
row0 = []

with open('games.csv', 'r') as file:
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
mode_sale_na = statistics.mode(ameruca_sale)
mean_sale_eu = statistics.mean(eur_sale)
median_sale_eu = statistics.median(eur_sale)
mode_sale_eu= statistics.mode(eur_sale)
mean_sale_jp = statistics.mean(jp_sale)
median_sale_jp = statistics.median(jp_sale)
mode_sale_jp = statistics.mode(jp_sale)
mean_sale_rest = statistics.mean(rest_sale)
median_sale_rest = statistics.median(rest_sale)
mode_sale_rest = statistics.mode(rest_sale)
mean_sale_global = statistics.mean(global_sale)
median_sale_global = statistics.median(global_sale)
mode_sale_global = statistics.mode(global_sale)
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
def bar_chart():
    species = ("na sales", "eur sales", "jp sales","rest of world","global")
    penguin_means = {
    'meduim': (median_sale_na,median_sale_eu,median_sale_jp,median_sale_rest,median_sale_global),
    'mean': (mean_sale_na, mean_sale_eu, mean_sale_jp,mean_sale_rest,median_sale_global),
    "mode": (mode_sale_na,mode_sale_eu,mode_sale_jp,mode_sale_rest,mode_sale_global)
    }

    x = np.arange(len(species))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
     offset = width * multiplier
     rects = ax.bar(x + offset, measurement, width, label=attribute)
     ax.bar_label(rects, padding=3)
     multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('sales in millons')
    ax.set_title('reigons by sales')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 20)
    plt.show()

for i in range(1):
   bar_chart()
for i in range(len(row0)):
    title = row0[i]
    values = [ameruca_sale[i], eur_sale[i], jp_sale[i], rest_sale[i]]
    plot_pie_chart(values, title)


