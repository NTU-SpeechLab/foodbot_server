# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fnb_definition import *

engine = create_engine('mysql+mysqlconnector://<your_sql_username>:<your_sql_password>@localhost/canteena_fnb?charset=utf8',encoding='utf8')

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# ---------------------- FOOD table -------------------#
food = Food("char kway teow", "local",
            "Char kway teow, literally 'stir-fried ricecake strips', is a popular noodle dish in Malaysia, Singapore, Brunei and Indonesia. The dish is considered a national favourite in Malaysia and Singapore",
            3.1, "https://www.nyonyacooking.com/images/recipes/char-kway-teow.jpg")
session.add(food)

food = Food("hokkien prawn mee", "chinese",
            "Hokkien Prawn Mee, is another favourite of every local in Singapore.",
            3.2, "https://rasamalaysia.com/wp-content/uploads/2011/01/hokkien-mee-8.jpg")
session.add(food)

food = Food("mee siam", "chinese",
            "Mee siam, which means 'Siamese noodle' in Malay, is a dish of thin rice vermicelli popular in Singapore and Malaysia.",
            3.3, "http://mayakitchenette.com/wp-content/uploads/2014/07/mee-siam-recipe-3.jpg")
session.add(food)

food = Food("wanton mee", "chinese",
            "Wonton noodles is a Cantonese noodle dish which is popular in Guangzhou, Hong Kong, Malaysia, Singapore and Thailand.",
            3.4,
            "https://c4.staticflickr.com/8/7386/27790732171_558d9ac9d3_b.jpg")
session.add(food)

food = Food("bak kut teh", "local", "Singapore Teochew Bak Kut Teh is a version of pork ribs tea with a clear garlicky and peppery broth. Only a few ingredients and very easy to prepare.",
            3.5, "https://www.rotinrice.com/wp-content/uploads/2016/12/ST-BakKutTeh-1.jpg")
session.add(food)

food = Food("nasi lemak", "malay", "Nasi lemak is a Malay fragrant rice dish cooked in coconut milk and pandan leaf. It is commonly found in Malaysia, where it is considered the national dish; it is also popular in neighbouring areas such as Singapore; Brunei, and Southern Thailand.",
            3.6, "https://d1alt1wkdk73qo.cloudfront.net/images/guide/6abb55670f06cebacdc5023d11367153/640x478_ac.jpg")
session.add(food)

food = Food("bak chor mee", "Chinese", " Bak Chor Mee literally means “minced meat and noodles” in the Teochew dialect. ",
            3.7, "https://mtc1-dydfxmh.netdna-ssl.com/wp-content/uploads/2017/03/P1040774-1300x867.jpg")
session.add(food)

food = Food("oyster omelette", "taiwanese", "The oyster omelette is a dish that is widely known for its savoury taste in Taiwan, Fujian and Chaoshan, as well as many parts of Asia",
            3.8, "https://sethlui.com/wp-content/uploads/2016/01/Hup-Kee-Fried-Oyster-Omelette-630x420.jpg")
session.add(food)

food = Food("roti prata", "indian", "Savour the delicious roti prata which is crispy on the outside but soft on the inside. This South-Indian flatbread will always satisfy your palette.",
            1.9, "http://www.visitsingapore.com/content/dam/desktop/global/dining-drinks-singapore/local-dishes/roti-prata-carousel01-square.jpeg")
session.add(food)

food = Food("chicken rice", "local", "Hainanese chicken rice is a dish adapted from early Chinese immigrants originally from Hainan province in southern China.",
            4.0, "https://upload.wikimedia.org/wikipedia/commons/7/71/Hainanese_Chicken_Rice.jpg")
session.add(food)


food = Food("hokkien mee", "chinese", "Hokkien mee is a dish in Malaysian and Singaporean cuisine that has its origins in the cuisine of China's Fujian province.",
            4.0, "https://mtc1-dydfxmh.netdna-ssl.com/wp-content/uploads/2016/12/16069838051_c75eb4dd99_o-1300x867.jpg")
