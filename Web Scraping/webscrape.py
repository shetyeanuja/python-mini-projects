# Scraping the faculty details of various departments of my college

# importing the packages required
import requests
from bs4 import BeautifulSoup
import csv

# taking the urls for web scraping
urls = ["https://vesit.ves.ac.in/faculty/IT","https://vesit.ves.ac.in/faculty/CMPN",
        "https://vesit.ves.ac.in/faculty/ETRX","https://vesit.ves.ac.in/faculty/INST",
        "https://vesit.ves.ac.in/faculty/EXTC"]

# soup is a list holding the tree structure of html content of all the urls
soup = []
for url in range(len(urls)):
    r = requests.get(urls[url])
    soup.append(BeautifulSoup(r.content,"html5lib"))
#print(soup)

# storing the department names of college
dep = []
for s in range(len(soup)):
    d = soup[s].find("div", attrs = {'class':'col-md-9 col-lg-10 col-sm-10 col-12 py-3'})
    x = (d.h2.style.next_sibling)
    x = " ".join(x.split())
    dep.append(x)
#print(dep)

# storing the images of all the faculties
images = []
for s in range(len(soup)):
    d = soup[s].findAll("div", attrs = {'class':'card-body'})
    for i in d:
        images.append(i.img['src'])
#print(images)

# storing all the details in a list
details = []
k1=0
k2=0
for s in range(len(soup)):
    d = soup[s].findAll("div", attrs = {'class':'data'})
    for i in d:
        data = {}
        data["Name"] = i.h4.text
        data["Designation"] = i.p.text
        data["Department"] = dep[k1]
        data["Image"] = images[k2]
        details.append(data)
        k2+=1
    k1+=1
#print(details)

# storing the list details in csv file
csv_filename = "faculty_details.csv"
with open(csv_filename,'w',newline='') as f:
    write = csv.DictWriter(f,['Name','Designation','Department','Image'])
    write.writeheader()

    for d in details:
        write.writerow(d)
