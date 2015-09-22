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
        return links


    def getAllLinks(self,url): # takes url, gathers raw html, then runs it through processors to finished links
        with urllib.request.urlopen(url) as response:
            html = str(response.read()) #converts url into string of html
            links = self.parsePage(html) # parses page into an array of links
            completeLinks = [] #will hold the completed links
            i = 0 #used to iterate through and ensure each link is complete
            while i < len(links):
                completeLinks.append(self.urlComplete(url,links[i])) #completes the links
                i = i + 1
            return completeLinks

    def urlStrip(self, url): # strips a url of one of its end components so it may be slotted into directory references
        url = url[:url.rfind("/")] # finds farthest back /
        return url[:url.rfind("/") + 1] #returns stripped end with slash intact

    def urlComplete(self, url, link): #takes broken or incomplete links and formalizes them
        slices = 0 #used later to fix directory reference
        if link.find("../") != -1: #if there is directory reference
            while link.find("../",0,3) != -1: #for each reference
                link = link[3:] #cut off the ../
                slices = slices + 1
            for i in range(slices): #trim the base url to slot in the link
                url = self.urlStrip(url)
            return url + link
        elif link.find("http",0,6) != -1: #if the link is valid, return it
            return link
        else: #otherwise, formalize the link
            return url + link

new = LinkAggregator() #both for functionality testing
print(new.getAllLinks("http://www.se.rit.edu/~swen-331/projects/fuzzer/"))