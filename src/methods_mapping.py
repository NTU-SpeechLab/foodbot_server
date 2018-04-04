'''
Created on 27 Nov 2017

@author: ly
'''

from intents.foods_order import *
from intents.promotions import *
from intents.stores_location import *

methods = {
    #This column should be exactly the same with intent name in your api.ai's agent
    'current_promotions':           list_all_promotions,
    'ask_menu':                     show_menu_daily,
    'find_nearest_location':        find_store_locations,
    'list_drink':                   list_all_drinks,
    'list_food_by_cuisine':         list_foods_by_cuisine,
    'list_food_by_keyword':         list_foods_by_name,
    'list_side_dishes':             list_side_dishs,
    'order_food':                   order_food,
    'order_drink':                  order_drink,
    'order_drink_no':               processing_order,
    'order_food_cancel':            clear_order,
    'order_food_confirm':           confirm_the_order,
    'order_food_repeat':            repeat_the_order,
    'order_food_adding':            modify_the_order,
    'food_payment':                 check_payment_methods,
    'ask_food_description':         get_food_description,
    'Default Fallback Intent':      other_processing,

}
