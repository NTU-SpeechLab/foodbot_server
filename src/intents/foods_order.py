'''
Created on 27 Nov 2017

@author: ly
'''
import json
import pprint

from sqlalchemy.orm import sessionmaker
from resources.fnb_definition import create_engine, Food, Drink, SideDish, OrderDetail, OrderArchive

__DEBUG__ = True
engine = create_engine('mysql+mysqlconnector://root:<rootpassword>@localhost/canteena_fnb', pool_recycle=3600)
Session = sessionmaker(bind=engine)
s = Session()


def check_payment_methods(params):
    payment_method = str(params[0]).lower()
    retStr = ""

    if (payment_method == 'cash') or (payment_method == 'card'):
        retStr = "Sure. You can pay by cash or card at the NorthSpine counter."
    else:
        retStr = "Sorry, we are not supporting payment by " + payment_method

    order_id = random.randint(1,1000) * 5
    uid = str(params[ len(params) - 1 ])

    # Clear and archive the order detail.
    has_entry = 0
    no_of_items = []
    food_or_drink = []

    for ord_detail in s.query(OrderDetail.fnbname, OrderDetail.no).filter(OrderDetail.user_id == (uid)):
        has_entry = 1
        no_of_items.append(ord_detail[1])
        food_or_drink.append(ord_detail[0])

    # Add the order for user id into a table of order history!
    order_archive = OrderArchive(order_id, no_of_items, food_or_drink, uid, 0)
    s.add(order_archive)
    s.commit()

    # Delete the info in the order detail, moved into history table already.
    s.query(OrderDetail.id).filter(OrderDetail.user_id == uid).delete()
    s.commit()

    return {"text" : [retStr, "Your order id is " + str(order_id) + ". Please show this number when you purchasing at cashier."]}


def other_processing(params):
    pass


def format_text_response(messages):
    return {
        "text": {
          "text": [messages]
          }
        }

def show_menu_daily(params):
    retStr = "We have a lot of food (Chinese food, local food, Western food, Indian Food, Malay food, Vietnamese food, etc.) and beverages"
    return {"text" : [retStr], "quickReplies": ["You can view the detail food and beverages before ordering", "Try Chinese food", "Local food", "List of beverages"]}


def list_all_drinks(params):
    retStr = "List of beverage in our menu: "

    for value in s.query(Drink.dname).distinct():
        if (__DEBUG__):
            pprint.pprint(value)
            print ("Drink: " + str(value[0]))
        retStr = retStr + " \n " + str(value[0]) + ", "

    retStr = retStr[:len(retStr) - 2]
    if (__DEBUG__):
        print ("List of beverage are available: " + retStr)

    imgs = []
    for value in s.query(Drink.fimg, Drink.dname).distinct():
        if (__DEBUG__):
            pprint.pprint(value)
            print ("Food images: " + str(value[0]))
        imgs.append(str(value[1]))
        imgs.append(str(value[0]))

    return {"text": [retStr, "Would you like something to drink?"], "cards": imgs}


def list_foods_by_cuisine(params):
    prefer_cuisine = str(params[0]).lower()
    retStr = "List of " + prefer_cuisine + " food is: "

    for value in s.query(Food.fname).filter(Food.ftype.in_([ prefer_cuisine ])):
        if (__DEBUG__):
            pprint.pprint(value)
            print ("Food: " + str(value[0]))
        retStr = retStr + " \n " + str(value[0]) + ", "

    retStr = retStr[:len(retStr) - 2]

    imgs = []
    for value in s.query(Food.fimg, Food.fname).filter(Food.ftype.in_([ prefer_cuisine ])):
        if (__DEBUG__):
            pprint.pprint(value)
            print ("Food images: " + str(value[0]))
        imgs.append(str(value[1]))
        imgs.append(str(value[0]))

    if (__DEBUG__):
        print ("List of food belonged to this group: " + retStr)

    return {"text": [retStr], "cards": imgs}


