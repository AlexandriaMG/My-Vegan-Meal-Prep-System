#Alexandria Morales-Garcia
#Vegan Meal Prep Project 

#Reccomdation System


from sympy import jn
import sqlite3

conn = sqlite3.connect('Recipe_database.db')
c = conn.cursor()

def createTables():
    'Puts Recipe, Ingredents, and Grocery tables in SQL Light'
    
    #Define Tables and columns
    recipesTable = '''CREATE TABLE Recipes(
               RecipeID     INTEGER NOT NULL,
               Name      VARCHAR(100),
               Aurthor     VARCHAR(50),
               MainSource      VARCHAR(200),
               SubSource      VARCHAR(200),
               Cooktime     NUMERIC(6,2),
               Cuisine    VARCHAR(25),
               TypeR      VARCHAR(25),
               GlutenFree       BOOL,
               NutFree       BOOL, 
               OilFree       BOOL,
               SoyFree       BOOL,
               NoAddedSugar       BOOL,
               RefinedSugarFree       BOOL,
               RawR       BOOL,
               LastMade      VARCHAR(10),
               
               PRIMARY KEY (RecipeID) 
          );'''
    
    ingredientsTable= '''CREATE TABLE Ingredients (
               IngredientId     INTEGER NOT NULL,
               Ingredient      VARCHAR(100),
               
               PRIMARY KEY (IngredientId) 
          );'''

    groceryTable= '''CREATE TABLE Grocery (
               RecipeID     INTEGER NOT NULL,
               IngredientId     INTEGER NOT NULL,
               Amount      DECIMAL(6, 3),
               Measurement  VARCHAR(10),

               PRIMARY KEY (RecipeID, IngredientId), 
               FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID),
               FOREIGN KEY (IngredientId) REFERENCES Ingredients(IngredientId)
          );'''

    # Runs the code in SQL light 
    c.execute('DROP TABLE IF EXISTS Recipes;')
    c.execute(recipesTable)
    c.execute('DROP TABLE IF EXISTS Ingredients;')
    c.execute(ingredientsTable)
    c.execute('DROP TABLE IF EXISTS Grocery;')
    c.execute(groceryTable)
    
    #teseting 
    newData = [ 1,'Cinnamony French Toast with Apple Compote', 'Hannah Sunderani','The Two Spoons Cookbook',29,30,'French','Breakfast',0,0,0,0,0,1,0,'NA']
    newData2= [1, 'apple']
    newData3= [1,1,4,'each']
    c.execute('Insert into  Recipes VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);',newData)
    c.execute('Insert into  Ingredients VALUES(?,?);',newData2)
    c.execute('Insert into  Grocery VALUES(?,?,?,?);',newData3)
    print(c.execute('Select * from Recipes ;').fetchall())
    print(c.execute('Select * from Ingredients ;').fetchall())
    print(c.execute('Select * from Grocery ;').fetchall())

createTables()

def Questions():
    'Asks a series of cooking questions and return an answer list'
    answers = [] 
    print("How many suggestions would you like?" ) 
    answers.append(input())
    print("How many recipes would you like this to aply to?")
    answers.append(input())
    print("How long would you like to spend cooking?" ) 
    answers.append(input())
    print("What types of recipes are you looking for? (breakfast, entree, snack, dessert)" ) 
    answers.append(input())
    print("Are there any diet ristrictions you would like for some or all recipes?")
    answers.append(input())
    print("How many recipes would you like this to aply to?")
    answers.append(input())
    return answers




#Grocery List

#def inSQL():
   # import sqlite3 as sql 

    


