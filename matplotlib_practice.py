# from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.pyplot as plt  #for bar graph import like this

style.use("ggplot")

#Linear Plot

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.title("graph")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend("line")

# x1 = [1,2,3]
# y1 = [23,45,67]
# x2 = [3,2,7]
# y2 = [32,45,71]
#
# plt.plot(x1, y1, "g", label = "line_one", linewidth="3")
# plt.plot(x2, y2, "r",label = "line_two", linewidth="5")
# plt.grid(True, color="black")
# plt.legend()
#
# plt.show()


####################################################################################

#BAr Graph

x1 = [1,2,3]
y1 = [23,45,67]
x2 = [3,2,7]
y2 = [32,45,71]

plt.bar(x1, y1, label = "graph_one")
plt.bar(x2, y2,label = "graph_two", color="green")


plt.title("graph")
plt.legend()
plt.xlable('ages')
plt.ylabel("y-axis")

plt.show()