def list_foods_by_name(params):
    keywords = params[0]
    retStr = ''

    for food_name in keywords:
        for value in s.query(Food.fname).filter(Food.fname.like('%' + food_name + '%')):
            if (__DEBUG__):
                pprint.pprint(value)
                print ("Food: " + str(value[0]))
            retStr = retStr + " \n " + str(value[0]) + ", "

    return {"text": [retStr, "Is this you are looking for?"]}


def get_food_description(params):
    keyword_food = params[0]
    keyword_drink = params[1]

    retRes = {}
    if (keyword_food != ''):
        for value in s.query(Food.fname, Food.fimg, Food.fdesc).filter(Food.fname.like('%' + keyword_food + '%')):
            if (__DEBUG__):
                pprint.pprint(value)
                print ("Food: " + str(value[2]))
            retRes = {"text": [value[2]], "cards": [value[0], value[1]]}
    if (keyword_drink != ''):
        for value in s.query(Drink.dname, Drink.fimg, Drink.ddesc).filter(Drink.dname.like('%' + keyword_drink + '%')):
            if (__DEBUG__):
                pprint.pprint(value)
                print ("Food: " + str(value[0]))
            retRes = {"text": [value[2]], "cards": [value[0], value[1]]}

    return retRes


def list_side_dishs(params):
    retStr = "List of side dishes in our menu: "

    for value in s.query(SideDish.sdname).distinct():
        if (__DEBUG__):
            pprint.pprint(value)
            print ("Drink: " + str(value[0]))
        retStr = retStr + " \n " + str(value[0]) + ", "

    retStr = retStr[:len(retStr) - 2]

    imgs = []
    for value in s.query(SideDish.fimg, SideDish.sdname).distinct():
        if (__DEBUG__):
            pprint.pprint(value)
            print ("Food images: " + str(value[0]))
        imgs.append(str(value[1]))
        imgs.append(str(value[0]))


    if (__DEBUG__):
        print ("List of side dishes are available: " + retStr)
    return {"text": [retStr, "Adding anything?"], "cards": imgs}


def ask_about_side_dishes():
    return ""


def checking_price(foods, units):
    retStr = "Total price: S$"
    totalprice = 0.0

    for idx, item in enumerate(foods):
        query = s.query(Food.fprice).filter(Food.fname.in_([foods[0]]))
        result = query.first()
        unit_price = 3.0
        if result:
            unit_price = float(result[0])
            if (__DEBUG__):
                print ("Checking price of your order")
                pprint.pprint(result[0])

        noItems = 1.0
        if (idx < len(units) ):
            numberStr = ""
            if (units[idx] != None):
                numberStr = str(units[idx]).replace("\"", "")
            noItems = float(numberStr)
        totalprice = totalprice + unit_price * noItems

    if (__DEBUG__):
        print ("Total price: " + str(totalprice))
    return (retStr + str(totalprice))


def order_food(params):
    if (__DEBUG__):
        print ("updated params")
        pprint.pprint(params)

    no_of_params = len(params)

    foods = []
    units = []
    uid = params[no_of_params - 1]

    retStr = "Your order is: "
    if (type(params) == type([])):
        # process the parameter
        foods = params[0] #list
        units = params[1] #list

    if (len(foods) >= 1 and len(units) == 0):
        units = [1]

    if (len(foods) == len(units)):
        #for item in foods:
        for idx, item in enumerate(foods):
            no_of_items = (str(units[idx]).replace("\"", ""))
            retStr = retStr + str(int(float(no_of_items))) + " " + item + ", "

            # Add the order for user id into a table for tracking!
            order_i = OrderDetail(units[idx], item, "regular", uid)
            s.add(order_i)
            s.commit()

        # remove the ", " at the end.
        retStr = retStr[:len(retStr) - 2]

    totalprice = checking_price(foods, units)

    if (__DEBUG__):
        pprint.pprint(foods)
        pprint.pprint(units)
        print (retStr)

    latest_query = retStr
    return {"text": [retStr], "quickReplies": [totalprice, "Confirm", "Wanna drink?", "Cancel"]}


