import requests

def getPage(url):
	r = requests.get(url)
	return r

def parseUrl(url):
	inputList = []
	url = url.split('?')
	url = url[len(url)-1]
	url = url.split('&')

	for u in url:
		if( u.find("=")):
			u = u.split("=")
			inputList.append(u)
	return inputList

def getCookies(res):
	cookiesList = []
	for c in res.cookies:
		cookiesList.append(c)
	return cookiesList
	
def crawlForInput(response):
	inputList = []
	tupleList = []
	typeindex = 0;
	nameindex = 0;
	currentIndex = 0;
	inputText = response.text.split('\r')
	for l in inputText:
		if( l.find("<input")!= -1):
			inputList.append(l.strip())
	for l in inputList:
		i = l.find("type=")
		y = l[i+6:l.find("\"",i+6)]
		i = l.find("name=")
		z = l[i+6:l.find("\"",i+6)]
		tupleList.append((z,y))
	return tupleList