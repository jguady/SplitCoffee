# SplitCoffee
A simple CLI app to determine who's turn it is to pay for coffee during lunch


# Running the Program

# Tests

# Github Actions

# Assumptions
The Following assumptions were made when creating the program
 - The group decides that the fairest way to take turns paying based on an internal score. 
   - This score is made up of previous purchase history
 - Items are only recorded in memory and not recalled in between runs.
   - Since this is just a proof of concept, no information will be retained until more requirements are defined.
     - Either a SQL or No-SQL db would be appropriate for this kind of data. 
 - People will always order something that is actually on the menu. 
   - If their favorite drink is on the menu they have a high likelihood of ordering it see: [Person.py](splitcoffee/model/Person.py)
 - Inflation doesn't exist, though prices can change (see below)
 - Each person only has 1 favorite
   - Jim only likes Drip coffee, not all non-dairy based drinks which could be considered "Black"

# Manipulate Data

## Changing the People


## Changing the Menu

### Adding Items to the Menu

