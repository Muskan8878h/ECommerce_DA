import matplotlib.pyplot as plt

y=[10, 15, 13, 17, 20]
x=["part1", "part2", "part3", "part4", "part5"]

plt.bar(x, y, color="purple")
# plt.pie(y, labels=x, autopct="%1.1f%%", colors=["lightblue", "lightgreen", "lightcoral", "gold", "violet"])
# plt.plot(x, y, color="purple")
# plt.scatter(x, y, color="purple") 
# plt.boxplot(y) 
# plt.violinplot(y)
# plt.stem(x, y, linefmt="purple", markerfmt="ro", basefmt="grey")

# if i want ro save 
plt.savefig("mybar.png")

plt.title("Parts vs Values")       # Optional: Add a title
plt.xlabel("Parts")                # Optional: Label x-axis
plt.ylabel("Values")               # Optional: Label y-axis
plt.show()