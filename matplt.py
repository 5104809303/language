import matplotlib.pyplot as plt
# import numpy as np
# plt.plot([1,2,3,4],[5,6,7,8],'ro')
# plt.ylabel('y number')
# plt.xlabel('x number')
# plt.show()



# import matplotlib.pyplot as plt

# xis=[0,7,5,5,9,8,1,0]

# yxis=['cat','dog','pig','ant','cow','owl','fly','eagle']


# plt.bar(xis,yxis,label="rating",color='k',width='4') 
# # linestyle='-',color='black',linewidth='20',height='10')
# plt.xlabel('xis')
# plt.ylabel('yxis')
# plt.title('barplot')
# plt.show()

import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 55]

# Create a bar plot with a numerical width value
plt.bar(categories, values, label="Rating", color='k', width=4)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

# Show the plot
plt.show()
