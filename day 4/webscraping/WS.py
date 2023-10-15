'''from bs4 import BeautifulSoup
'''
file=open("index.html")
contents=file.read()
file.close()
#print(contents)

soup=BeautifulSoup(contents,"html.parser")#parser-identifies html file and reads
#print(soup.title)
#print(soup.a)#first a only retrived
#print(soup.h1)
#to extract all anchor tags use find all

#print(soup.find_all(name="a"))

#first heading text only needed ,avoid tags
print(soup.h1.text)

#get()->href attri can be extracted

print(soup.a.get("href"))

first_heading=soup.find(name="h1",id="first-heading")
print(first_heading.getText())

x=soup.select(selector="")
y=

to extract from live modules-'''
import requests

response=requests.get("https://www.youtube.com/",headers)
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
print(soup)

#list of all heading to be extracted inspect-class-find-heading text only;selector->
#list-all scores
#heading  click links
#lxml-price,name:amazon product

user agent
accept'''