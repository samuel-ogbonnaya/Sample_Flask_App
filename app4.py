# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:39:13 2019

@author: isogb
"""

from flask import Flask, render_template

app = Flask(__name__)  ##Instantiates the Flask class

@app.route('/')
def home():
    #return " Home Page"
    return render_template("home.html")


@app.route('/about/')
def about():
    #return "about page"
    return render_template("about.html")


if __name__ == "__main__": #run the app when when the scirpt is the one being written
    app.run(debug=True)
    



