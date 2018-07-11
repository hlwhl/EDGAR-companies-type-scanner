#coding:utf-8
import urllib, urllib2
from bs4 import BeautifulSoup
 
file=open('complist.txt','rU')
try:
	for line in file:
		url_pre = 'https://www.sec.gov/cgi-bin/browse-edgar?company='
		url = url_pre+line
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response.read(),'lxml') 
		comptype=soup.select('div.companyInfo a')
		if len(comptype)>=2 :
			if comptype[1].get_text()=='2833':
				print(line+' : '+comptype[1].get_text())
			if comptype[1].get_text()=='2834':
				print(line+' : '+comptype[1].get_text())
			if comptype[1].get_text()=='2835':
				print(line+' : '+comptype[1].get_text())
			if comptype[1].get_text()=='2836':
				print(line+' : '+comptype[1].get_text())
finally:
	file.close()


