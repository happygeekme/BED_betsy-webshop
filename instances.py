from unittest import mock
from models import User, Product, Tag, db, Transaction
import peewee

def create_users_and_products():
    job = User.create(name='job', address='dorpsweg 1, het dorp')
    fleur = User.create(name='fleur', address='stadsweg 2, de stad')
    joris = User.create(name='joris', address='bergweg 235, bergen')
    mila = User.create(name='mila', address='straatweg 103, straten')
    fiore = User.create(name='fiore', address='kleiweg 45, kleien')
    kick = User.create(name='kick', address='kloosterweg 21, kloosteren')

    vaas = Product.create(
        name='vaas',     
        price_per_item=25, 
        quantity=10,
        description='een vaas om bloemen in te zetten of voor decoratie',  
        seller=job
        )

    mok = Product.create(
        name='mok',     
        price_per_item=10, 
        quantity=7,
        description='een mok om warme dranken uit te drinken', 
        seller=job
        )

    armband = Product.create(
        name='armband',     
        price_per_item=5, 
        quantity=15,
        description='een armbandje met kralen in regenboogkleuren', 
        seller=fleur
        )

    ketting = Product.create(
        name='ketting',     
        price_per_item=10, 
        quantity=15,
        description='een ketting met kralen en bedels', 
        seller=fleur
        )

    schilderij_1 = Product.create(
        name='schilderij_1',     
        price_per_item=25, 
        quantity=5,
        description='schilderij van zonsondergang', 
        seller=joris
        )

    schilderij_2 = Product.create(
        name='schilderij_2',     
        price_per_item=25, 
        quantity=5,
        description='schilderij van de maan',  
        seller=joris
        )

    cupcake = Product.create(
        name='cupcake',     
        price_per_item=2.50, 
        quantity=10,
        description='cupcake met blauwe bessen', 
        seller=mila
        )

    appeltaart = Product.create(
        name='appeltaart',     
        price_per_item=11.95, 
        quantity=4,
        description='vers gebakken appeltaart', 
        seller=mila
        )

    sokken = Product.create(
        name='sokken',     
        price_per_item=7.50, 
        quantity=10,
        description='gebreide sokken', 
        seller=fiore
        )

    trui = Product.create(
        name='trui',     
        price_per_item=35, 
        quantity=6,
        description='gebreide trui', 
        seller=fiore
        )

    tafel = Product.create(
        name='tafel',     
        price_per_item=40, 
        quantity=4,
        description='houten tafel',  
        seller=kick
        )

    kast = Product.create(
        name='kast',     
        price_per_item=50, 
        quantity=2,
        description='houten kast', 
        seller=kick
        )
    
    aardewerk = Tag.create(name='aardewerk', product=[vaas, mok])
    houtwerk = Tag.create(name='houtwerk', product = [tafel, kast])
    handwerk = Tag.create(name='handwerk', product=[vaas, mok, armband, ketting, schilderij_1, schilderij_2, sokken, trui, tafel, kast])
    ambachtelijk = Tag.create(name='ambachtelijk', product = [cupcake, appeltaart])
    kleding = Tag.create(name='kleding', product=[trui, sokken])
    meubels = Tag.create(name='meubels', product=[tafel, kast])
    sierraad = Tag.create(name='sierraad', product=[armband, ketting])
    gebak = Tag.create(name='gebak', product=[cupcake, appeltaart])
    decoratie = Tag.create(name='decoratie', product=[vaas, schilderij_1, schilderij_2])
    kado = Tag.create(name='kado', product=[vaas, mok, ketting, armband, schilderij_1, schilderij_2])

    return(job, fleur, joris, mila, fiore, kick, vaas, mok, armband, ketting, schilderij_1, schilderij_2, cupcake, appeltaart, sokken, trui, tafel, kast, aardewerk, houtwerk, handwerk, ambachtelijk, kleding, meubels, sierraad, gebak, decoratie, kado)

db.create_tables([User, Product, Tag, Transaction])

create_users_and_products()

