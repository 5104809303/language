import requests
from bs4 import BeautifulSoup
import csv

url="https://trojanpowersports.com/Motorcycles-Honda-Africa-Twin-2022-Monroe-MI-7ed54ceb"
page = requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.text)
#print(soup.prettify()) #prettify means the data in the website will print as it is.

#how to get images
img1=[]
image=soup.findAll('div',class_="item")
#print(image)

#i want only source of the image
# for i in image:
#     j=i.img['src']
#     img1.append(j)
# print(img1)
 
to get links
links=[]
link=soup.findAll('div',class_='thumbnail-frame')
# print(link)
for i in link:
    # j=i.a.text --> this line is to get text
    j=i.a['href']
    links.append(j)
print(links)

#how to save data in csv file(we are storing the links)
with open('li.csv','w') as csv_file:
   write=csv.writer(csv_file)
   write.writerow(link)
   for i in link:
     j=i.a['href']
     links.append(j)
   write.writerow(img1)

   


