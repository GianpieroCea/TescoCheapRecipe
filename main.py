
from flask import Flask, render_template, redirect, url_for, jsonify,request
from tescoSearch import tescoSearch
from food2fork import food2fork
import urllib
app = Flask(__name__)

@app.route("/")
def index():
    #when random button is pressed give a random recipe
    if request.args.get("random") == "Go": 
        id= food2fork().getRandomRecipeID()  
        return redirect(url_for('show_recipe', id =id))
    
    
    #search the tesco database
    if (request.args.get("ingredients")) is not None : 
        #naively validates input
        query = (request.args.get("ingredients")).lower()
        query = urllib.quote_plus(query)  #very important,yay!
        tesco = tescoSearch(query).getResults()    
        return render_template('show_ingredients.html', tesco = tesco , query = query)
    
    #search the food2fork database
    if (request.args.get("ingredients_rec")) is not None: 
        query = (request.args.get("ingredients_rec")).lower()
        query = urllib.quote_plus(query)  #very important,yay!
        f2f = food2fork().search(query) 
        #this should be made into a food2fork method
        if f2f is not None:
            id = f2f['recipes'][1]['recipe_id']
            
        return redirect(url_for('show_recipe', id=id))
    
    
    return render_template('index.html')
    
    

      
    
    
@app.route("/recipe/<id>")
def show_recipe(id):
    f2f = food2fork()
    recipe = f2f.getRecipe(id)
    if recipe is not None:
        title = recipe['recipe']['title']
        ingredients = recipe['recipe']['ingredients']
        source_url = recipe['recipe']['source_url']
        return render_template('show_recipe.html' , title = title ,ingredients= ingredients, source_url = source_url)
        
        

#############################################


if __name__ == "__main__":
    app.run()