#  Created by KAR:
#
#  Kyle Awah     - (816012635)
#  Avita John    - (816012533)
#  Riandra Maraj - (816010975)
#  Kyle Sukhdeo  - (816014143)
#
#  AFTR_MARKT
#  (Group Project - Storefront)
#  INFO 2602 - Web Programming and Technologies 1
#
#  main.py contains:
#  - Setup for Flask
#  - Paths For The Server

import json
from flask_cors import CORS
from flask import Flask, request, render_template, flash, url_for, redirect, Markup, session
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from models import db, product_tee, product_jacket, product_pants, product_shoes, product_acc, user
from forms import SignUp, LogIn, EditUser
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

# Flask Login Function #
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return user.query.get(user_id)
##################################

# Boilerplate #
def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AFTR_MARKT_MAIN_DATABASE.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "MYSECRET"
    CORS(app)
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7)
    login_manager.init_app(app)
    db.init_app(app)
    return app
app = create_app()
app.app_context().push()
########################






# Function To Add More Than one item together into a single python dictionary for session shopping cart #
def MergeDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        list1 = list(dict1.items())
        list2 = list(dict2.items())
        return dict (list1 + list2)
    return False
########################






####   SERVER PATHS   ####

# Normal Server Paths #
@app.route('/', methods=['GET'])
def index():
    id = 1
    product_1 = product_tee.query.get(id)
    product_2 = product_jacket.query.get(id)
    product_3 = product_pants.query.get(id)
    product_4 = product_shoes.query.get(id)
    product_5 = product_acc.query.get(id)
    return render_template('index.html', product_1 = product_1, product_2=product_2, product_3=product_3, product_4=product_4, product_5=product_5)

@app.route('/index', methods=['GET'])
def index_2():
    id = 1
    product_1 = product_tee.query.get(id)
    product_2 = product_jacket.query.get(id)
    product_3 = product_pants.query.get(id)
    product_4 = product_shoes.query.get(id)
    product_5 = product_acc.query.get(id)
    return render_template('index.html', product_1 = product_1, product_2=product_2, product_3=product_3, product_4=product_4, product_5=product_5)

@app.route('/discover', methods=['GET'])
def discover():
    id = 1
    product_1 = product_tee.query.get(id)
    product_2 = product_jacket.query.get(id)
    product_3 = product_pants.query.get(id)
    product_4 = product_shoes.query.get(id)
    product_5 = product_acc.query.get(id)
    return render_template('Discover.html', product_1 = product_1, product_2=product_2, product_3=product_3, product_4=product_4, product_5=product_5)

@app.route('/tees', methods=['GET'])
def tees():
    tees_query = product_tee.query.all()
    return render_template('Tees.html', products = tees_query)

@app.route('/jackets', methods=['GET'])
def jackets():
    jackets_query = product_jacket.query.all()
    return render_template('Jackets.html', products = jackets_query)

@app.route('/pants', methods=['GET'])
def pants():
    pants_query = product_pants.query.all()
    return render_template('Pants.html', products = pants_query)

@app.route('/shoes', methods=['GET'])
def shoes():
    shoes_query = product_shoes.query.all()
    return render_template('Shoes.html', products = shoes_query)

@app.route('/accessories', methods=['GET'])
def accessories():
    acc_query = product_acc.query.all()
    return render_template('Accessories.html', products = acc_query)
########################################






