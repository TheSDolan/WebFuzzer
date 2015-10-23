import urllib.request


class Sensitive():
    #test vector list
    #testlist = ["http://www.tutorialspoint.com/python/string_find.htm","http://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/"]
    #this function will process the requests provided in the vector list and be sure that none of the returned data
    #is on the BlackList
    def checklist(self,VectorList,BlacklistFile):
        #list of words we should not find in the request result
        BlackList = []
        #take in a file and append each line of that file to the blacklist
        file = open(BlacklistFile,'r')
        for line in file:
            BlackList.append(line)
        for item in VectorList:
            result = urllib.request.urlopen(item)
            text = result.read()
            #need to decode the bytes into a string so we can compare to strings from blacklist
            text = text.decode(encoding='UTF-8')
            for word in BlackList:
                if (word in text):
                    print("Fuzzer found potential security risk. A string in the Blacklist was found in the response from the website.")
