## 1. If Statements ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)

avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)
                                        
                                    

## 2. Booleans ##

a_price = 0
if a_price == 0:
    print('This is free')
if a_price == 1:
    print('This is not free')
    

## 3. The Average Rating of Non-free Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_apps_ratings = []
for each_row in apps_data[1:]:
    rating =float (each_row[7])
    price =float (each_row[4])
    if price != 0.0: 
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free= sum(non_free_apps_ratings)/len(non_free_apps_ratings)  
print(round(avg_rating_non_free))

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_games_ratings =[]

for row in apps_data[1:]:
    rating = float(row[7])
    genre = str(row[11])
    
    if genre != 'Games':
        non_games_ratings.append(rating)
    
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)    
    
    
    

## 5. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    
    if price == 0.0 and genre =='Games':
        free_games_ratings.append(rating)
    
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)                              
    
    

## 6. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == "Social Networking" or genre=="Games":
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings)/len(games_social_ratings)        
        
    

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price !=0:
        non_free_games_social_ratings.append(rating)
        
avg_non_free = float(sum(non_free_games_social_ratings) / len(non_free_games_social_ratings))

# Non-free apps (average)

## 9. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

ratings= []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float (row[4])
    
    if price > 9:
        ratings.append(rating)
    
    
avg_rating =sum(ratings)/len(ratings)
n_apps_more_9 = len(ratings)
n_apps_less_9 = len (apps_data[1:])- len(ratings)
    

    
    
    

## 11. The elif Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0:
        app.append("free")
    elif price > 0 and price < 20:
        app.append("affordable")
    elif price >= 20 and price <50:
            app.append( "expensive")
    elif price >= 50:
            app. append( "very expensive") 

(apps_data[0]).append('price_label')
print(apps_data[:6])
        