session.add(food)

food = Food("oyster omelette", "taiwanese", "The oyster omelette is a dish that is widely known for its savoury taste in Taiwan, Fujian and Chaoshan, as well as many parts of Asia.",
            4.0, "https://sethlui.com/wp-content/uploads/2016/01/Hup-Kee-Fried-Oyster-Omelette-630x420.jpg")
session.add(food)

food = Food("curry fish head", "chinese", "Fish head curry is a dish in Singaporean and Malaysian cuisine with Indian and Chinese origins. The head of a red snapper is semi-stewed in a Kerala-style curry with assorted vegetables such as okra and eggplants.",
            4.0, "https://farm5.staticflickr.com/4233/35800092885_902a64e85b_o.jpg")
session.add(food)

food = Food("biryani", "indian", "Biryani, also known as biriyani, biriani, birani or briyani, 'spicy rice' is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent.",
            4.0, "http://www.ndtv.com/cooks/images/mutton-biryani-new.jpg")
session.add(food)

food = Food("hokkien char mee", "chinese", "Hokkien mee is a dish in Malaysian and Singaporean cuisine that has its origins in the cuisine of China's Fujian (Hokkien) province. In its most common form, the dish consists of egg noodles and rice noodles stir-fried with egg, slices of pork, prawns and squid, and served and garnished with vegetables, small pieces of lard, sambal sauce and lime (for adding the lime juice to the dish).",
            4.0, "https://www.google.com.sg/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiT-eyn_IjaAhWMvI8KHSJoC30QjRx6BAgAEAU&url=http%3A%2F%2Fdinnerwithtina.blogspot.com%2F2014%2F06%2Fstir-fried-hokkien-noodles-with.html&psig=AOvVaw3ECoabJKbZH7CKS7yTzKcw&ust=1522118733531148")
session.add(food)

food = Food("rojak", "malay", "Rojak or Rujak is a traditional fruit and vegetable salad dish commonly found in Indonesia, Malaysia and Singapore. Other than referring to this fruit salad dish, the term rojak also means 'mixture' or 'eclectic mix' in colloquial Malay. ",
            4.0, "http://www.visitsingapore.com/dining-drinks-singapore/local-dishes/rojak/_jcr_content/par-carousel/carousel_detailpage/carousel/item_2.thumbnail.carousel-img.740.416.jpg")
session.add(food)

food = Food("bee hoon", "chinese", "Rice vermicelli are a thin form of rice noodles. They are sometimes referred to as rice noodles, rice sticks, or bee hoon, but they should not be confused with cellophane noodles which are a different Asian type of vermicelli made from mung bean starch or rice starch rather than rice grains itself.",
            4.0, "https://s3-ap-southeast-1.amazonaws.com/afc-prod/thumbnails/standard_mobile/5415/0286/1193/tn-HFM-Braised-Pig-Trotter-Bee-Hoon.jpg")
session.add(food)

food = Food("bun bo hue", "vietnamese", "Bun bo Hue or bun bo is a popular Vietnamese soup containing rice vermicelli (bun) and beef (bò). Huế is a city in central Vietnam associated with the cooking style of the former royal court. The dish is greatly admired for its balance of spicy, sour, salty and sweet flavors and the predominant flavor is that of lemon grass.",
            4.0, "https://media.foody.vn/res/g65/642530/prof/s/foody-mobile-ba-thu-jpg-537-636255976625248994.jpg")
session.add(food)

food = Food("pho bo", "vietnamese", "Pho is a Vietnamese soup consisting of broth, rice noodles called 'banh pho', a few herbs, and meat, primarily made with either beef or chicken. ",
            4.0, "http://thila.com.vn/en/upload/pho-bo-bap-hoa-30-11-2017-17-52-15.jpg?w=400&h=400&zc=0&q=100&")
session.add(food)

