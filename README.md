# TescoCheapRecipe
An flask based mashup that uses Tesco API (to find ingredients and prices) and food2fork API (to find recipes)


The end goal for this web app is to give a way to find cheap meals from Tesco (UK groceries store). Ideally one of the feature would be to search for ingredients 
and the webapp should give you some meals that are cheap to make, according to the price of the ingredients from Tesco.

This is just a project to learn Flask, so don't mind to much the code being messy and ugly, I plan to fix that, eventually.


## Installation

You need to have Python 2.7 installed.
You need to have Flask installed : http://flask.pocoo.org/docs/0.11/installation/ .


Then you need to request a:

- Tesco apikey from: https://devportal.tescolabs.com/
- food2fork apikey from: http://food2fork.com/about/api

Then place these two apikeys in the [apikey.cfg]()

You are now ready to run TescoCheapRecipe locally using Flask builtin debug server.
Download the repo, navigate inside it then run:

In Windows:
```
$ set FLASK_APP=main
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 ```
 
Otherwise:
```
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```
 
Finally on your browser navigate to
http://127.0.0.1:5000/

## Todo List
- []Add price function to get the "cost" of a recipe
- []Allow search for cheapest recipe
- []Clean up code / add WTForms
- []Create nice CSS style
