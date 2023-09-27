import pickle

mylist=["sweety","ganesh"]
with open('file.txt','wb') as f:
    pickle.dump(mylist,f)
#unpickling
unpic=open('file.txt','rb')
m=pickle.load(unpic)
print(m)