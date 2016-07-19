# tescoSearch.py

# This module uses Tesco API to perform various useful operation on the 
# database.
# The class tescoSearch abstract a search on the database. Its paramaters
# are the query for the search and the offset(starting point) and limit
# (number of results to show)
#
# AUTHOR: s


import httplib, urllib, base64, json
import ConfigParser

class tescoSearch():
    # constructor for the search object
    def __init__(self, query,offset = 0, limit = 10):
	config = ConfigParser.RawConfigParser()
	config.read('apikey.cfg') 
	
	self.API_KEY = config.get('Keys','API_TESCO')        
        self.query = query
        self.offset = offset
        self.limit = limit
        self.data = self.getData()
      
    # creates the url we call to make the search    
    def getUrl(self):
        return "/grocery/products/?query={q}&offset={o}&limit={l}&%s".format(q=self.query, o = self.offset, l = self.limit)
    
    # returns the raw JSON data associated with the search 
    def getData(self):
        url = self.getUrl()
        
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': self.API_KEY
        }    
        
        try:
            conn = httplib.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", url , "", headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            
        return data  #return data as  <string> ,maybe change
    
    # returns a dictionary for all products that match the search
    def getResults(self):
        data = self.getData()
        dic_data = json.loads(data)
        return dic_data['uk']['ghs']['products']['results']# <dict>
    
    #displays the results in decrescent order of cost
    def cheapestResults(self):
        res = self.getResults()
        cheap_res = sorted(res, key= lambda k:k['price'])
        return cheap_res


        


def main():
   return
        
if __name__ == '__main__':
    main()