def order_drink(params):
    if (__DEBUG__):
        pprint.pprint(params)

    uid = str(params[ len(params) - 1 ])
    drinks = []
    units = []
    retStr = "Your order is: "
    if (type(params) == type([])):
        # process the parameter
        drinks = params[1] #list
        units = params[0] #list

    if (len(drinks) >= 1 and len(units) == 0):
        units = [1]

    if (len(drinks) == len(units)):
        #for item in foods:
        for idx, item in enumerate(drinks):
            retStr = retStr + str(units[idx]) + " " + item + ", "
            # Add the order for user id into a table for tracking!
            order_i = OrderDetail(units[idx], item, "regular", uid)
            s.add(order_i)
            s.commit()

        # remove the ", " at the end.
        retStr = retStr[:len(retStr) - 2]

    totalprice = checking_price(drinks, units)

    if (__DEBUG__):
        pprint.pprint(drinks)
        pprint.pprint(units)
        print (retStr)
    return {"text": [retStr, totalprice, "Anything else?"]}


def clear_order(params):
    uid = str(params[ len(params) - 1 ])

    print ("Clearing your order")
    s.query(OrderDetail.id).filter(OrderDetail.user_id == uid).delete()
    s.commit()

    return {"text": ["Ok, your order is clear. Do you want to restart the ordering?"]}


def repeat_the_order(params):
    uid = str(params[ len(params) - 1 ])

    responseStr = "Your latest order: \n"
    has_entry = 0

    for ord_detail in s.query(OrderDetail.fnbname, OrderDetail.no).filter(OrderDetail.user_id == (uid)):
        responseStr = responseStr + str(ord_detail[1]) + " " + ord_detail[0] + "\n"
        has_entry = 1

    if (has_entry == 1):
        responseStr = responseStr[:len(responseStr) - 1]
    else:
        responseStr = "Sorry, but you haven't ordered anything yet."
    return {"text": [responseStr, "Is this right?"]}


def confirm_the_order(params):
    uid = str(params[ len(params) - 1 ])
    if (__DEBUG__):
        print ("User id is: " + str(uid))

    responseStr = "Your order: \n"
    ask_for_more = "Do you want to pay by cash or card?"

    has_entry = 0
    no_of_items = []
    food_or_drink = []

    for ord_detail in s.query(OrderDetail.fnbname, OrderDetail.no).filter(OrderDetail.user_id == (uid)):
        has_entry = 1
        responseStr = responseStr + str(ord_detail[1]) + " " + ord_detail[0] + "\n"
        if (__DEBUG__):
            print ("FOUND: " + str(ord_detail[1]) + " " + ord_detail[0] + "\n")

        no_of_items.append(ord_detail[1])
        food_or_drink.append(ord_detail[0])

    totalprice = checking_price(food_or_drink, no_of_items)
    responseStr = responseStr + ". " + str(totalprice)

    if (has_entry == 0):
        responseStr = "Great."
        ask_for_more = "What food or drink you want?"

    return {"text": [responseStr, ask_for_more]}


def modify_the_order(params):
    pass


import random
def processing_order(params):
    order_id = random.randint(1,1000) * 5
    uid = str(params[ len(params) - 1 ])

    # Clear and archive the order detail.
    has_entry = 0
    no_of_items = []
    food_or_drink = []
    order_detail = "Detail of your order is: "

    for ord_detail in s.query(OrderDetail.fnbname, OrderDetail.no).filter(OrderDetail.user_id == (uid)):
        has_entry = 1
        no_of_items.append(ord_detail[1])
        food_or_drink.append(ord_detail[0])
        order_detail = order_detail + str(ord_detail[1]) + " " + str(ord_detail[0]) + ", "

    # Add the order for user id into a table of order history!
    order_archive = OrderArchive(order_id, no_of_items, food_or_drink, uid, 0)
    s.add(order_archive)
    s.commit()

    # Delete the info in the order detail, moved into history table already.
    s.query(OrderDetail.id).filter(OrderDetail.user_id == uid).delete()
    s.commit()

    if (has_entry == 0):
        return {"text": ["Ok."]}
    else:
        return {"text": [order_detail[:len(order_detail) - 1], "Your order id is " + str(order_id) + ". Please show this number when you purchasing at cashier."]}
