 
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



   

