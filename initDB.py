#  Kyle Awah     - (816012635)
#
#  AFTR_MARKT
#  INFO 2602 - Web Programming and Technologies 1 
#
#  initDB.py contains:
#  - imports the CSV file
#  - breaks it down into variables and creates an object from them
#  - stores object as a row in the database 


from main import db, product_tee, product_jacket, product_pants, product_shoes, product_acc, user, app
import csv
db.create_all(app=app);

# ADDING TEES #
with open('Tees.csv', 'r') as csv_file:
    csv_file_contents = csv.reader(csv_file)
    next(csv_file_contents)
    for line in csv_file_contents:
        row_to_add = product_tee(price=line[0], name=line[1], brand=line[2], size=line[3], color=line[4], desc=line[5], catagory=line[6])
        db.session.add(row_to_add)
        db.session.commit()

# ADDING JACKETS # 
with open('Jackets.csv', 'r') as csv_file:
    csv_file_contents = csv.reader(csv_file)
    next(csv_file_contents)
    for line in csv_file_contents:
        row_to_add = product_jacket(price=line[0], name=line[1], brand=line[2], size=line[3], color=line[4], desc=line[5], catagory=line[6])
        db.session.add(row_to_add)
        db.session.commit()

# ADDING PANTS # 
with open('Pants.csv', 'r') as csv_file:
    csv_file_contents = csv.reader(csv_file)
    next(csv_file_contents)
    for line in csv_file_contents:
        row_to_add = product_pants(price=line[0], name=line[1], brand=line[2], size=line[3], color=line[4], desc=line[5], catagory=line[6])
        db.session.add(row_to_add)
        db.session.commit()

# ASSING SHOES #
with open('Shoes.csv', 'r') as csv_file:
    csv_file_contents = csv.reader(csv_file)
    next(csv_file_contents)
    for line in csv_file_contents:
        row_to_add = product_shoes(price=line[0], name=line[1], brand=line[2], size=line[3], color=line[4], desc=line[5], catagory=line[6])
        db.session.add(row_to_add)
        db.session.commit()

# ADDING ACCESSORIES # 
with open('Acc.csv', 'r') as csv_file:
    csv_file_contents = csv.reader(csv_file)
    next(csv_file_contents)
    for line in csv_file_contents:
        row_to_add = product_acc(price=line[0], name=line[1], brand=line[2], color=line[3], desc=line[4], catagory=line[5])
        db.session.add(row_to_add)
        db.session.commit()