# User / Login Server Paths #
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LogIn()
  if form.validate_on_submit():
    data = request.form
    User = user.query.filter_by(username = data['username']).first()
    if User and User.check_password(data['password']):
      login_user(User)
      if current_user.login_counter == 0:
        flash('Welcome to your new account ' + current_user.username + " we hope you'll enjoy your stay, Please Take this oppertunity to finish your account setup.....")
      elif current_user.login_counter != 0:
        flash('Welcome Back ' + current_user.username)
      return redirect(url_for('profile_page'))
    else:
      flash('Invalid Username or Password for Account, Please try again')
      return redirect(url_for('login'))
  return render_template('Login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        data = request.form
        newuser = user(username=data['username'], email=data['email'], login_counter = 0)
        newuser.set_password(data['password'])
        db.session.add(newuser)
        db.session.commit()
        flash('Account Succesfully Created!')
        return redirect(url_for('login'))
    return render_template('SignUp.html', form=form)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_page():
    return render_template('Logged_In_Profile.html')




@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditUser()
    edit_user = user.query.get(current_user.id)
    if form.validate_on_submit():
        data = request.form

        if data['email'] != " ":
          edit_user.email = data['email']
				
        if data['passsword'] != " ":
          edit_user.email = data['email']

        if data['shipping_address'] != " ":
          edit_user.email = data['shipping_address']

        if data['payment_method'] != " ":
          edit_user.email = data['payment_method']
				
        if data['payment_method_card_number'] != " ":
          edit_user.email = data['payment_method_card_number']

        db.session.commit()
        flash('Account Sucesfully Updated!')
        return redirect(url_for('profile_page'))
    return render_template('Edit_Logged_In_Profile.html', form=form)






@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    this_user = user.query.get(current_user.id)
    this_user.login_counter += 1
    db.session.commit()
    message = Markup("<strong> LOGGED OUT </strong>")
    flash (message + 'Goodbye ' + current_user.username)
    logout_user()
    return redirect(url_for('index'))

@app.route('/delete_account_ask', methods=['GET'])
@login_required
def delete_account_ask():
    return render_template('Delete_Profile_Ask.html')

@app.route('/delete_account', methods=['GET', 'DELETE'])
@login_required
def delete_account():
    this_user = user.query.get(current_user.id)
    db.session.delete(this_user)
    db.session.commit()
    message = Markup("<strong> ACCOUNT DELETED </strong>")
    flash (message + 'Goodbye ' + current_user.username + ' thank you for shopping with us!')
    logout_user()
    return redirect(url_for('index'))
#####################################






# Product Page Server Paths #
@app.route('/tees/<id>', methods=['GET'])
def load_a_tee(id):
    tees_query = product_tee.query.get(id)
    recomended_items = product_jacket.query.all()
    incart = False
    name = "tee_"+id
    if 'ShoppingCart' in session and len(session['ShoppingCart']) > 0:
      for key, item in session['ShoppingCart'].items():
        if key == name:
          incart = True
    return render_template('Product_Page.html', product = tees_query, product_type = "tees", recomended_items = recomended_items, incart = incart)



@app.route('/jackets/<id>', methods=['GET'])
def load_a_jacket(id):
    jackets_query = product_jacket.query.get(id)
    recomended_items = product_tee.query.all()
    incart = False
    name = "jacket_"+id
    if 'ShoppingCart' in session and len(session['ShoppingCart']) > 0:
      for key, item in session['ShoppingCart'].items():
        if key == name:
          incart = True
    return render_template('Product_Page.html', product = jackets_query, product_type = "jackets", recomended_items =recomended_items, incart = incart)

@app.route('/pants/<id>', methods=['GET'])
def load_a_pants(id):
    pants_query = product_pants.query.get(id)
    recomended_items = product_tee.query.all()
    incart = False
    name = "pants_"+id
    if 'ShoppingCart' in session and len(session['ShoppingCart']) > 0:
      for key, item in session['ShoppingCart'].items():
        if key == name:
          incart = True
    return render_template('Product_Page.html', product = pants_query, product_type = "pants", recomended_items =recomended_items, incart = incart)

@app.route('/shoes/<id>', methods=['GET'])
def load_a_shoes(id):
    shoes_query = product_shoes.query.get(id)
    recomended_items = product_jacket.query.all()
    incart = False
    name = "shoes_"+id
    if 'ShoppingCart' in session and len(session['ShoppingCart']) > 0:
      for key, item in session['ShoppingCart'].items():
        if key == name:
          incart = True
    return render_template('Product_Page.html', product = shoes_query, product_type = "shoes", recomended_items =recomended_items, incart = incart)

@app.route('/accessories/<id>', methods=['GET'])
def load_an_acc(id):
    accessories_query = product_acc.query.get(id)
    recomended_items = product_shoes.query.all()
    incart = False
    name = "acc_"+id
    if 'ShoppingCart' in session and len(session['ShoppingCart']) > 0:
      for key, item in session['ShoppingCart'].items():
        if key == name:
          incart = True
    return render_template('Product_Page.html', product = accessories_query, product_type = "accessories", recomended_items =recomended_items, incart = incart)
########################################






# ADD Product To Shopping Cart Server Paths #
@app.route('/tees/add_to_cart/<id>', methods=['GET'])
def add_to_cart_tee(id):
    add_tee = product_tee.query.get(id)
    add_cart_item = {"tee_"+id:{'id':id, 'price':add_tee.price,'name':add_tee.name, 'brand':add_tee.brand, 'size':add_tee.size, 'color':add_tee.color,'desc':add_tee.desc, 'catagory':add_tee.catagory}}
    if 'ShoppingCart' in session:
       session['ShoppingCart'] = MergeDicts(session['ShoppingCart'] , add_cart_item)
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_tee.name + " and " + str(len(session['ShoppingCart'])-1) + " other item(s) are waiting for you to check out!.....")
       return redirect(request.referrer)
    else:
       session['ShoppingCart'] = add_cart_item
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_tee.name + ' is waiting for you to check out!.....')
       return redirect(request.referrer)

