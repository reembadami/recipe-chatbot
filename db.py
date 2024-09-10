import sqlite3
import json
import csv
import re

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

print("Opened database successfully")

conn.execute(
    '''CREATE TABLE RECIPE_TABLE (
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        MINUTES INT,
        STEPS TEXT NOT NULL,
        NO_STEPS INT,
        DESCRIPTION TEXT,
        INGREDIENTS TEXT,
        NO_INGREDIENTS INT
    );'''
)

file = list(csv.DictReader(open('RAW_recipes.csv', encoding="utf-8")))

for idx, recipe in enumerate(file):
    if idx < 2000:
        recipe_id = recipe["id"]
        name = recipe["name"]
        minutes = recipe["minutes"]
        
        # Steps - list
        steps = recipe["steps"]
        steps = re.sub("(',\s')", ", ", steps)
        res = steps.strip('][').split(', ') # converts list which is a string to a list
        steps_para = ''
        for idx, step in enumerate(res):
            try:
                if idx == 0:
                    formatting = step[1].upper() + step[2:]
                else:
                    formatting = step[0].upper() + step[1:]
            except:
                formatting = step
            step = str(idx+1) + ") " + formatting
            step = step.replace("\'", "")
            steps_para = steps_para + step + ", "

        n_steps = recipe["n_steps"]
        description = recipe["description"]

        # Ingredients - list
        ingredients = recipe["ingredients"]
        res = ingredients.strip('][').split(', ')
        ingredients_para = ''
        for ingredient in res:
            ingredient = ingredient.replace("\'", "")
            ingredients_para = ingredients_para + ingredient + ","

        n_ingredients = recipe["n_ingredients"]

        params = (
            recipe_id, name, minutes, steps_para, n_steps, description, ingredients_para, n_ingredients
        )

        cursor.execute(f"INSERT INTO RECIPE_TABLE VALUES (?, ?, ?, ?, ?, ?, ?, ?)", params)
        conn.commit()
    else:
        break

conn.close()







# cursor = conn.execute("SELECT ID, NAME, MINUTES, NO_STEPS, DESCRIPTION, NO_INGREDIENTS from RECIPE_TABLE")
# for row in cursor:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("MINUTES = ", row[2])
#    print("NO_STEPS = ", row[3])
#    print("DESCRIPTION = ", row[4])
#    print("NO_INGREDIENTS = ", row[5], "\n")