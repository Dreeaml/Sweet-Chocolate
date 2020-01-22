import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

app = Flask(__name__)
load_dotenv()

app.config["MONGO_DBNAME"] = 'sweet_chocolate'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

#home with all recipes
@app.route('/')
@app.route('/get_recipes') 
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    categories = list(mongo.db.categories.find())
    for recipe in recipes : 
        recipe["category_name"] = list(filter(lambda x: x["_id"] == recipe["category_name"] , categories))[0]["category_name"]
    return render_template('recipes.html', recipes=recipes)

#create new recipe
@app.route('/add_recipe') 
def add_recipe():
    return render_template('add_recipe.html', 
                categories=mongo.db.categories.find(), 
                duration=mongo.db.duration.find(),
                difficulty=mongo.db.difficulty.find(),
                )

@app.route('/insert_recipe/', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    category = mongo.db.categories.find_one({"category_name": request.form.to_dict()["category_name"]})
    post_data = request.form.to_dict()
    post_data["category_name"] = ObjectId(category.get('_id')) 
    recipes.insert_one(post_data)
    return redirect(url_for("get_recipes"))

#open a recipe
@app.route('/show_recipe/<recipe_id>', methods=['GET'])
def show_recipe(recipe_id):
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("show_recipe.html", recipe=recipe_id)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    mongo.db.recipes.update(
        {'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

#categories create, delete, edit, update and insert.

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                           {'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))

@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', "3000")),
            debug=True)