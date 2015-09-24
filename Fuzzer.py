import FindInputs
import customauth
from page_discovery import LinkAggregator
import sys

def main():
	custom_auth = False
	custom_auth_string = ""
	common_words_file = ""
	argv = sys.argv
	if len(argv) < 3:
		print("Not enough information provided")
		exit()
	url = argv[2]
	if (argv[1] == "discover"):
		for arg in argv[2:]:
			a =arg.split("=")
			if(a[0] == "--custom-auth"):
				custom_auth = True
				custom_auth_string = a[1]
			if(a[0] == "--common-words"):
				common_words_file = a[1]
	elif argv[1] == "test":
		print("Not Implemented Yet")
	else:
		print("Invalid Mode")
	
	if(common_words_file == ""):
		print("Please provide valid word file\n")
		exit()
	f = open(common_words_file)
	commonw = f.read().split('\n')
	if(custom_auth):
		getsite(custom_auth_string)
	
	res = FindInputs.getPage(url)
	cookies = FindInputs.getCookies(res)
	inputs = FindInputs.crawlForInput(res)
	
	urlargs = FindInputs.parseUrl(url)
	#urls = LinkAggregator.getAllLinks(url)
	print("======================================================")
	print("linked pages:\n")
	#for a in urls:
	#	print("%s \n", a)
	print("======================================================")
	print("cookies received\n")
	for cookie in cookies:
		print("{0}\n".format(cookie))
	print("======================================================")
	print("Found inputs\n")
	for input in inputs:
		print("name {0} : type {1} \n".format(input[0], input[1]))
	print("======================================================")
	print("URL arguments\n")
	for urlarg in urlargs:
		if len(urlarg) == 2:
			print("Key {0}: Value {1}\n".format(urlarg[0], urlarg[1]))
	print("======================================================")
	"""for a in urls:
		urlargs = parseUrl(a)
		res = getPage(a)
		inputs = crawlForInput(a)
		cookies = getCookies(a)
		print("for url: %s", url)
	"""
main()