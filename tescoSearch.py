# tescoSearch.py

# This module uses Tesco API to perform various useful operation on the 
# database.
# The class tescoSearch abstracts a search on the database. Its paramaters
# are the query for the search and the offset(starting point) and limit
# (number of results to show)
#
# AUTHOR: Gianpiero Cea


import  json
import ConfigParser, os
import requests

class tescoSearch():
    # constructor for the search object
    def __init__(self, query,offset = 0, limit = 10):
	#config object to read the apikey from config file
	config = ConfigParser.RawConfigParser()
	
	## if this doesn't work ,hack: write extended path 
	abspath = os.path.abspath('apikey.cfg')	
	config.read(abspath)
	
	# here we set all the things we need
	self.API_KEY = config.get('Keys','API_TESCO')        
        self.query = query
        self.offset = offset
        self.limit = limit
        self.data= self.getData()
	

	
    def getData(self):
	#the parameters of hour search
	params = {'query'  : self.query,
	        'offset' : self. offset,
	        'limit'  : self.limit
	    }
	
	#set the headers for apikey auth:
	headers = {
		    # Request headers
		    'Ocp-Apim-Subscription-Key': self.API_KEY
		}    	
	
	#here is the core! we use the nice requests module
	r = requests.get('https://dev.tescolabs.com/grocery/products/', params = params, headers = headers)
	
	data = r.text
	##maybe add try-exception for error 
	return data
    
    # returns a dictionary for all products that match the search
    def getResults(self):
        data = self.getData()
	##maybe replace with request json()
        dic_data = json.loads(data)
        return dic_data['uk']['ghs']['products']['results']# <dict>
    
    #displays the results in decrescent order of cost
    def cheapestResults(self):
        res = self.getResults()
        cheap_res = sorted(res, key= lambda k:k['price'])
        return cheap_res