food = Food("pho", "vietnamese", "Pho is a Vietnamese soup consisting of broth, rice noodles called 'banh pho', a few herbs, and meat, primarily made with either beef or chicken. ",
            4.0, "https://taxiairport.vn/uploads/ckeditor/images/%5E7773CA1C492E6FA75D868CBFEEEB798876EDFC409543529799%5Epimgpsh_fullsize_distr.png")
session.add(food)

food = Food("spaghetti with chicken bolognese", "western", "This family dinner recipe combines lean ground chicken, linguine, and classic Bolognese ingredients.",
            4.0, "https://www.daringgourmet.com/wp-content/uploads/2013/02/Chicken-Spaghetti-1-sm.jpg")
session.add(food)

food = Food("spaghetti with ham and mushroom", "western", "Delicious pieces of ham add a meaty touch to this hearty pasta dish.",
            4.0, "https://img.taste.com.au/pSKAAN57/w720-h480-cfill-q80/taste/2016/11/mushroom-and-ham-spaghetti-25701-1.jpeg")
session.add(food)

food = Food("spaghetti with chicken chop", "western", "Chicken Chop in mushroom sauce with pasta in tomato sauce and saute assorted capsicum!",
            4.0, "http://1.bp.blogspot.com/-VKJwtLwNayI/UIN_P8EUNVI/AAAAAAAACAA/SuES6VlzQEQ/s1600/IMG_9499+edit.JPG")
session.add(food)

food = Food("spaghetti with chicken cutlet", "western", "Chicken Cutlets and Spaghetti with Peppers and Onions",
            4.0, "https://search.chow.com/thumbnail/800/0/www.chowstatic.com/assets/2015/04/31394_chicken_parmesan_spaghetti_inline_640_2.jpg")
session.add(food)

food = Food("spaghetti with sausage", "western", "Quick and easy spaghetti recipe with Italian sausage. The tomato-based sauce gets its seasoning from the sweet and spicy sausages. Our favorite way to make spaghetti!",
            4.0, "https://www.simplyrecipes.com/wp-content/uploads/2006/09/italian-sausage-spaghetti-vertical-a-600.jpg")
session.add(food)

food = Food("singapore pasta", "western", "Pasta is a staple food of traditional Italian cuisine, with the first reference dating to 1154 in Sicily. Also commonly used to refer to the variety of pasta dishes, pasta is typically made from an unleavened dough of a durum wheat flour mixed with water or eggs and formed into sheets or various shapes.",
            4.0, "https://i.ytimg.com/vi/6aVOjLuw-Qg/maxresdefault.jpg")
session.add(food)

food = Food("aglio olio chicken chop", "western", "Aglio Olio Chicken Chop",
            4.0, "http://4.bp.blogspot.com/-7UwaNrcWZqI/TrFHDzzFHzI/AAAAAAAAKd0/UtaHvJhV0QE/s1600/Grilled+Chicken+with+Pasta+Aglio+E+Olio+October+31st%252C+2011.jpg")
session.add(food)

food = Food("aglio olio chicken cutlet", "western", "Aglio Olio Chicken Cutlet",
            4.0, "http://cookdiary.net/wp-content/uploads/images/Chicken-and-Noodles.jpg")
session.add(food)

food = Food("fish burger", "western", "Fish Burger",
            4.0, "https://d1yupijb0jmhpf.cloudfront.net/52929f79-a794-4249-8a8f-bafe64b35a4a.png")
session.add(food)

food = Food("chicken burger", "western", "Chicken Burger",
            4.0, "https://www.chicken.ca/assets/RecipePhotos/_resampled/FillWyI3MjAiLCI2MDAiXQ/Moist-Chicken-Burgers.jpg")
session.add(food)

food = Food("fish n chips", "western", "Fish and fries",
            4.0, "https://d2iq9gqtfwsete.cloudfront.net/wp-content/uploads/2017/11/mcd3.jpg?x20326")
session.add(food)

