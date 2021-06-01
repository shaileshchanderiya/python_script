import os,sys
import re
from bs4 import BeautifulSoup as bs
import urllib.request,urllib3
output=[]
def Stack_over_flow_serach(string, mx):
    string=re.sub(' ','+',string)
    html_contant=urllib.request.urlopen(('https://stackoverflow.com/questions/tagged/{0}?tab=Votes').format(string)).read()
    #html_contant=urllib.request.urlopen(('https://stackoverflow.com/search?q={0}').format(string)).read()
    soup = bs(html_contant, 'html.parser')
    befr=soup.find_all('a')[1].get('href')
    for tag in soup.find_all(re.compile("h3")):
        match=re.findall('\/questions.*\"',str(tag.a))
        if  match:
            #print(befr + str(match).replace('"','').replace('[\'','').replace('\']',''))
            found=befr + str(match).replace('"','').replace('[\'','').replace('\']','')
            output.append(found)
    for i in range(0,mx):
        print(output[i])

search_str=input("What do you want to search ? \n")

if not search_str:
	#print("please provide input")
	sys.exit("please provide input")
else:
    Stack_over_flow_serach(search_str,30)

	
		
		
