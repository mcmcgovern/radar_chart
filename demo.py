import matplotlib.pyplot as plt
import numpy as np

# data
categories = ['Fuel Economy', 'Reliability', 'Comfort', 'Design', 'Repair Costs', 'Fuel Economy']

vehicle1 = [5,4,4,2,3]
# ***** to close the radar shape: add the first list element to the end of the list or concatenate *****
vehicle1 = np.concatenate((vehicle1, [vehicle1[0]]))

vehicle2 = [3,4,5,5,4]
vehicle2 = np.concatenate((vehicle2, [vehicle2[0]]))

vehicle3 = [4,4,3,4,5]
vehicle3 = np.concatenate((vehicle3, [vehicle3[0]]))

# calculate evenly-spaced angle coordinates
# use radians for polar plot with 2 * np.pi
label_placement = np.linspace(start=0, stop=2*np.pi, num = len(vehicle1))

# create matplotlib figure and polar plot with labels, title, and legend
plt.figure(figsize=(6,6))
plt.subplot(polar=True)
plt.plot(label_placement, vehicle1)

# use thetagrids to place labels at the specified angles using degrees
lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categories)
plt.title('Compare Vehicles', y=1.1, fontdict={'fontsize': 18})
plt.legend(labels=['vehicle1'], loc=(0.95, 0.8))

plt.show()
