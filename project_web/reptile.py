import sys, os
sys.path.append(os.getcwd())
from manage import DEFAULT_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)
import django
django.setup()
import requests
import json
import pyprind
from bs4 import BeautifulSoup
from models import article


json_arr = []

def dump(fileName):
	with open(fileName, 'w', encoding='UTF-8') as f:
		json.dump(json_arr, f)
def parsePage(url):
	for j in range(1,2):
		control_1=1
		print (os.path.abspath(reptile))
		while control_1==1:
			try:
				res = requests.get(url+str(j),timeout=0.5)
				soup = BeautifulSoup(res.text,"html.parser")
				control_1=0
				for i in soup.select('.subject-text'):
					tmp={}
					tmp['title'] = i.select('a')[0].text
					tmp['link']='https://www.mobile01.com/' + i.select('a')[0]['href']
					article.objects.create(title=tmp['title'], link=tmp['link'])
					json_arr.append(tmp)
			except requests.RequestException as e:
				control_1=1
		
	for i in json_arr:
		control_2 = 1
		print(i['title'])
		while control_2==1:
			try:
				inner_res = requests.get(i['link'],timeout=0.3)
				inner_soup = BeautifulSoup(inner_res.text,"html.parser")
				control_2=0
				x=inner_soup.select('.pagination')[1].select('a')
				length=1
				if len(x) > 3 :
					length=int(x[len(x)-1].text)
				elif len(x) >0 :
					length=int(x[len(x)-2].text)
				i['reply']=[]
				for j in inner_soup.select('.single-post'):
					tmp={}
					tmp["author"] = j.select('.fn a')[0].text
					tmp["time"] = j.select('.date')[0].text
					tmp["reply"] = j.select('.single-post-content div')[0].text
					i['reply'].append(tmp)
				for j in range(1,length):
					control_3 = 1
					while control_3==1:
						try:
							inner_res = requests.get(i['link']+"&p="+str(j+1),timeout=0.3)
							inner_soup = BeautifulSoup(inner_res.text,"html.parser")
							control_3 = 0
							for j in inner_soup.select('.single-post'):
								tmp={}
								tmp["author"] = j.select('.fn a')[0].text
								tmp["time"] = j.select('.date')[0].text
								tmp["reply"] = j.select('.single-post-content div')[0].text
								i['reply'].append(tmp)
						except requests.RequestException as e:
							control_3 = 1
			except requests.RequestException as e:
				control_2=1

	dump('demo.json')

parsePage('https://www.mobile01.com/forumtopic.php?c=23&p=')