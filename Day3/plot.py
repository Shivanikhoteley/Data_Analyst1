import matplotlib.pyplot as plt

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
sales = [160, 150, 140, 145, 175, 165, 180]

plt.plot(days, sales, marker="o", color="red", linestyle="--")  # Dashed red line

plt.title("Sales Over Days", fontsize=14, color="blue", fontweight="bold")  # Blue bold title
plt.xlabel("Days", fontsize=12, color="blue")  # Blue X-axis label
plt.ylabel("Sales", fontsize=12, color="blue")  # Blue Y-axis label

plt.show()