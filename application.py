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
@app.route('/categories/')
def categoriesMenu():
    category = session.query(Categories).all()
    
    
    return render_template('categories.html',category=category)

#Show category items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items')
def categoryItems(category_id):


    
    return render_template('items.html')



#Show item description
@app.route('/category/<int:category_id>/items/<int:item_id>/')
def showItemDescription(category_id, item_id):

    
    return render_template('itemDescription.html')


# Add item
@app.route('/category/<int:category_id>/items/new')
def newCategoryItem(category_id):

    return render_template('newItem.html')

# Edit item
@app.route('/category/<int:category_id>/items/<int:item_id>/edit')
def editCategoryItem(category_id, item_id):

    return render_template('editItem.html')


# Delete item
@app.route('/category/<int:category_id>/items/<int:item_id>/delete')
def deleteCategoryItem(category_id, item_id):

    return render_template('deleteItem.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
