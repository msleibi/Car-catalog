#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Properties

app = Flask(__name__)

engine = create_engine('sqlite:///carcatalogapp.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#All Categories
@app.route('/')
@app.route('/categories/')
def categoriesMenu():
    category = session.query(Categories).all()
        
    return render_template('categoriesMenu.html',category=category)

# CREATE NEW CATEGORY
@app.route('/categories/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCat = Categories(name=request.form['name'])
        session.add(newCat)
        session.commit()
        flash("new category " + newCat.name  + " created!")
        return redirect(url_for('categoriesMenu'))
    else:
	return render_template('newCategory.html')
        

# EDIT EXISTING CATEGORY
@app.route('/categories/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    
    editCat = session.query(Categories).filter_by(id=category_id).one()
    if request.method =='POST':
        editCat.name = request.form['name']
        session.add(editCat)
        session.commit()
        flash("Category has been edited")
        return redirect(url_for('categoriesMenu'))
    else:
        return render_template('editCategory.html',category = editCat,category_id=editCat.id)
    
# DELETE EXISTING CATEGORY
@app.route('/categories/<int:category_id>/delete',methods=['GET', 'POST'])
def deleteCategory(category_id):
    deleteCat = session.query(Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(deleteCat)
        session.commit()
        flash(deleteCat.name + " has been deleted")
        return redirect(url_for('categoriesMenu'))
    else:
        return render_template('deleteCategory.html', deleteCategory=deleteCat)


#Show category properties
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/properties')
def categoryProperties(category_id):
    CarOne = session.query(Categories).filter_by(id=category_id).one()
    properties = session.query(Properties).filter_by(categories_id=category_id)
    
    return render_template('propertiesMenu.html',car = CarOne,properties = properties, category_id = category_id)


#Show property description
@app.route('/category/<int:category_id>/properties/<int:property_id>/')
def showPropertyDescription(category_id, property_id):

    return render_template('propertyDescription.html')


# Add property
@app.route('/category/<int:category_id>/properties/new')
def newCategoryProperty(category_id):

    return render_template('newProperty.html')

# Edit property
@app.route('/category/<int:category_id>/properties/<int:property_id>/edit')
def editCategoryProperty(category_id, property_id):

    return render_template('editProperty.html')


# Delete property
@app.route('/category/<int:category_id>/properties/<int:property_id>/delete')
def deleteCategoryProperty(category_id, property_id):

    return render_template('deleteProperty.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