# ---------------------- DRINK table -------------------#
drink = Drink("clementi", "local", "lemon tea", 0.7, "https://health.trythis.co/wp-content/uploads/sites/2/2018/01/Lemon-Tea-Treats-Stomach-Pain.jpg")
session.add(drink)

drink = Drink("kopi", "local", "coffee", 0.7, "http://img.beritasatu.com/cache/beritasatu/910x580-2/1455707867.jpg")
session.add(drink)

drink = Drink("tak kiu", "local", "tak kiu", 0.8, "http://www.rediscovernew.shangri-la.com/wp-content/uploads/2017/08/beverage_7-300x225.jpg")
session.add(drink)

drink = Drink("bubble tea", "local", "bubble tea", 2.7, "https://truffle-assets.imgix.net/pxqrocxwsjcc_3XWh6BV9wAwc8eKcgICgAY_homemade-bubble-tea_squareThumbnail_en.png")
session.add(drink)

drink = Drink("soy bean", "local", "soy bean", 1.0, "http://eatwhattonight.com/wp-content/uploads/2016/04/Soya-Bean-Drink_4.jpg")
session.add(drink)

drink = Drink("teh", "local", "tea", 0.6, "http://carnivalmunchies.com/wp-content/uploads/2015/12/6836327620_648f79b711_o.jpg")
session.add(drink)

drink = Drink("milk tea", "local", "milk tea", 0.9, "https://i2-prod.mirror.co.uk/incoming/article6201545.ece/ALTERNATES/s615/Cup-of-tea.jpg")
session.add(drink)

drink = Drink("coffee", "local", "coffee", 0.7, "https://drinks.seriouseats.com/images/2012/08/20120802-singapore-kopi.jpg")
session.add(drink)

# ---------------------- SIDE DISHES table -------------------#
sidedish = SideDish("salad", "local", "salad", 1.0, "http://recipes.heart.org/-/media/aha/recipe/recipe-images/mediterranean-salad.jpg")
session.add(sidedish)

sidedish = SideDish("fries", "local", "french fries", 1.0, "http://www.alwaha.pk/wp-content/uploads/2017/11/french-fries-1200.jpg")
session.add(sidedish)

sidedish = SideDish("pasta", "local", "pasta", 1.0, "http://img1.cookinglight.timeinc.net/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/2017/05/main/pasta-chickpea-sauce-1707p46.jpg?itok=Jmv3zJMU")
session.add(sidedish)

sidedish = SideDish("spaghetti", "local", "spaghetti", 1.0, "https://www.seriouseats.com/recipes/images/2016/03/20160209-amatriciana-pasta-vicky-wasik-017-1500x1125.jpg")
session.add(sidedish)

sidedish = SideDish("soup", "local", "soup", 1.0, "https://static01.nyt.com/images/2016/11/29/dining/recipelab-chick-noodle-still/recipelab-chick-noodle-still-videoSixteenByNineJumbo1600.jpg")
session.add(sidedish)

sidedish = SideDish("mash-potato", "local", "mash potato", 1.0, "https://static01.nyt.com/images/2015/10/30/dining/30COOKING-MASHEDPOTATOES1/30COOKING-MASHEDPOTATOES1-superJumbo.jpg")
session.add(sidedish)

# ---------------------- FOOD MODIFIER table -------------------#
fmodifier = FnBModification("more", 1.2)
session.add(fmodifier)

fmodifier = FnBModification("less", 0.85)
session.add(fmodifier)

fmodifier = FnBModification("regular", 1.0)
session.add(fmodifier)

fmodifier = FnBModification("normal", 1.0)
session.add(fmodifier)

fmodifier = FnBModification("small", 0.85)
session.add(fmodifier)

fmodifier = FnBModification("large", 1.2)
session.add(fmodifier)

fmodifier = FnBModification("extra", 1.2)
session.add(fmodifier)

fmodifier = FnBModification("extra-large", 1.2)
session.add(fmodifier)


# commit the record the database
session.commit()
session.commit()
