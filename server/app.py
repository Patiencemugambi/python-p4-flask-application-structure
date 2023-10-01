#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)   #


# Decorators are functions that take other functions as arguments, 
# extend their behavior in some way, and then return them or another function. 
# eg @app.route()

# define routes 

@app.route('/')   #(/) base URL 
def index():      # view - functions that map to the url. they return the rsponse that the client delivers to the user. 
                  #  eg view index() returns the HTML code 
    return '<h1>Welcome to my page!</h1>'

# append to server/app.py

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
    app.run(port=5556, debug= True)    