
def plot_pie_chart(values):
    total = sum(values)
    fractions = [value / total for value in values]

    # Colors
    colors = ['#ff5733', '#33ff57', '#5733ff', '#33ffff']  # You can adjust colors as needed

    # Plot
    plt.figure(figsize=(8, 8))
    wedges, _, autotexts = plt.pie(values, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Specify the coordinates for text
    text_x = 0
    text_y = -1.2

    # Display values and fractions at specified coordinates
    for value, fraction in zip(values, fractions):
        plt.text(text_x, text_y, f'{value} / {total} ({fraction:.2f})', ha='center')
        text_y += 0.2  # Increment y-coordinate for next text line

    plt.show()