@app.route('/jackets/add_to_cart/<id>', methods=['GET'])
def add_to_cart_jackets(id):
    add_jacket = product_jacket.query.get(id)
    add_cart_item = {"jacket_"+id:{'id':id, 'price':add_jacket.price,'name':add_jacket.name, 'brand':add_jacket.brand, 'size':add_jacket.size, 'color':add_jacket.color,'desc':add_jacket.desc, 'catagory':add_jacket.catagory}}
    if 'ShoppingCart' in session:
       session['ShoppingCart'] = MergeDicts(session['ShoppingCart'] , add_cart_item)
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_jacket.name + " and " + str(len(session['ShoppingCart'])-1) + " other item(s) are waiting for you to check out!.....")
       return redirect(request.referrer)
    else:
       session['ShoppingCart'] = add_cart_item
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_jacket.name + ' is waiting for you to check out!.....')
       return redirect(request.referrer)

@app.route('/pants/add_to_cart/<id>', methods=['GET'])
def add_to_cart_pants(id):
    add_pants = product_pants.query.get(id)
    add_cart_item = {"pants_"+id:{'id':id, 'price':add_pants.price,'name':add_pants.name, 'brand':add_pants.brand, 'size':add_pants.size, 'color':add_pants.color,'desc':add_pants.desc, 'catagory':add_pants.catagory}}
    if 'ShoppingCart' in session:
       session['ShoppingCart'] = MergeDicts(session['ShoppingCart'] , add_cart_item)
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_pants.name + " and " + str(len(session['ShoppingCart'])-1) + " other item(s) are waiting for you to check out!.....")
       return redirect(request.referrer)
    else:
       session['ShoppingCart'] = add_cart_item
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_pants.name + ' is waiting for you to check out!.....')
       return redirect(request.referrer)

@app.route('/shoes/add_to_cart/<id>', methods=['GET'])
def add_to_cart_shoes(id):
    add_shoes = product_shoes.query.get(id)
    add_cart_item = {"shoes_"+id:{'id':id, 'price':add_shoes.price,'name':add_shoes.name, 'brand':add_shoes.brand, 'size':add_shoes.size, 'color':add_shoes.color,'desc':add_shoes.desc, 'catagory':add_shoes.catagory}}
    if 'ShoppingCart' in session:
       session['ShoppingCart'] = MergeDicts(session['ShoppingCart'] , add_cart_item)
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_shoes.name + " and " + str(len(session['ShoppingCart'])-1) + " other item(s) are waiting for you to check out!.....")
       return redirect(request.referrer)
    else:
       session['ShoppingCart'] = add_cart_item
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_shoes.name + ' is waiting for you to check out!.....')
       return redirect(request.referrer)

