#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items

app = Flask(__name__)

engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#All Categories
@app.route('/')
@app.route('/categories')
def categoriesMenu():
    
    return "This page show all categories"

#Show category items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items')
def categoryItems(category_id):

    return "This page show category: "+str(category_id)+" items"


#Show item description
@app.route('/category/<int:category_id>/items/<int:item_id>/')
def showItemDescription(category_id, item_id):

    return "This page show category: "+str(category_id)+" and item: "+str(item_id)


# Add item
@app.route('/category/<int:category_id>/items/new')
def newCategoryItem(category_id):

    return "This page create new category item"

# Edit item
@app.route('/category/<int:category_id>/items/<int:item_id>/edit')
def editCategoryItem(category_id, item_id):

    return "This page edit category: "+str(category_id)+ " item: "+str(item_id)


# Delete item
@app.route('/category/<int:category_id>/items/<int:item_id>/delete')
def deleteCategoryItem(category_id, item_id):

    return "This page delete category: "+str(category_id)+" item: "+str(item_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
