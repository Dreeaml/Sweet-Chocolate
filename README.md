## Sweet Chocolate
The project is a database-driven online recipe book. Convining Flask to create the application, MongoDB as a non-relational database to store data and python as programming language for the funcionalities, creates a clever and usufull interface for the public. This demostrate one more time the power of coding and what is possible to build.

## UX
Sweet chocolate is a Recipe Book for those passionates of sweets, cakes and confectionery. The aim of this webside is to provide an interface to create, edit, store and share sweet recipes with the rest of the world.

More specificly, Sweet Chocolate has a ***Home*** page where users can see all created recipes and open them. An ***Add recipe*** buttom to create and insert a recipe in the database and therefore include it in the main view where is accesible for everyone. In this section, users are able to write and choose the information related to the recipe such as name, description, category, cooking time, difficulty, ingredients and instructions.

Additionally,  a ***Manage categories*** button is included in the navbar where is possible to create new categories, delete, edit and update existing ones.


  

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

  
Here can be found some diagrams and mockups: [Click here]()

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

  ### Existing Features

 - [Home page with recipes previews](https://github.com/Dreeaml/Sweet-Chocolate/blob/master/templates/recipes.html)
 - [Show recipe](https://github.com/Dreeaml/Sweet-Chocolate/blob/master/templates/show_recipe.html) page that amplifies the preview of each recipe.
 - [Add recipe page](https://github.com/Dreeaml/Sweet-Chocolate/blob/master/templates/add_recipe.html)
 - [Manage categories page](https://github.com/Dreeaml/Sweet-Chocolate/blob/master/templates/categories.html)
 - [Add](https://github.com/Dreeaml/Sweet-Chocolate/blob/master/templates/addcategory.html) and [edit](https://github.com/Dreeaml/Sweet-Chocolate/blob/master/templates/editcategory.html) pages for categories.
 
### Features Left to Implement

The idea is to convert it into an Instagram style platform but specially for chefs, food and kirchen lovers. Including users accounts, follower and following options, share options, ect.
 
## Technologies Used

-   Python 3.4.3
-   Flask (Python Microframework)
-   BootStrap 3
-   Google Fonts
-   JavaScript
-   CSS
-   HTML
-   Materialize


## Testing

#### Testing Add Recipe Form

-   Test that a new added recipe immediately appears on the website's homepage
-   Go to the form and try to submit empty inputs to make sure that the "required" message appear.
- Go to Add recipe and make sure the database is connected.
- Ensure that if a category is edited, the changes will also appear in the recipes that have used it.
-  Test that the select fields are producing the correct options.

#### Testing Edit Categories

-   Make sure that the form is being populated with the correct data from the MongoDB document when editing recipe.
-   Ensure a category is able to be updated more than once without any bugs occuring (such as fields going missing or name clashes causing issues)

#### Other Tests

-   Make sure the 'delete category' functionality is removing the correct document.
-   Ensure that newly added categories become available on the add recipe form.
-   Make sure removing a cuisine that recipes have as their cuisine doesn't cause the website to crash.
-   Test responsiveness of each page on different screen sizes and ensure all elements stay readable. 
- The webside is tried in Responsinator ([https://www.responsinator.com/](https://www.responsinator.com/)) to check if all the media queries fit in Iphone, tablets and laptop screens. 

## Data
The database is structured with four collections, recipes, categories, difficulty and duration. Recipes and categories are related since users can edit/edit categories, so those changes can be reflected also in recipe that use that categorie.

The recipes document itself contains unstuctured data. With key/value pairs that make up a description of the recipe. 

## Deployment
his site is hosted using GitHub pages, deployed directly from the master branch. To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/Dreeaml/Sweet-Chocolate.git.

The project is deployed on [Heroku]([https://sweet-chocolate.herokuapp.com/](https://sweet-chocolate.herokuapp.com/))
  

## Credits

### Media

The backgroud photo used in this site was obtained from [Unsplash](https://unsplash.com/).
The favicon was generated with [Favicon.ico]([https://www.favicon-generator.org/](https://www.favicon-generator.org/))

## Acknowledgements

I received inspiration for this project from [Cooking Ideas](http://cooking-ideas.herokuapp.com/index), [Live to cook](https://online-cookbook-js.herokuapp.com/), [Task Manager](https://github.com/Code-Institute-Solutions/TaskManager/tree/master/07-AddingApplicationNavigation/01-adding_a_navigation_bar).