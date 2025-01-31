import matplotlib.pyplot as plt

subjects = ["DSA", "Web Development", "SAD", "AI", "Python"]
marks = [90, 80, 85, 95, 99]
colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#FFD700"]
explode = [0, 0, 0, 0, 0.1]  

plt.figure(figsize=(7,7))  
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)

plt.title("Marks in Different Subjects", fontsize=14, fontweight="bold", color="blue")
plt.show()