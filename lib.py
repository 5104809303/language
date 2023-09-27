# from matplotlib import pyplot as plt
# import numpy as np
# x=[5,2,7]
# y=[2,16,4]
# plt.plot(x,y,'o')
# plt.title('info')
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')
# plt.show()

import pickle 
mylist=["sweety",'python']
with open ('file.txt','wb') as f:
    pickle.dump(mylist,f)
# unpic=open('file.txt','rb')
# m=pickle.load(unpic)
# print(m)