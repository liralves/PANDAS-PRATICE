import panda as pd

#1.In the cell below, create a DataFrame `fruits` with Apples and Bananas:
pd.DataFrame({'Apples': [30], 'Bananas': [21]}) 

# 2. Create a dataframe `fruit_sales` that matches the diagram below:
pd.DataFrame({'Apples': ['31', '45'], 'Bananas': ['21', '41']}, index=['2017 Sales', '2018 Sales'])

# 3. Create a variable `ingredients` with a Series that looks like:
"""Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object """
ingredientes = ['4 cups', '1 cup', '2 large', '1 can']
pd.Series(ingredientes, index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# 4. Read the following csv dataset of wine reviews into a DataFrame called `reviews`:
reviews = pd.read_csv("/content/winemag-data-130k-v2.csv.zip")
reviews.shape
reviews.head()

# 5. Run the cell below to create and display a DataFrame called `animals`:
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

#In the cell below, write code to save this DataFrame to disk as a csv file with the name `cows_and_goats.csv`.
animals.to_csv("cows_and_goats.csv")
