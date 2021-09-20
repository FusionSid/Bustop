# Bustop

Website: https://bustop-api.fusionsid.repl.co

Categories: Name, Place, Animal, Food, Color, Movie

This is a 3 in one python app for the game bustop. It includes:
- Website
- Database
- API (Flask REST) - its not really an api i just like to call it that

When you got to the (poorly designed little to no css) website, You have 3 options.

Bustop:

When you go on this page you have to input a letter. Once you input a letter you will get a list of items per categories (see categories above) starting with that letter.

Insert:

Lets you insert values into the database. Adding to the database helps everyone.

Search:

Lets you search for things.

API:

All values in the database can accessed with the requests module in python. 
By changing the website address to certain thing which i will specify bellow can return json information from the database.

Here is the default url: https://bustop-api.fusionsid.repl.co
Examples:

Get all:
/api/letter=<letter>/
```response = requests.get(https://bustop-api.fusionsid.repl.co/api/letter=a/)```
That will return anything related to the letter a

Get specific things:
/api/<letter>/<thing>/
 ```response = requests.get(https://bustop-api.fusionsid.repl.co/api/a/name/)```
 That will return all names(stored in the database) starting with the letter a
