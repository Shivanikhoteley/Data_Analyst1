import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Orange", "Mango"]
quantity = [50, 60, 71, 88]
colors = ['#FF5733', '#33FF57', '#3357FF', '#F4C542']  # Different colors for each bar

plt.bar(fruits, quantity, color=colors, edgecolor='black')

# Add labels on top of bars
for i in range(len(fruits)):
    plt.text(i, quantity[i], quantity[i], ha='center', va='bottom')

plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title("Fruits vs Quantity")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
