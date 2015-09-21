__author__ = 'Zak'

'''
Creates a list of URLs reachable from the initial given page. Does not follow links off-site.
'''

import urllib.request

class LinkAggregator():

    def parsePage(self,html): # breaks a page down and generates a raw list of all links on page
        start = 0 # inital entry into html
        displacement = 6 #number of spaces away the link is from its href tag
        end = len(html) # depth of the html
        links = [] #will store found links
        while html.find("href=",start,end) != -1: #while undiscovered links remain in the page
            startIndex = html.find("href=",start,end) #start index of search for new links
            startFind = displacement + startIndex #start index of salvagable link
            endIndex = html.find('"',startFind, end ) #finds the index of the end of the link
            links.append(html[startIndex + displacement:endIndex]) #adds the gathered link to the list
            start = endIndex #moves start up to the end of the last gathered link
        print(links) #displays all gathered links (currently for testing)


    def getPageSource(self,url): # just gathers raw HTML from a url and converts to string for processing
        with urllib.request.urlopen(url) as response:
            html = str(response.read())
            self.parsePage(html)


new = LinkAggregator() #both for functionality testing
new.getPageSource("http://www.se.rit.edu/~swen-331/projects/fuzzer/")
