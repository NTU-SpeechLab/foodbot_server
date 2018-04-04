from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

###############################################################################
engine = create_engine('mysql+mysqlconnector://root:<yourpassword>@localhost/canteena_fnb?charset=utf8mb4',encoding='utf8')
Base = declarative_base()

#######################################################################
#
# DATABASE CREATION & PREPARATION: TABLE DEFINITION
#
#######################################################################
class Food(Base):
    """"""
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50), primary_key=True)
    ftype = Column(String(20))
    fdesc = Column(String(200))
    fimg  = Column(String(400))
    fprice = Column(Float)

    #--------------------------------------------------------------------------
    def __init__(self, foodname, foodtype, desc, foodprice, imglink):
        """"""
        self.fname = foodname
        self.ftype = foodtype
        self.fdesc = desc
        self.fprice = foodprice
        self.fimg = imglink


class Drink(Base):
    """"""
    __tablename__ = "drink"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dname = Column(String(50), primary_key=True)
    dtype = Column(String(20))
    ddesc = Column(String(200))
    fimg  = Column(String(400))
    dprice = Column(Float)

    #--------------------------------------------------------------------------
    def __init__(self, drinkname, dtype, ddesc, dprice, imglink):
        """"""
        self.dname = drinkname
        self.dtype = dtype
        self.ddesc = ddesc
        self.dprice = dprice
        self.fimg = imglink


class SideDish(Base):
    """"""
    __tablename__ = "side_dish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sdname = Column(String(50), primary_key=True)
    sdtype = Column(String(20))
    sddesc = Column(String(200))
    fimg  = Column(String(400))
    sdprice = Column(Float)

    #--------------------------------------------------------------------------
    def __init__(self, sdname, sdtype, sddesc, sdprice, imglink):
        """"""
        self.sdname = sdname
        self.sdtype = sdtype
        self.sddesc = sddesc
        self.sdprice = sdprice
        self.fimg = imglink


class FnBModification(Base):
    """"""
    __tablename__ = "fnb_option"

    id = Column(Integer, primary_key=True)
    size = Column(String(20))
    multiplier = Column(Float)

    #--------------------------------------------------------------------------
    def __init__(self, size, multiple_price):
        """"""
        self.size = size
        self.multiplier = multiple_price


class OrderDetail(Base):
    """"""
    __tablename__ = "order_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    no = Column(Integer)
    fnbname = Column(String(20))
    side_id = Column(Integer)
    user_id = Column(String(20))

    #--------------------------------------------------------------------------
    def __init__(self, numberofitems, food_or_drink_name, modifier_id, customer_id):
        """"""
        self.no = numberofitems
        self.fnbname = food_or_drink_name
        self.side_id = modifier_id
        self.user_id = customer_id


class OrderArchive(Base):
    """"""
    __tablename__ = "order_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    no = Column(Integer)
    user_id = Column(String(20))
    detail_order = Column(String(500))

    #--------------------------------------------------------------------------
    def __init__(self, archive_no, numberofitems, food_or_drink_name, customer_id, modifier_id):
        """"""
        self.no = archive_no
        self.user_id = customer_id
        self.detail_order = ""
        for idx, item in enumerate(numberofitems):
            self.detail_order = self.detail_order + "; " + str(item) + ": " + food_or_drink_name[idx]
        # end of processing init/adding data.


class UserReference(Base):
    """"""
    __tablename__ = "user_info"

    userid = Column(String(20), primary_key=True)
    preferfood = Column(String(20))
    preferdrink = Column(String(20))


    #--------------------------------------------------------------------------
    def __init__(self, user_id, order_details, prefer_food, prefer_drink):
        """"""
        self.userid  = user_id
        self.preferfood = prefer_food
        self.preferdrink = prefer_drink


# create tables
Base.metadata.create_all(engine)


#######################################################################
#
# INTERFACE WITH SQL CURSOR - QUERY FROM DATABASE
#
#######################################################################

#######################################################################
#
# INTERFACE WITH OTHER MODULES
#
#######################################################################


if __name__ == '__main__':
    print ("Creating the tables for canteena_fnb database !")
