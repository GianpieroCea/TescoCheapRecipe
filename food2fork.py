import urllib2
import urllib
import json
from functools import partial

import random
import ConfigParser
 
 # Code adapted from food2fork Github
 



class food2fork():
	'''
	Usage:
		import food2fork
		f2f = food2fork("My Api Key")
		recipes = f2f.search("chicken, rice")
		moreRecipes = f2f.search("chicken, rice", 2)
	'''

	def __init__(self, debug=False):
		config = ConfigParser.RawConfigParser()
		config.read('apikey.cfg') 
		
		API_KEY = config.get('Keys','API_F2F')
		
		self.apiKey = API_KEY

		self.debugMode = debug

		self.SEARCH_ENDPOINT = 'http://food2fork.com/api/search'
		self.VIEW_ENDPOINT   = 'http://food2fork.com/api/get'
		self.MAX_PAGESIZE = 30

	def search(self,query,page = 1,pageSize = 30):
		try:
			url = self._urlHelper(self.SEARCH_ENDPOINT,q=query,page=page,count=pageSize)

			contents = self._getUrlContents(url)

			data = json.loads(contents)

			if(self.debugMode): print contents

			return data

		except Exception as inst:
			if(self.debugMode): print inst

			return None

	def getTopRated(self,page = 1,pageSize = 30):
		if(pageSize > self.MAX_PAGESIZE): pageSize = self.MAX_PAGESIZE

		try:
			url = self._urlHelper(self.SEARCH_ENDPOINT,page=page,count=pageSize)

			contents = self._getUrlContents(url)
			
			data = json.loads(contents)

			if(self.debugMode): print contents

			return data
		
		except Exception as inst:
			if(self.debugMode): print inst

			return None
	
	def getTrending(self,page = 1,pageSize = 30):
		try:
			url = self._urlHelper(self.SEARCH_ENDPOINT,page=page,count=pageSize,sort='t')

			contents = self._getUrlContents(url)

			data = json.loads(contents)

			if(self.debugMode): print contents

			return data
		
		except Exception as inst:
			if(self.debugMode): print inst

			return None

	def getRecipe(self,recipeId):
		try:
			url = self._urlHelper(self.VIEW_ENDPOINT,rId=recipeId)

			contents = self._getUrlContents(url)

			data = json.loads(contents)

			return data

		except Exception as inst:
			if(self.debugMode): print inst

			return None

	def _urlHelper(self,endpoint,**kwargs):
		data = { 'key' : self.apiKey }

		for key, value in kwargs.iteritems():
			data[key] = value

		if(self.debugMode):
			print "Url:", endpoint + '?' + urllib.urlencode(data)

		return endpoint + '?' + urllib.urlencode(data)

	def _getUrlContents(self,url):
		try:
			response = urllib2.urlopen(url)

			contents = response.read()

			return contents

		except Exception as inst:
			if(self.debugMode): print inst

			return None
		
#######################################################################
		
	def getRandomRecipe(self):
		try:
			
			if self.getTrending() is not None:
				recipes = self.getTrending()['recipes']	
				random.shuffle(recipes)
				return recipes[0]
			else:
				if self.getTopRated() is not None:
					recipes = self.getTrending()['recipes']	
					random.shuffle(recipes)
					return recipes[0]					
				
				
		except Exception as inst:
			if(self.debugMode): print inst

			return None		
	
	def getRandomRecipeID(self):
		try:
			
			recipe = self.getRandomRecipe()
			return recipe['recipe_id']
		except Exception as inst:
			if(self.debugMode): print inst

			return None		
	
	
#1a2a2d741db9a9c3c4bffe2de393d3ee pri