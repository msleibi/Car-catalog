#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items

app = Flask(__name__)

engine = create_engine('sqlite:///catalogapp.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#All Categories
@app.route('/')
@app.route('/categories/')
def categoriesMenu():
    category = session.query(Categories).all()
    lastItems = session.query(Items).order_by(desc("createdate")).limit(10)
        
    return render_template('categoriesMenu.html',category=category,lastItems = lastItems)

# CREATE NEW CATEGORY
@app.route('/categories/new', methods=['GET', 'POST'])

def newCategory():
    if request.method == 'POST':
        newCat = Categories(name=request.form['name'])
        session.add(newCat)
        session.commit()
        flash("new category %s has been created!" % (newCat.name))
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
        flash( '%s has been edited' % (editCat.name))
        return redirect(url_for('categoryItems',category_id=editCat.id))
    else:
        return render_template('editCategory.html',categ = editCat,category_id=editCat.id)
    
# DELETE EXISTING CATEGORY
@app.route('/categories/<int:category_id>/delete',methods=['GET', 'POST'])
def deleteCategory(category_id):
    deleteCat = session.query(Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(deleteCat)
        session.commit()
        flash(' %s has been deleted' % (deleteCat.name))
        return redirect(url_for('categoriesMenu'))
    else:
        return render_template('deleteCategory.html', deleteCategory=deleteCat)


#Show category items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items')
def categoryItems(category_id):
    CatOne = session.query(Categories).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(categories_id=category_id)
    
    return render_template('itemsMenu.html',categ = CatOne,items=items)


# Add item
@app.route('/category/<int:category_id>/items/new',methods=['GET','POST'])
def newCategoryItem(category_id):
    CatOne = session.query(Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Items(name = request.form['name'], description = request.form['description'], price = request.form['price'],manufacture = request.form['manufacture'] , categories_id = category_id)
        session.add(newItem)
        session.commit()
        flash('New Menu %s Item Successfully created' % (newItem.name))
        return redirect(url_for('categoryItems', category_id = CatOne.id ))
    else:
        return render_template('newItem.html',category_id = CatOne.id,categ = CatOne)

# Edit item
@app.route('/category/<int:category_id>/items/<int:item_id>/edit',methods=['GET','POST'])
def editCategoryItem(category_id, item_id):
    CatOne = session.query(Categories).filter_by(id=category_id).one()
    editedItem = session.query(Items).filter_by(id=item_id).one()
    if request.method == 'POST':
        editedItem.name = request.form['name']
        editedItem.description = request.form['description']
        editedItem.price = request.form['price']
        editedItem.manufacture = request.form['manufacture'] 
        session.add(editedItem)
        session.commit()
        flash('Menu %s Item Successfully edited' % (editedItem.name))
        return redirect(url_for('categoryItems', category_id = CatOne.id))
    else:
        return render_template('editItem.html',categ = CatOne,item = editedItem)


# Delete item
@app.route('/category/<int:category_id>/items/<int:item_id>/delete',methods=['GET','POST'])
def deleteCategoryItem(category_id, item_id):
    CatOne = session.query(Categories).filter_by(id=category_id).one()
    itemToDelete = session.query(Items).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Menu %s Item Successfully deleted' % (itemToDelete.name))
        return redirect(url_for('categoryItems', category_id = CatOne.id))
    else:
        return render_template('deleteItem.html',categ = CatOne,item =itemToDelete )


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