@app.route('/accessories/add_to_cart/<id>', methods=['GET'])
def add_to_cart_accessories(id):
    add_accessories = product_acc.query.get(id)
    add_cart_item = {"acc_"+id:{'id':id, 'price':add_accessories.price,'name':add_accessories.name, 'brand':add_accessories.brand, 'color':add_accessories.color,'desc':add_accessories.desc, 'catagory':add_accessories.catagory}}
    if 'ShoppingCart' in session:
       session['ShoppingCart'] = MergeDicts(session['ShoppingCart'] , add_cart_item)
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_accessories.name + " and " + str(len(session['ShoppingCart'])-1) + " other item(s) are waiting for you to check out!.....")
       return redirect(request.referrer)
    else:
       session['ShoppingCart'] = add_cart_item
       message = Markup("<strong> ADDED TO CART! </strong>")
       flash (message + " Your new " + add_accessories.name + ' is waiting for you to check out!.....')
       return redirect(request.referrer)
#######################################






# Remove Products From Shopping Cart Server Paths #
@app.route('/tees/remove_from_cart/<id>', methods=['GET'])
def remove_from_cart_tee(id):
   del_name = "tee_"+id
   if 'ShoppingCart' not in session and len(session['ShoppingCart']) <= 0:
     return redirect(url_for('cart'))
   else:
      session.modified = True
      for key, item in session['ShoppingCart'].items():
         if key == del_name:
           session['ShoppingCart'].pop(key, None)
           return redirect(url_for('cart'))

@app.route('/jackets/remove_from_cart/<id>', methods=['GET'])
def remove_from_cart_jacket(id):
   del_name = "jacket_"+id
   if 'ShoppingCart' not in session and len(session['ShoppingCart']) <= 0:
     return redirect(url_for('cart'))
   else:
      session.modified = True
      for key, item in session['ShoppingCart'].items():
         if key == del_name:
           session['ShoppingCart'].pop(key, None)
           return redirect(url_for('cart'))

@app.route('/pants/remove_from_cart/<id>', methods=['GET'])
def remove_from_cart_pants(id):
   del_name = "pants_"+id
   if 'ShoppingCart' not in session and len(session['ShoppingCart']) <= 0:
     return redirect(url_for('cart'))
   else:
      session.modified = True
      for key, item in session['ShoppingCart'].items():
         if key == del_name:
           session['ShoppingCart'].pop(key, None)
           return redirect(url_for('cart'))

@app.route('/shoes/remove_from_cart/<id>', methods=['GET'])
def remove_from_cart_shoes(id):
   del_name = "shoes_"+id
   if 'ShoppingCart' not in session and len(session['ShoppingCart']) <= 0:
     return redirect(url_for('cart'))
   else:
      session.modified = True
      for key, item in session['ShoppingCart'].items():
         if key == del_name:
           session['ShoppingCart'].pop(key, None)
           return redirect(url_for('cart'))

@app.route('/accessories/remove_from_cart/<id>', methods=['GET'])
def remove_from_cart_accessories(id):
   del_name = "acc_"+id
   if 'ShoppingCart' not in session and len(session['ShoppingCart']) <= 0:
     return redirect(url_for('cart'))
   else:
      session.modified = True
      for key, item in session['ShoppingCart'].items():
         if key == del_name:
           session['ShoppingCart'].pop(key, None)
           return redirect(url_for('cart'))
###########################################






# Normal Shopping Cart Server Paths #
@app.route('/cart', methods=['GET'])
def cart():
    id = 1
    product_1 = product_tee.query.get(id)
    product_2 = product_jacket.query.get(id)
    product_3 = product_pants.query.get(id)
    product_4 = product_shoes.query.get(id)
    product_5 = product_acc.query.get(id)
    return render_template('Shopping_Cart.html', product_1 = product_1, product_2=product_2, product_3=product_3, product_4=product_4, product_5=product_5)

@app.route('/check_out', methods=['GET'])
@login_required
def cashout():
  total = 0
  for key , product in session['ShoppingCart'].items():
    total = total + int(product['price'])
  return render_template('Check_Out.html', total = total)
########################################






# RUN APP ON PORT FUNCTION #
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
############################
