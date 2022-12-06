# the authors' names are: Cadyn and Sarah
limit = 140
def too_long(x):
    if x < limit:
        print(x, "characters can be sent in a SMS message")
    else:
        print(x, "characters is too long to be sent in a SMS message")


too_long(100)
too_long(150)


#practice
#unicodedata.lookup("snake")
#unicodedata.lookup("dog")
#unicodedata.lookup("rose")

#unicodedata.lookup("sun")
#unicodedata.lookup("cat")
#unicodedata.lookup("two hearts")

#len("The (insert rose emoji) is red")
#len("The (insert sun emoji) is yellow")
#len("I hate (insert snake emoji")
#len("insert the snake, dog, rose, sun, cat, and heart emoji")
#len("I love (insert dog emoji")

import unicodedata
unicodedata.name("*")
unicodedata.name("{")
unicodedata.name("&")
unicodedata.name("[")
unicodedata.name("/")
