import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'sweet_chocolate'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_URI"] = 'mongodb+srv://dreeaml_06:qV8hoAKKPSmzZB7v@myfirstcluster-aklf4.mongodb.net/sweet_chocolate?retryWrites=true&w=majority'

mongo = PyMongo(app)

#home with all recipes
@app.route('/')
@app.route('/get_recipes') 
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())

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
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for("get_recipes"))

#open a recipe
@app.route('/show_recipe/<recipe_id>/')
def show_recipe(recipe_id):
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
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
    categories=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

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