
from flask import Flask, render_template, redirect, url_for, jsonify,request
from tescoSearch import tescoSearch
from food2fork import food2fork
import urllib
app = Flask(__name__)

@app.route("/")
def index():
    if (request.args.get("ingredients")) is not None: 
        query = (request.args.get("ingredients")).lower()
        query = urllib.quote_plus(query)  #very important,yay!
        tesco = tescoSearch(query).getResults()    
        return render_template('index.html', tesco = tesco)
    else:
        return render_template('index.html')
    
    
    if (request.args.get("ingredients_rec")) is not None: 
            query = (request.args.get("ingredients_rec")).lower()
            query = urllib.quote_plus(query)  #very important,yay!
            f2f = food2fork().search(query)    
            return render_template('index.html', tesco = tesco)
        else:
            return render_template('index.html')
    
    
@app.route("/recipe/<id>")
def show_recipe(id):
    f2f = food2fork()
    if f2f.getRecipe(id) is not None:
        title = f2f.getRecipe(id)['recipe']['title']
        ingredients = f2f.getRecipe(id)['recipe']['ingredients']
        source_url = f2f.getRecipe(id)['recipe']['source_url']
        return render_template('show_recipe.html' , title = title ,ingredients= ingredients, source_url = source_url)
        
        

#############################################


if __name__ == "__main__":
    app.run()