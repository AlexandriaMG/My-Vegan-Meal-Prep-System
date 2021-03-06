# My-Vegan-Meal-Prep-System

## Welcome!
Hi! I am Alexandria and welcome to the overview of my project! I would like to share the journey I am going on to solve my meal prepping problem. I hope it inspires you to find ways to automate some tasks so your time can be spent doing the things you love.

## Background
I LOVE cooking, more particularly I love making vegan recipes. I currently have 17 vegan cookbooks and 8 vegan food blogs I follows. When doing my weekly prep, I go through several of these sources to get inspiration for what I want to make. This is time consuming! There are times were this is enjoyable but when done EVERY week it can be overwhelming, as I am also a full time mom of two little ones, part time graduate student, and currently looking for a job. I want to steamline this process by having a system give me a few suggestions. I also want this system to make my grocery list since this is my least favorite task in meal prepping. 

## Process

### Problem

How can I reduse the time it takes me to meal prep while still using the resources I already have?

#### Objective
I plan to make a system to recommend several recipes and make a grocery list for the recipes I choose. The system
should be able to take feedback on the recipes I did or did not pick and update itself accordingly and return a grocery
list of all my chosen recipes for the week. 
        
#### Measures
How much does my meal prep time reduce? What is it currently? Do I stick with the meal prep more often? Currently I don't always commit to my meal prep if I don't make my grocery list first.
              

### Collecting The Data 

I have 17 cookbooks and 8 vegan blogs that I want to collect recipe data from. I am going to use a scan to an ORC (Optical Character Recognition) system for the cookbooks and make a web spider for the blogs.   

I used CamScanner app to take pictures of the cookbook's index and (http://www.free-online-ocr.com/) for the ORC system to copy and paste the names of the recipes. I in put other variables by hand because this was the most time-efficent way I could think of. 


### Tables

#### Recipe Table
Recipe ID: an unique identification number for each recipe     
Name: the name of the recipe  
Aurthor: the person who wrote the recipe  
Main_Source: the name of the cookbook or blog  
Sub_Source: the page number or weblink  
Cooktime: the complete time in minutes it takes the make the recipe    
Cuisine: culture who the recipe is inspired by  
Type: the type of recipe is, (ex. Salad, Soup, Entree, Breakfast, Dessert)   
Gluten-Free: recipe does not include gluten, 0-no and 1-yes    
Nut_Free: recipe does not include nut, 0-no and 1-yes   
Oil_Free: recipe does not include oil, 0-no and 1-yes   
Soy_Free: recipe does not include soy, 0-no and 1-yes    
No_Added_Sugar: recipe does not any added sugar, 0-no and 1-yes   
Refined_Sugar_Free: recipe does not include refined sugars like can sugar, 0-no and 1-yes   
Raw: recipe does not need to be cooked on the stove or baked, 0-no and 1-yes  
Last_Made: the last time I made the recipe (MM-DD-YYYY)


#### Ingredient Table
Ingredient ID: an unique identification each ingredient   
Ingredient: the name of each ingredient    

#### Grocery Table
Recipe ID: an unique identification number for each recipe     
Ingredient ID: an unique identification each ingredient       
Amount: the numerical value associated with the amount of the ingredient in the recipe       
Measurement: the way in which the ingredient is measured (ex. tbs)       

