import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = .025
fig = plt.subplots(figsize=(12,8))

# set height of bar
IT = [12,30,1,8,22]
ECE = [28,6,16,5,10]
CSE = [29,3,24,25,17]

# set position of bar on x axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# make the plot
plt.bar(br1, IT, color='r', width=barWidth,edgecolor='grey', label='IT')
plt.bar(br2, ECE, color='g',width=barWidth,edgecolor='grey',label='ECE')
plt.bar(br3, CSE, color='b',width=barWidth,edgecolor='grey', label='CSE')

# adding Xticks
plt.xlabel('Branch', fontweight='bold', fontsize=15)
plt.ylabel('Students passed', fontweight='bold',fontsize=15)
plt.xticks([r +barWidth for r in range(len(IT))],['2015','2016','2017','2018','2019'])

plt.legend()
plt.show()