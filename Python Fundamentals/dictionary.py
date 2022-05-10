'''  dictionary stores key-value pairs, where each unique key is an indes which holds the value
    associated with it 
    
    They are unordered as the values are not stored in a linear structure  '''


empty_dict = {}

dict1 = { "Batman" : 55,
         1 : "Manga",
         "Try it":  96}

print(dict1)


### dictionaries can also be defined with the dict() constructor ###
phone_book = dict(Batman = 33, Cersei = 34)
print(phone_book)

## Alternative approach
phone_book2 = dict([('Batman' , 1),
                    ('Cersei' ,2),
                    ('Busters', 33)])

print(phone_book2)

## accessing values using get(). Enter the key
print(phone_book.get('Batman'))
print(phone_book['Batman'])

## Adding values
phone_book['New value'] = 90

## Updating values
phone_book['New value'] = 100

## Removing entry using del keyword
del phone_book['New value']

## Removing using pop
batman  = phone_book.pop('Batman')
print(phone_book)
print(batman)

###  Removing using pop item. REMOVES THE LAST INSERTED ITEM
last_added = phone_book.popitem()
print("Last added item: " ,last_added)

### Copy items using update()
phone_book_new = {'New items' : 77, 'New item2' : 56}
phone_book2.update(phone_book_new)
print("Updated phone book 2 with phone book new: ", phone_book2)

### dictionary comprehensions. Adds '!' to the strings and 100 to values
phone_book_comprehension = {item + '!' : n+100 for (item, n) in phone_book2.items()}
print("Phone book comprehension: ", phone_book_comprehension)

